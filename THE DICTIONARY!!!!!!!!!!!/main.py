class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print("Contact added!\n")

    def find_phone_number(self,name):
        if name in self.contacts:
            print(f"{name}'s phone number is: {self.contacts[name]}\n")
        else:
            print("Contact not found in phone book.\n")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} has been delete from the phone book.\n")
        else:
            print("contact not found in phone book.")

    def display_contact(self):
        if not self.contacts:
            print("(empty)\n")
        else:
            for name in self.contacts:
                print(f"{name}: {self.contacts[name]}")
        print()
phonebook = PhoneBook()
program = True

while program:
    print("welcome to Phone Book")
    print()
    print()
    print("1.Add contact")
    print("2.Lookup contact")
    print("3.Delete contact")
    print("4.Display all contacts")
    print("5.Quit")
    print()
    print()
    choice = int(input("Please enter your choice:"))
    if choice == 1:
        name = input("Please enter the name that you want to add")
        phonenumbers = input("Please enter phone number")
        phonebook.add_contact(name, phonenumbers)
    elif choice == 2:
        name = input("Please enter the name that you want to find")
        phonebook.find_phone_number(name)
    elif choice == 3:
        name = input("Please enter the name you want to delete")
        phonebook.delete_contact(name)
    elif choice == 4:
        phonebook.display_contact()
    else:
        program = False