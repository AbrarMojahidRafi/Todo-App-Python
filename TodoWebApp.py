import streamlit as st
import functions

st.title("My Todo App")
st.subheader("Hello! Insha'allah it will be a great todo web app for you!")
st.write("Your todos are: ")
# getting todos from the text file and making a checkbox each one of them
todos = functions.openingTheTodos("todos.txt")
for i in todos:
    st.checkbox(f"{i[:-1]}")
st.text_input("", placeholder="Enter new todo", key="TextBox")
newTodo = st.session_state["TextBox"]


def append_new_todo(new_todo):
    todos.append(f"{new_todo}\n")
    functions.writingInTheTodos("todos.txt", todos)
    st.checkbox(f"{new_todo}")


try:
    append_new_todo(newTodo)
except:
    pass
# st.write(f"{todos}")
