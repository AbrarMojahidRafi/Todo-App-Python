import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

while True:

    userCommand = input("Type add, show, edit, complete or exit :) ")
    userCommand = userCommand.strip(" ")

    if userCommand.lower() == "add":
        # print("adding the item")
        askTheItem = input("Write your to-do.. ")

        todos = functions.openingTheTodos("todos.txt")

        todos.append(askTheItem + "\n")

        functions.writingInTheTodos("todos.txt", todos)

    elif userCommand.lower() == "show":
        # print("show the all items")

        todos = functions.openingTheTodos("todos.txt")

        for i in range(len(todos)):
            print(f"{i + 1} - {todos[i][0:len(todos[i]) - 1]}")

    elif userCommand.lower() == "edit":
        # print("ask which item you want to edit?")
        itemNumber = int(input("Enter the int number which you want to edit: "))

        # print("And then edit it")
        todos = functions.openingTheTodos("todos.txt")

        if 0 <= itemNumber - 1 < len(todos):
            editText = input("Enter your text: ")

            todos[itemNumber - 1] = editText + "\n"

            functions.writingInTheTodos("todos.txt", todos)
        else:
            print("Please enter a valid item number :)")

    elif userCommand.lower() == "complete":
        # print("means remove that item from the list")
        askNumber = int(input("Write the int number which is completed: "))

        todos = functions.openingTheTodos("todos.txt")

        if 0 <= askNumber - 1 < len(todos):
            todos.pop(askNumber - 1)

            functions.writingInTheTodos("todos.txt", todos)
        else:
            print("Please enter a valid item number :)")

    elif userCommand.lower() == "exit":
        print("close the application")
        break

    else:
        print("Please give the correct command..!!!")

