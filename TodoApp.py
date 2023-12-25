import PySimpleGUI as gui
import functions
import os

gui.theme("DarkGreen5")

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

typeInAToDo = gui.Text("Type in a To-do: ")
addButton = gui.Button("Add")
inputBox = gui.Input(key="inputBox")
listBox = gui.Listbox(values=functions.openingTheTodos("todos.txt"), size=(48, 10), key="listBox")
editButton = gui.Button("Edit")
completeButton = gui.Button("Complete")
commentBox = gui.Text("If you can dream about it, you can obviously able to do it.")

window = gui.Window("My To-Do App",
                    layout=[
                        [typeInAToDo, inputBox, addButton],

                        [listBox, editButton, completeButton]
                    ]
                    )

while True:

    event = window.Read()  # event = ('Add', {'inputBox': 'rafi'})

    clickEvent, dictionary = event
    # print(clickEvent, dictionary)

    match clickEvent:

        case "Add":
            to_do_from_inputBox = dictionary["inputBox"]
            if to_do_from_inputBox != "":
                if functions.check_already_in_the_todos_list_or_not("todos.txt", to_do_from_inputBox + "\n"):
                    # opening the todos.txt file
                    todos = functions.openingTheTodos("todos.txt")
                    # appending the new todo in the todos.txt file list
                    todos.append(to_do_from_inputBox + "\n")
                    # updateing the todos.txt file
                    functions.writingInTheTodos("todos.txt", todos)
                    # for seeing realtime update
                    window["listBox"].update(values=todos)
                    # Notifying what you're done
                    gui.popup_ok(f'"{to_do_from_inputBox}" added SUCCESSFULLY', title="Add", auto_close_duration=10,
                                 auto_close=True)
                else:
                    gui.popup_ok('This task already in the todos list. \nSo please type another task!', title="Add",
                                 auto_close_duration=7, auto_close=True)
            else:
                s = "-----------------------------------------------------"
                gui.popup_ok(f'{s}\nPlease type something..!!\n{s}', title="Add", auto_close_duration=5,
                             auto_close=True)

        case "Edit":
            if len(dictionary["listBox"]) == 0:
                s = "-----------------------------------------------------"
                gui.popup_ok(f'{s}\nPlease select one to-do!\n{s}', title="Edit", auto_close_duration=5,
                             auto_close=True)
            else:
                if len(dictionary["inputBox"]) == 0:
                    s = "-----------------------------------------------------"
                    gui.popup_ok(f'{s}\nPlease enter new to-do!\n{s}', title="Edit", auto_close_duration=5,
                                 auto_close=True)
                else:
                    if functions.check_already_in_the_todos_list_or_not("todos.txt", dictionary["inputBox"] + "\n"):
                        # store the new input value
                        to_do_from_inputBox = dictionary["inputBox"]
                        # store the selected value for edit
                        selectedValueFromListBox = dictionary["listBox"][0]
                        # opening the todos.txt file
                        todos = functions.openingTheTodos("todos.txt")
                        # updating the new input value with the "selected value for edit"
                        for index in range(len(todos)):
                            if todos[index] == selectedValueFromListBox:
                                todos[index] = to_do_from_inputBox + "\n"
                                break
                        # appending the edited todo in the todos.txt file list
                        functions.writingInTheTodos("todos.txt", todos)
                        # for seeing realtime update
                        window["listBox"].update(values=todos)
                        # Notifying what you're done
                        gui.popup_ok(
                            f'You successfully edit your to-do!\nFrom"{selectedValueFromListBox[:-1]}" to "{to_do_from_inputBox}"',
                            title="Edit", auto_close_duration=10, auto_close=True)
                    else:
                        gui.popup_ok('This task already in the todos list. \nSo please type another task!',
                                     title="Edit", auto_close_duration=10, auto_close=True)

        case "Complete":
            if len(dictionary["listBox"]) == 0:
                s = "-----------------------------------------------------"
                gui.popup_ok(f'{s}\nPlease select one to-do!\n{s}', title="Complete", auto_close_duration=5,
                             auto_close=True)
            else:
                # select the todo that I want to consider as a "Complete" task.
                todoFromListBox = dictionary["listBox"][0]
                # opening the todos.txt file
                todos = functions.openingTheTodos("todos.txt")
                # iterate through the todos, and remove it from the todos
                position = 0
                while (position < len(todos)):
                    s = todos[position]
                    if s == todoFromListBox:
                        todos.pop(position)
                        break
                    position += 1
                # updating the new list
                functions.writingInTheTodos("todos.txt", todos)
                # for seeing realtime update
                window["listBox"].update(values=todos)
                # Notifying what you're done
                gui.popup_ok(f'You successfully completed "{todoFromListBox[:-1]}"', title="Complete",
                             auto_close_duration=5, auto_close=True)

        case gui.WIN_CLOSED:  # gui.WIN_CLOSED = None
            # print(f"{gui.WIN_CLOSED}")
            break

window.close()
