
from collections import deque
from package import Package
from bottle import Bottle


class Machine:
    def process(self, incoming_production_line):
        print("-"*20)
        print(f"Machine {self.__class__.__name__} started working")

class BottleModulator(Machine):

    def __init__(self):
        self.bottles_to_produce = 0

    def process(self, incoming_production_line=None):
        super().process(incoming_production_line)

        Q = deque()

        for i in range(self.bottles_to_produce):
            b = Bottle()
            if (i%5 == 1) & (i >1):
                b.liters = 3
            if (i%6 == 1) & (i> 1):
                print(i)
                b.liters = Q[-1].liters*0.5+4*Q[-2].liters
            Q.append(b)

        return Q

class LowFAT32(Machine):
    def __init__(self):
        self.discarded_bottles = []

    def discard_bottle(self, bottle):
        self.discarded_bottles.append(bottle)

    def print_discarded_bottles(self):
        print("{} bottles were discarded".format(len(self.discarded_bottles)))

    def process(self, incoming_production_line):
        super().process(incoming_production_line)
        D = deque()
        while incoming_production_line:
            p = incoming_production_line.popleft()
            if len(D)==0:
                D.append(p)
            else:
                if p.liters >= D[-1].liters:
                    D.append(p)
                elif p.liters <= D[0].liters:
                    D.appendleft(p)
                else:
                    self.discard_bottle(p)

        self.print_discarded_bottles()
        return D

class HashSoda9001(Machine):

    def process(self, incoming_production_line=None):
        super().process(incoming_production_line)
        stacks = {}
        for b in incoming_production_line:
            if b.liters not in stacks.keys():
                stacks[b.liters] = []
            stacks[b.liters].append(b)
        return stacks

class PackageManager(Machine):

    def process(self, incoming_production_line):
        super().process(incoming_production_line)
        packages = deque()
        for stack in incoming_production_line.values():
            package = Package()
            package.add_bottles(stack)
            packages.append(package)
        return packages

class Factory:

    def __init__(self):

        self.bottlemodulator = BottleModulator()
        self.lowFAT32 = LowFAT32()
        self.hashSoda9001 = HashSoda9001()
        self.packageManager = PackageManager()

    def production(self, num_bottles):

        self.bottlemodulator.bottles_to_produce = num_bottles
        product = None
        for machine in [self.bottlemodulator, self.lowFAT32, self.hashSoda9001, self.packageManager]:
            product = machine.process(product)
        return product


if __name__ == "__main__":

    num_bottles = 10
    factory = Factory()
    output = factory.production(num_bottles)
    print("-"*20)
    print(f"{num_bottles} bottles produced { len(output) } packages")

    for package in output:
        package.see_content()
    print("-"*20)