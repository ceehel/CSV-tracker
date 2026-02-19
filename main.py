import pandas

# The intent is to process CSV files in a systematic fashion which is expected to bring a capacity to display
# from a single file, a list of elements, their caracteristics and, above the rest, allow for a relationship
# to be visible and actionnable from the interface
# Also, while the data behind the program should allow to relate a line to another, there needs to be a special
# attention to how this relationship is, both, structured in the file, and depicted on screen. A unique ID on each
# task seems advisable.

# functionalities :
# - create a blank file
# - add a column
# - remove a column
# - move a column
# - make a column mandatory
# - display, or not, empty columns
# - add a task
# - update a task (link to another, make independent, etc)
# - delete a task

df = pandas.read_csv("/home/cyril/Documents/CSV_link/test_file.csv", header=1)

print(df)
