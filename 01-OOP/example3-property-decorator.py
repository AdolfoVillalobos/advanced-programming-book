
# Encapsulation using property()
class Color:

    def __init__(self, rgb_code, name):
        self.rgb_code = rgb_code
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


    name = property(get_name, set_name)


# Encapsulation using @property decorator

class Color2:

    def __init__(self, rgb_code, name):
        self._rgb_code = rgb_code
        self._name = name

    @property
    def name(self):
        print("Getter")
        return self._name

    @name.setter
    def name(self, new_name):
        print("Setter")
        self._name = new_name

    @name.deleter
    def name(self):
        print("Erase the name!")
        del self._name



if __name__ == "__main__":

    c = Color2("#fff", "white")

    print(c.name)


    c.name = "black"
    print(c.name)
    
    print(c._name)

    del c.name




