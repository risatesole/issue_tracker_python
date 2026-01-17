from create_issue import create_local_issue
from read_issue import read_issue
from close_issue import close_issue
from edit_issue import edit_issue


def main():
    print("1. Create issue")
    print("2. Read issue")
    print("3. Close issue")
    print("4. Edit issue")

    choice = input("Select option: ")

    if choice == "1":
        create_local_issue()
    elif choice == "2":
        read_issue()
    elif choice == "3":
        close_issue()
    elif choice == "4":
        edit_issue()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
