import csv
import os

from menus import new_table_menu, table_open_menu, task_menu


def define_name():
    new_table_menu()
    name = input() + ".csv"
    print(f"the name of the file will be : {name}\n")
    return name


def define_headers():
    headers = {}

    print("\nWhat fields should your tasks present ?")
    print("Press 'Enter' to confirm each entry")
    print(
        "\nNote that some functional fields will be added by the program. These fields are :"
    )
    print("'Task_ID' - holds a unique ID for each line in the table")
    print("'Nesting' - records the sub-level each task is located at")
    print("'Parent_ID' - hold the unique ID of the parent task")
    print(
        "'Progress' - holds the percentage of progress for each task. This is set manually for or calculated automatically if sub-tasks are linked"
    )
    print("\nEnter 'Done' to end this phase.")

    i = 0
    choice = 0

    while True:
        choice = input()
        if choice.lower() == "done":
            break
        else:
            headers[i] = choice
            i += 1

    print("the column headers you defined are :")
    i = 0
    for i in range(0, len(headers)):
        print(f"Header {i + 1} is {headers[i]}")
    print("Please confirm (y/n) ?")

    validation = input()

    match validation:
        case "y":
            headers[i + 1] = "Task_ID"
            headers[i + 2] = "Nesting"
            headers[i + 3] = "Parent_ID"
            headers[i + 4] = "Progress"
            return list(headers.values())
        case "n":
            headers = {}
            define_headers()
        case _:
            print("Please enter y, Y, n or N")


def table_selector():
    # create a function that allows to navigate the computer and select a CSV file
    current_dir = os.getcwd()
    files = os.walk(current_dir)
    filenames = []
    for file in files:
        filenames.append(file)
    correct_files = filenames[0]
    correct_files = correct_files[2]
    filenames = []
    for file in correct_files:
        if file.endswith(".csv"):
            filenames.append(file)
    print("\nAvailable CSV files are :")
    for file in filenames:
        print(file)
    print("\nPlease select a table to load")
    table_choice = input()
    return table_choice


# present user with options on table management
def open_table(table_name):
    table_open_menu()
    choice = input()

    match choice:
        case "1":
            task_menu(table_name)
            choice = input()
            return choice
        case "2":
            print("delete table")
        case "3":
            pass


class Table:
    def __init__(self, table_name, headers):
        self.table_name = table_name
        self.headers = headers
        with open(self.table_name, mode="w", newline="") as file:
            writer = csv.writer(
                file
            )  # generating the csv file which will host the table
            writer.writerow(self.headers)
