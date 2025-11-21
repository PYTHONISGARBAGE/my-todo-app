import streamlit as st
import functions
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("my todo app")
st.subheader("this is todo app")
st.write("this app is to increas your productivity")
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(index)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add to do", placeholder="add todo...",
              on_change=add_todo, key="new_todo")