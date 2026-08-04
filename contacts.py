import json

try:
    with open("contacts.json" , "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

while True:
    print("\n1. Add  2. Look up  3. View  4. Exit")
    choice = input("pick an option: ")
    if choice == "1":
        name = input("enter the name: ")
        phone = input("enter the number: ")
        contacts[name] = phone
        print("added")
        with open("contacts.json", "w") as file:
            json.dump(contacts,file)

    elif choice == "2":
        name = input("enter the name to look: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("contact not found")

    elif choice == "3":
        for name in contacts:
            print(f"{name}: {contacts[name]}")

    elif choice == "4":
        print("bye!")
        break
    else:
        print("not a valid option")
