from cli.menu import show_menu
from cli.commands import handle_command

def main():
    while True:
        show_menu()
        choice = input("Select: ")

        if choice == "5":
            break

        handle_command(choice)

if __name__ == "__main__":
    main()
