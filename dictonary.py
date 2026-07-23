note_id = 1

def add_note(notes, note_id):
    text = input("write your note: ")
    notes[note_id] = text
    print("note saved")
    return note_id + 1      

def show_notes(notes):
    for key in notes:
            print(f"{key}:{notes[key]}")

def delete_notes(notes):
    try:
        number = int(input("enter the node number:"))
        notes.pop(number)
        print("note deleted")

    except(ValueError,KeyError):
        print("notes do not match or not exist")

def save_notes(notes):
     with open("notes.txt", "w") as file:
          for key in notes:
               file.write(f"{key} | {notes[key]}\n")

def load_notes():
    notes = {}
    try:
        with open("notes.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                key = int(parts[0])
                text = parts[1].strip()
                notes[key] = text
    except FileNotFoundError:
        pass
    return notes

notes = load_notes()

while True:
    print("\n1. Add note    2. show note    3.Delete note  4.quit")
    choice = input("pick an option:")

    if choice == "1":
         note_id = add_note(notes, note_id)
         save_notes(notes)
    elif choice == "2":
         show_notes(notes)
    elif choice == "3":
         delete_notes(notes)
    elif choice == "4":
        print("bye bye")
        break
    else:
        print("enter a valid opotion")


