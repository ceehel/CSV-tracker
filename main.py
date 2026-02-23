import sys
from menus import main_menu
from tables import define_name, define_headers, Table, table_selector, open_table

while True:
    main_menu()
    choice = input()

    match choice:
        case "1":
            name = define_name()
            headers = define_headers()
            Table(name, headers)
            open_table(name)
        case "2":
            table = table_selector()
            open_table(table)
        case "3":
            print("\nGood bye !")
            sys.exit()
        case _:
            print("\nPlease enter a valid choice")
