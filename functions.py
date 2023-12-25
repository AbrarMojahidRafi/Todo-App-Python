def openingTheTodos(fileName):
    """will return a list which contains all the todos."""
    with open(fileName, "r") as forReadingTheFile:
        return forReadingTheFile.readlines()


def writingInTheTodos(fileName, todos):
    with open(fileName, "w") as forWritingInTheFile:
        for todo in todos:
            forWritingInTheFile.writelines(todo)


def check_already_in_the_todos_list_or_not(fileName, to_do_from_inputBox):
    todos = openingTheTodos(fileName)
    if to_do_from_inputBox in todos:
        return False
    else:
        return True
