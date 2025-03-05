class ContactBook:  
    def __init__(self):
        self.contacts = {}

    def add_contact(self, email, name, phone):
        self.contacts[email] = {"Name": name, "Phone": phone}
        print(f"Contact '{email}' added successfully")

    def search_contact(self, email):
        if email in self.contacts:
            print(f"Email: {email}, Name: {self.contacts[email]['Name']}, Phone: {self.contacts[email]['Phone']}")
        else:
            print("Not found.")

book = ContactBook()  

while True:
    print("Options: add, search, update, delete, show, exit")
    choice = input("Enter a command: ").strip().lower()

    if choice == "add":
        email = input("Enter Email: ")
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        book.add_contact(email, name, phone)

    elif choice == "search":  
        email = input("Enter Email to search: ")
        book.search_contact(email)
