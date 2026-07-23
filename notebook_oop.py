import json
class Notebook:
    def __init__(self):
        self.notes = {}
        self.notes_id = 1
        
        

    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes,file)

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = {}

    def add_notes(self):
        text = input("write your note:")
        self.notes[self.notes_id]= text
        self.notes_id = self.notes_id + 1
        print("notes saved")
        self.save_notes()

    def show_notes(self):
        for key in self.notes:
            print(f"{key}: {self.notes[key]}")

    def delete_notes(self):
        try:
            number = int(input("enter the note to delete:"))
            self.notes.pop(number)
            print("note deleted:")
            self.save_notes()
        except (ValueError, KeyError):
            print("note doesnt exist")

my_notebook = Notebook()
while True:
    print("\n1.Add_note  2.Show_note  3.Delete_note. 4.quit")
    choice = input("pick an option")
    if choice == "1":
        my_notebook.add_notes()
    elif choice == "2":
        my_notebook.show_notes()
    elif choice == "3":
        my_notebook.delete_notes()
    elif choice == "4":
        print("bye")
        break
    else:
        print("bye not a valid option")