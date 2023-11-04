#from functions import get_todos, write_todos

import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # this is a string

    #match user_action:
        #case 'add':
    #if 'add' in user_action or 'new' in user_action:
    #if 'add' not in user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]  #list slicing operation

        #file = open("todos.txt", 'r')
        #todos = file.readlines() #store line in the list
        #file.close()

        #context manager code
        todos = functions.get_todos()
        #todos = get_todos()

        todos.append(todo + '\n')


        #file = open('todos.txt', 'w')
        #file.writelines(todos)
        #file.close()

        #with open ('todos.txt', 'w') as file:
            #file.writelines(todos)

        #write_todos(filepath="todos.txt", todos_arg=todos)
        #write_todos(todos, "todos.txt")
        functions.write_todos(todos) #default parameter

    #case 'show' | 'display':
        #file = open('todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

    #elif 'show' in user_action:
    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    #case 'edit':
    #elif 'edit' in user_action:
    elif user_action.startswith('edit'):
        try:
            #number = int(input("number todo to edit: "))
            #number = number - 1

            number = int(user_action[5:])
            print(number)
            number = number - 1

            #print("bye")

            todos = functions.get_todos()
            #print('here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            #print('here is how it will be', todos)

            #write_todos("todos.txt", todos)
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    #case 'complete':
    #elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        try:
            #number = int(input("number todo to complete: "))
            number = int(user_action[9:])

            #get current list
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            #write back to the file
            #write_todos("todos.txt", todos)
            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    #case 'exit':
    elif user_action.startswith('exit'):
        break

    else:
        print("command is not valid")

print("BYE!")

        #case whatever:
            #print("hey, u entered an unknown command")
