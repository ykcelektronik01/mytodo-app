import streamlit as st
import  functions

todos=functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("TODO APP")
st.subheader("This is TODO app")
st.text("This app is creating for improving my pyhton skils")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="",placeholder="Enter a todo...",on_change=add_todo,key='new_todo')


#print(st.session_state) Dictionary donduruyor.