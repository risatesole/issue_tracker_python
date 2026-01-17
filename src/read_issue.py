from list_issues import list_issues


def read_issue():
    issues = list_issues()
    if not issues:
        return

    try:
        choice = int(input("\nSelect issue number to read: "))
        issue = issues[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection")
        return

    print("\n--- ISSUE ---")
    print(f"ID: {issue['id']}")
    print(f"Title: {issue['title']}")
    print(f"Status: {issue['status']}")
    print(f"Created: {issue['created_at']}")

    if issue.get("closed_at"):
        print(f"Closed: {issue['closed_at']}")

    print("\nDescription:\n")
    print(issue["description"])
    print("\n-------------")
