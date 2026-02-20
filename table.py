import csv


def define_headers():
    headers = {}

    print("What fields should your tasks present ?")

    i = 0
    choice = 0

    while choice != "q":
        choice = input()
        headers[i] = choice

    print("the column headers you defined are :")
    i = 0
    for i in range(0, len(headers)):
        print(headers[i])
    print("is it ok (y/n) ?")

    validation = input()

    if validation == "y":
        return Table(headers)
    else:
        pass


class Table:
    def __init__(self, headers):
        pass
