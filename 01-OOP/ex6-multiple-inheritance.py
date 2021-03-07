## In multiple Inheritance, arguments can be passed using **kwg

class AddressHolder:

    def __init__(self, street, number, city, state, **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.number = number 
        self.city = city
        self.state = state


class Contact:

    contact_list = []

    def __init__(self, name, email, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email

        Contact.contact_list.append(self)

class Customer(Contact, AddressHolder):

    def __init__(self, phone_number, **kwargs):
        super().__init__(**kwargs)
        self.phone_number = phone_number

if __name__ == "__main__":
    c = Customer(name="John Davis", email="adolfo@vill.com",
            phone_number="2345678", street="Beacon Street",
            number="231", city="Cambridge", state="Massachussets")

    print(f"name: {c.name} \nemail: {c.email}\naddress: {c.street}, {c.state}")

