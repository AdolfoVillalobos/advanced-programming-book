

class Apartment:

    def __init__(self, _id, mts2, value):

        self._id = _id
        self.mts2 = mts2
        self.value = value
        self.sold = False


    def sell(self):

        if not self.sold:
            self.sold =True

        else:
            print("Apartment {} was sold".format(self._id))


if __name__ == "__main__":

    d1 = Apartment(_id=1, mts2=100, value=5000)

    print("sold?", d1.sold)

    d1.sell()

    print("sold?", d1.sold)

    d1.sell()
