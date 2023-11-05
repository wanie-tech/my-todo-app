import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    #print(todo)
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader('This is my todo app.')
st.write("This app is to increase your productivity.")

#st.checkbox("Buy grocery")
#st.checkbox("Throw the trash")

#for todo in todos:
    ##st.checkbox(todo)
    #checkbox = st.checkbox(todo, key=todo)
    #if checkbox:
        #print(checkbox)

for index, todo in enumerate(todos):
    #st.checkbox(todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label="", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')

#print("Hello")

#st.session_state #ni mcm print cond true false