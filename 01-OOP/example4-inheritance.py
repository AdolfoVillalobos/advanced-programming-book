class GroceryList(list):

    def discard(self, price):

        for product in self:
            if product.price > price:
                self.remove(product)

        return self

    def __str__(self):
        out = "Grocery List : \n\n"

        for p in self:
            out += "name: "+p.name+"-price: "+str(p.price)+"\n"
        return out

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":

    grocery_list = GroceryList()

    grocery_list.extend([Product("bread", 5), Product("milk", 10), Product("rice", 12)])

    print(grocery_list)

    grocery_list.discard(11)

    print(grocery_list)

