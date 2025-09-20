# Python Lessons API

FastAPI backend for Python learning platform with lessons, topics, and code testing.

## Features

- **Topics & Lessons**: Organized learning content with thematic structure
- **Code Testing**: Automated testing of student solutions using pytest
- **RESTful API**: Clean API endpoints for frontend integration
- **CORS Support**: Ready for frontend development

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /api/topics` - List all topics
- `GET /api/topics/{topic_id}` - Get topic details with lessons
- `GET /api/lessons` - List all lessons (backward compatibility)
- `GET /api/lessons/{lesson_id}` - Get lesson details with tasks
- `POST /api/submit` - Submit code for testing

## Run locally

Requirements: Python 3.10+

```bash
python -m venv .venv
. .venv/Scripts/activate  # on Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn server.main:app --reload --port 8000
```

API will be available at http://localhost:8000

## How it works
- Backend scans lessons from `python_lessions/` directory structure
- Supports both old format (`lession_XX`) and new format (`topic/lesson_XX`)
- Reads lesson content from `README.md` and task definitions from `tasks.py`
- Runs pytest against `test_tasks.py` in temporary directory for code validation

## Security Notes
- Code execution happens locally in temporary directories
- Do not expose publicly without proper sandboxing
- Consider adding authentication and rate limiting for production use

