import json
from datetime import datetime
from list_issues import list_issues

ISSUES_FILE = "issues.json"


def close_issue():
    issues = list_issues()
    if not issues:
        return

    try:
        choice = int(input("\nSelect issue number to close: "))
        issue = issues[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection")
        return

    if issue["status"] == "closed":
        print("Issue is already closed.")
        return

    issue["status"] = "closed"
    issue["closed_at"] = datetime.now().isoformat()

    with open(ISSUES_FILE, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)

    print("\nIssue closed successfully")
    print(f"ID: {issue['id']}")
    print(f"Title: {issue['title']}")
    print(f"Closed at: {issue['closed_at']}")
