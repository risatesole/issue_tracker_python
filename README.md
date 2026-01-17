# Local Issue Tracker

This is a small **offline issue tracker** built for working locally from the terminal.

It lets you write down problems, ideas, and tasks as issues, keep them stored on disk, read them later, update them, and mark them as closed. Everything lives in a local JSON file and nothing depends on the internet.

Issue descriptions are written using your terminal text editor (`vi`, `nano`, or whatever is set in `$EDITOR`), so writing an issue feels like writing a normal text file, not filling a form.

---

## What it does

* Create issues with a title and description
* Store issues locally in `issues.json`
* List existing issues
* Read full issue details
* Edit issue titles and descriptions
* Close issues and record when they were closed

Each issue keeps basic metadata:

* unique id
* status (open / closed)
* creation date
* close date (if closed)

---

## What it is meant to be

This is not a big system or a platform.
It’s just a **simple local tool** to keep track of things while working on a project.

The code is intentionally small, readable, and split by responsibility so it’s easy to change or extend as needed.
