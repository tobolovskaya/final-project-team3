class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contacts(self, search_term):
        matching_contacts = [
            contact
            for contact in self.contacts
            if search_term.lower() in contact.name.lower()
        ]
        return matching_contacts

    def display_contacts(self, contacts):
        for contact in contacts:
            print(contact)


def main():
    my_contacts = ContactBook()

    my_contacts.add_contact(Contact("name, phone, email"))

    search_query = input("name: ")
    matching_contacts = my_contacts.search_contacts(search_query)

    if matching_contacts:
        print("Contacts found:")
        my_contacts.display_contacts(matching_contacts)
    else:
        print("Contacts not found.")


if __name__ == "__main__":
    main()
