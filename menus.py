def main_menu():
    print("\nWelcome to CSV Tracker\n")
    print("Please select your desired option")
    print("1 - Create a new table")
    print("2 - Open a table")
    print("3 - Exit")


def new_table_menu():
    print("\nPlease enter the name of the table")


def task_menu(table_name):
    print(
        f"Your table '{table_name}' is loaded. Please select from the options below\n"
    )
    print("1 - Add a task to your table")
    print("2 - Update a task from the table")
    print("3 - Remove a task from the table")
    print("4 - Come back to the main menu")
    print("5 - Exit the program")
