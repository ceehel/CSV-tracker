import sys
from menus import main_menu, task_menu
from tables import define_name, define_headers, Table

while True:
    main_menu()
    choice = input()

    match choice:
        case "1":
            name = define_name()
            headers = define_headers()
            Table(name, headers)
            task_menu(name)
            input()
        case "2":
            print("you chose 2")
        case "3":
            print("\nGood bye !")
            sys.exit()
        case _:
            print("Please enter a valid choice")
