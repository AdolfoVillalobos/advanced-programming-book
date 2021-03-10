class Package:
    packages_id = 0
    def __init__(self):
        Package.packages_id += 1
        self.id = Package.packages_id
        self.bottles = []

    def add_bottle(self, bottle):
        self.bottles.append(bottle)

    def add_bottles(self, bottles):
        self.bottles.extend(bottles)
    
    def see_content(self):
        print("-"*20)
        print("Package ID : # {} \n".format(self.id))
        for b in self.bottles:
            print(b)