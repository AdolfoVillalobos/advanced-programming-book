class Email:

    def __init__(self, address):
        self._email = address

    def _set_email(self, value):
        if "@" in value:
            self._email = value
        else:
            print("Invalid Email!")

    def _get_email(self):
        return self._email

    def _del_email(self):
        print("Erase the email attribute!")
        del self._email

    email = property(fget=_get_email, fset=_set_email, fdel=_del_email, doc="This property contains the email.")


if __name__ == "__main__":

    m1 = Email("amvillalobos@uc.cl")
    print(m1.email)

    m1.email = "a2@othermail.com"
    print(m1.email)

    m1.email = "123"
    print(m1.email)

    del m1.email
