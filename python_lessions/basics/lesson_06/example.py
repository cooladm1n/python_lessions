"""
Lesson 06: Strings and File I/O
"""
from pathlib import Path
from datetime import datetime

content = "Python makes file I/O easy.\nSecond line."
path = Path("sample.txt")

# Write
with path.open("w", encoding="utf-8", newline="\n") as f:
    f.write(content)

# Read
with path.open("r", encoding="utf-8") as f:
    text = f.read()

print("read back:")
print(text)

# Count lines, words, chars
lines = text.splitlines()
num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = len(text)
print("counts:", num_lines, num_words, num_chars)

# Replace and write to a new file
replaced = text.replace("Python", "PYTHON")
Path("sample_upper.txt").write_text(replaced, encoding="utf-8")

# CSV-like parse and join
csv_line = "a,b, c ,d"
parts = [p.strip() for p in csv_line.split(",")]
print("csv parts:", parts)
print("rejoined:", ";".join(parts))

# Timestamped log
log_path = Path("app.log")
with log_path.open("a", encoding="utf-8") as f:
    f.write(f"{datetime.utcnow().isoformat()}Z - message example\n")

# UTF-8 read/write demo
emoji_file = Path("emoji.txt")
emoji_file.write_text("Hello 👋, café, naïve", encoding="utf-8")
print("emoji read:", emoji_file.read_text(encoding="utf-8"))
