import json

ISSUES_FILE = "issues.json"


def list_issues():
    try:
        with open(ISSUES_FILE, "r", encoding="utf-8") as f:
            issues = json.load(f)
    except FileNotFoundError:
        print("No issues found.")
        return []

    if not issues:
        print("No issues found.")
        return []

    print("\nIssues:\n")
    for i, issue in enumerate(issues, start=1):
        print(f"{i}. [{issue['status']}] {issue['title']}")

    return issues
