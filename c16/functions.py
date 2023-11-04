FILEPATH = "todos.txt"

#def get_todos():
#def get_todos(filepath="todos.txt"):
def get_todos(filepath=FILEPATH):
    """Read a text file and retun the list of
    to do items.
    """
    ##filepath = "todos1.txt" -->ada error argument
    #with open('todos.txt', 'r') as file_local:
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#print(help(get_todos))

#text = """
#principles of productivity
#managing inflow
#"""
#print(text)



#def write_todos(todos_arg, filepath="todos.txt"):
def write_todos(todos_arg, filepath=FILEPATH):
    #filepath = ["1.To"]
    """ write to do item list in text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())