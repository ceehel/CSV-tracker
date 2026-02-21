import csv


def define_name():
    print("Please enter the name of the table you want to create")
    name = input() + ".csv"
    print(f"the name of the file will be : {name}\n")
    return name


def define_headers():
    headers = {}

    print("What fields should your tasks present ?")
    print("Press 'Enter' to confirm each entry")
    print("Enter 'q' when you are done.")

    i = 0
    choice = 0

    while True:
        choice = input()
        if choice == "q":
            break
        else:
            headers[i] = choice
            i += 1

    print("the column headers you defined are :")
    i = 0
    for i in range(0, len(headers)):
        print(f"Header {i + 1} is {headers[i]}")
    print("is it ok (y/n) ?")

    validation = input()

    if validation == "y":
        headers[i + 1] = "task_ID"
        headers[i + 2] = "nesting"
        headers[i + 3] = "parent_ID"
        return list(headers.values())
    else:
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
