import json
import os
import subprocess
import tempfile
from list_issues import list_issues

ISSUES_FILE = "issues.json"


def open_editor_for_text(initial_text):
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


def edit_issue():
    issues = list_issues()
    if not issues:
        return

    try:
        choice = int(input("\nSelect issue number to edit: "))
        issue = issues[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection")
        return

    print(f"\nEditing issue: {issue['title']}")

    new_title = input(
        f"New title (leave empty to keep '{issue['title']}'): "
    ).strip()

    if new_title:
        issue["title"] = new_title

    new_description = open_editor_for_text(
        issue["description"]
    )

    if new_description:
        issue["description"] = new_description

    with open(ISSUES_FILE, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)

    print("\nIssue updated successfully")
    print(f"ID: {issue['id']}")
    print(f"Title: {issue['title']}")
