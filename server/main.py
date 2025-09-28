from __future__ import annotations
import json
import re
import shutil
import subprocess
import os
import sys
import tempfile
from pathlib import Path
from typing import List, Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Configuration
ROOT = Path(__file__).resolve().parent.parent
LESSONS_ROOT = ROOT / "python_lessions"
TOPICS_JSON = LESSONS_ROOT / "topics" / "topics.json"

# FastAPI app
app = FastAPI(
    title="Python Lessons API",
    description="API for Python learning platform with lessons, topics, and code testing",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SubmitRequest(BaseModel):
    lesson_id: str
    code: str


def read_topics() -> Dict[str, Any]:
    """Read topics configuration from JSON file."""
    if not TOPICS_JSON.exists():
        return {"topics": []}
    data = json.loads(TOPICS_JSON.read_text(encoding="utf-8"))
    return data


@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "message": "Python Lessons API",
        "version": "1.0.0",
        "endpoints": {
            "topics": "/api/topics",
            "topic_detail": "/api/topics/{topic_id}",
            "lessons": "/api/lessons",
            "lesson_detail": "/api/lessons/{lesson_id}",
            "submit": "/api/submit"
        }
    }


@app.get("/api/topics")
def api_topics_index() -> List[Dict[str, Any]]:
    """Get list of all topics."""
    data = read_topics()
    topics = data.get("topics", [])
    result = []
    for t in topics:
        result.append({
            "id": t["id"],
            "title": t.get("title", t["id"]),
            "lessons_count": len(t.get("lessons", [])),
        })
    return result


@app.get("/api/topics/{topic_id}")
def api_topic_detail(topic_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific topic."""
    data = read_topics()
    topic = next((t for t in data.get("topics", []) if t["id"] == topic_id), None)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Read topic README
    readme_rel = topic.get("readme")
    readme = ""
    if readme_rel:
        readme_path = LESSONS_ROOT / "topics" / readme_rel
        if readme_path.exists():
            readme = readme_path.read_text(encoding="utf-8")
    
    # Map lessons to include basic lesson metadata
    lessons_out = []
    for idx, item in enumerate(topic.get("lessons", []), start=1):
        lesson_id = item["lessonId"]
        lesson_dir = LESSONS_ROOT / lesson_id
        title = lesson_id
        
        # Try to extract title from README
        readme_path = lesson_dir / "README.md"
        if readme_path.exists():
            try:
                first_line = readme_path.read_text(encoding="utf-8").splitlines()[0].strip()
                title = first_line.lstrip("# ") or lesson_id
            except Exception:
                pass
        
        lessons_out.append({
            "displayId": item.get("displayId", f"lesson_{idx:02d}"),
            "lessonId": lesson_id,
            "title": title,
        })
    
    return {
        "id": topic_id,
        "title": topic.get("title", topic_id),
        "readme": readme,
        "lessons": lessons_out
    }


@app.get("/api/lessons")
def api_lessons() -> List[Dict[str, Any]]:
    """Get list of all lessons (for backward compatibility)."""
    return discover_lessons()


@app.get("/api/lessons/{lesson_id:path}")
def api_lesson_detail(lesson_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific lesson."""
    # Support both old format (lession_XX) and new format (topic/lesson_XX)
    if "/" in lesson_id:
        # New format: topic/lesson_XX
        lesson_dir = LESSONS_ROOT / lesson_id
    else:
        # Old format: lession_XX (for backward compatibility)
        lesson_dir = LESSONS_ROOT / lesson_id
    
    if not lesson_dir.exists():
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    # Read lesson files
    readme_path = lesson_dir / "README.md"
    tasks_path = lesson_dir / "tasks.py"
    tests_path = lesson_dir / "test_tasks.py"
    
    readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    tasks_source = tasks_path.read_text(encoding="utf-8") if tasks_path.exists() else ""
    
    # Extract task/function names from tasks.py
    task_names: List[str] = []
    if tasks_path.exists():
        for line in tasks_path.read_text(encoding="utf-8").splitlines():
            # Match function definitions
            m = re.match(r"^def\s+([a-zA-Z_]\w*)\s*\(", line)
            if m:
                task_names.append(m.group(1))
            # Match class definitions
            c = re.match(r"^class\s+([A-Za-z_]\w*)\s*\(", line)
            if c:
                task_names.append(c.group(1))
    
    return {
        "id": lesson_id,
        "readme": readme,
        "tasks": task_names,
        "tasks_source": tasks_source,
        "has_tests": tests_path.exists(),
    }


def discover_lessons() -> List[Dict[str, Any]]:
    """Discover all lessons in the lessons directory."""
    lessons: List[Dict[str, Any]] = []
    if not LESSONS_ROOT.exists():
        return lessons
    
    # First, scan for old format (lession_XX) for backward compatibility
    for entry in sorted(LESSONS_ROOT.iterdir()):
        if entry.is_dir() and re.match(r"^lession_\d+$", entry.name):
            readme = entry / "README.md"
            tasks = entry / "tasks.py"
            tests = entry / "test_tasks.py"
            title = entry.name
            
            if readme.exists():
                try:
                    first_line = readme.read_text(encoding="utf-8").splitlines()[0].strip()
                    title = first_line.lstrip("# ") or entry.name
                except Exception:
                    pass
            
            task_names: List[str] = []
            if tasks.exists():
                try:
                    for line in tasks.read_text(encoding="utf-8").splitlines():
                        m = re.match(r"^def\s+([a-zA-Z_]\w*)\s*\(", line)
                        if m:
                            task_names.append(m.group(1))
                except Exception:
                    pass
            
            lessons.append({
                "id": entry.name,
                "title": title,
                "has_tasks": tasks.exists(),
                "has_tests": tests.exists(),
                "tasks": task_names,
            })
    
    # Then, scan for new format (topic/lesson_XX)
    for topic_dir in sorted(LESSONS_ROOT.iterdir()):
        if topic_dir.is_dir() and not re.match(r"^lession_\d+$", topic_dir.name) and topic_dir.name != "topics":
            for lesson_dir in sorted(topic_dir.iterdir()):
                if lesson_dir.is_dir() and re.match(r"^lesson_\d+$", lesson_dir.name):
                    readme = lesson_dir / "README.md"
                    tasks = lesson_dir / "tasks.py"
                    tests = lesson_dir / "test_tasks.py"
                    title = lesson_dir.name
                    
                    if readme.exists():
                        try:
                            first_line = readme.read_text(encoding="utf-8").splitlines()[0].strip()
                            title = first_line.lstrip("# ") or lesson_dir.name
                        except Exception:
                            pass
                    
                    task_names: List[str] = []
                    if tasks.exists():
                        try:
                            for line in tasks.read_text(encoding="utf-8").splitlines():
                                m = re.match(r"^def\s+([a-zA-Z_]\w*)\s*\(", line)
                                if m:
                                    task_names.append(m.group(1))
                        except Exception:
                            pass
                    
                    lessons.append({
                        "id": f"{topic_dir.name}/{lesson_dir.name}",
                        "title": title,
                        "has_tasks": tasks.exists(),
                        "has_tests": tests.exists(),
                        "tasks": task_names,
                    })
    
    return lessons


def run_pytest_with_student_code(lesson_id: str, student_code: str) -> Dict[str, Any]:
    """Run pytest on student code with lesson tests.

    Notes:
    - This function makes a best-effort attempt to limit damage from untrusted student code
      by running tests inside a temporary directory, using a minimal environment, closing
      stdin, enforcing a timeout and (on Unix) applying soft resource limits.
    - This is NOT a full sandbox. For multi-tenant safety deploy behind container-based
      sandboxes (Docker, gVisor, Firecracker) or sandboxing tools (nsjail, Firejail).
    """

    # Support both old format (lession_XX) and new format (topic/lesson_XX)
    if "/" in lesson_id:
        # New format: topic/lesson_XX
        lesson_dir = LESSONS_ROOT / lesson_id
    else:
        # Old format: lession_XX (for backward compatibility)
        lesson_dir = LESSONS_ROOT / lesson_id

    # Prevent path traversal or accidental access outside LESSONS_ROOT
    try:
        lesson_dir = lesson_dir.resolve()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid lesson path")

    if LESSONS_ROOT not in lesson_dir.parents and LESSONS_ROOT != lesson_dir:
        raise HTTPException(status_code=400, detail="Lesson path outside allowed root")

    tests_src = lesson_dir / "test_tasks.py"
    if not tests_src.exists():
        raise HTTPException(status_code=400, detail="Tests not found for this lesson")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        # Write student file and copy tests strictly inside the temp dir
        student_file = tmp / "tasks.py"
        student_file.write_text(student_code, encoding="utf-8")
        shutil.copy2(tests_src, tmp / "test_tasks.py")

        cmd = [sys.executable, "-m", "pytest", "-q", "--maxfail=1", "--disable-warnings"]

        # Minimal environment for the subprocess to reduce inherited secrets
        safe_env = {
            "PATH": "/usr/bin:/bin" if sys.platform != "win32" else os.environ.get("PATH", ""),
            "PYTHONUNBUFFERED": "1",
        }

        # On Unix, apply resource limits to the child (soft limits)
        preexec_fn = None
        if sys.platform != "win32":
            try:
                import resource

                def _limits():
                    # 2 seconds of CPU time
                    resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
                    # 256 MB address space (soft limit)
                    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, resource.RLIM_INFINITY))

                preexec_fn = _limits
            except Exception:
                preexec_fn = None

        try:
            proc = subprocess.run(
                cmd,
                cwd=str(tmp),
                capture_output=True,
                text=True,
                timeout=60,
                env=safe_env,
                stdin=subprocess.DEVNULL,
                preexec_fn=preexec_fn,
            )
        except subprocess.TimeoutExpired as te:
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"TimeoutExpired: {str(te)}",
            }
        except Exception as e:
            return {
                "success": False,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Execution error: {str(e)}",
            }

        success = proc.returncode == 0
        return {
            "success": success,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }


@app.post("/api/submit")
def api_submit(req: SubmitRequest) -> Dict[str, Any]:
    """Submit student code for testing."""
    # Validate lesson ID format
    old_format = re.match(r"^lession_\d+$", req.lesson_id)
    new_format = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*/lesson_\d+$", req.lesson_id)
    
    if not (old_format or new_format):
        raise HTTPException(status_code=400, detail="Invalid lesson id format")
    
    if not req.code or len(req.code) < 5:
        raise HTTPException(status_code=400, detail="Code is empty")
    
    result = run_pytest_with_student_code(req.lesson_id, req.code)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)