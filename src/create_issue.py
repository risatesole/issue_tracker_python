import json
import uuid
import os
import subprocess
import tempfile
from datetime import datetime

ISSUES_FILE = "issues.json"


def open_editor_for_text(initial_text=""):
    editor = os.environ.get("EDITOR", "vi")

    with tempfile.NamedTemporaryFile(
        suffix=".txt",
        delete=False,
        mode="w",
        encoding="utf-8"
    ) as tf:
        tf.write(initial_text)
        temp_name = tf.name

    subprocess.call([editor, temp_name])

    with open(temp_name, "r", encoding="utf-8") as f:
        content = f.read().strip()

    os.unlink(temp_name)
    return content


def create_local_issue():
    title = input("Issue title: ")
    description = open_editor_for_text(
        "# Write issue description below\n"
        "# Lines starting with # are comments\n\n"
    )

    if not description:
        print("Aborted: empty description")
        return

    issue = {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }

    try:
        with open(ISSUES_FILE, "r", encoding="utf-8") as f:
            issues = json.load(f)
    except FileNotFoundError:
        issues = []

    issues.append(issue)

    with open(ISSUES_FILE, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)

    print("Issue created locally")
    print(f"ID: {issue['id']}")
    print(f"Title: {issue['title']}")
