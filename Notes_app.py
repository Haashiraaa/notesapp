import datetime
import json
users = {}
users_file = "users.json"

def load():
    global users
    try:
        with open(users_file, "r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        users = {}

def save():
    try:
        with open(users_file, "w") as f:
            json.dump(users, f, indent=4)
        print("Note saved successfully.")
    except Exception as e:
        print(f"Error saving note: {e}")
def load():
    pass








def add():
    note = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info = [timestamp, note]
    save() 
    pass

def view():
    pass

def delete():

    pass

def main_block():
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

def main():
    print("""Welcome to the Notes App!
          Please register or login to continue.""")
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        ans = input("Please choose an option to continue: ")
        if ans == "1":
            main_block()
        elif ans == "2":
            main_block()
        elif ans == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            continue

    
        
if __name__ == "__main__":
    main()
