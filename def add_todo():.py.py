def add_todo():
    task = input("what you need to do?")
    with open("todos.txt", "a") as file:
        file.write(task+"\n")
        print("todo added")
def show_todo():
    try:
        with open("todo.txt", "r") as file:
            for line in file:
                print(line.strip)
    except FileNotFoundError:
        print("no todos")

while True:
    print("\n1. Add 2.show 3.quit")
    choice = input("pick an option")

    if choice == "1":
        add_todo()
    if choice == "2":
        show_todo()
    if choice == "3":
        print("bye")