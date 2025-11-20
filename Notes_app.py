<<<<<<< HEAD
import datetime
import json
notes = {}
def save(timestamp, note):
    with open("notes.txt", "a+") as f:
        f.write(f"{timestamp} - {note}\n")



def main():
    print("""Welcome to the Notes App!""")
    print("1. Add a note")
    print("2. View notes")
    print("3. Delete a note")
    ans = input("Please coose an option to continue: ")
    if ans == "1":
        add()
    elif ans == "2":
        view()
    elif ans == "3":
        delete()
  




def add():
    note = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save(timestamp, note) 
    pass

def view():
    pass

def delete():

    pass


if __name__ == "__main__":
    main()
=======
import datetime
def save(timestamp, note):
    with open("notes.txt", "a+") as f:
        f.write(f"{timestamp} - {note}\n")


def main():
    print("""Welcome to the Notes App!""")
    print("1. Add a note")
    print("2. View notes")
    print("3. Delete a note")
    ans = input("Please coose an option to continue:\n")

    if ans == "1":
        add()
    elif ans == "2":
        view()
    elif ans == "3":
        delete()
    pass




def add():
    note = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save(timestamp, note) 
    pass

def view():
    pass

def delete():
    pass


if __name__ == "__main__":

    main()
>>>>>>> bfeb9f1109a590d897e98e29328ab52d35dc8452
