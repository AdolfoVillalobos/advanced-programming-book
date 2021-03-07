# Geometric Shapes

# 1) property: center
# 2) Method: Translate
# 3) Property: Perimeter
# 4) Property: Area
# 5) Method: Grow_area
# 6) Method: grow_perimeter
# 7) Repr or str override
#
# Rectangle: Two properties: length and width
# Equilateral Triangle: property side

from abc import ABCMeta, abstractmethod
from math import pi, cos, sqrt, sin, asin

def calculate_points(center, radius, angles):
    points = []
    for k in angles:
        coords = [radius*cos(k), radius*sin(k)]
        for i in range(len(center)):
            coords[i] += center[i]
        points.append(coords)

    return points


class Figure(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, center):
        self._center = center

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        self._center = value

    @center.deleter
    def center(self):
        del self._center

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def vertices(self):
        pass
    
    def translate(self, vector):
        if len(self.center) == len(vector):
            self.center = tuple(map(lambda x,y: x+y, self.center, vector))
        else:
            print("Wrong vector size")
            return

    @abstractmethod
    def grow_area(self):
        pass

    @abstractmethod
    def grow_perimeter(self):
        pass

    def __repr__(self):
        return f"{type(self).__name__} - Perimeter: {self.perimeter}, Area: {self.area}, Center: {self.center}" 

    @property
    @abstractmethod
    def angles(self):
        pass
    
    @property
    @abstractmethod
    def distance_to_center(self):
        pass

    @property
    def vertices(self):
        return calculate_points(self.center, self.distance_to_center, self.angles)


class Rectangle(Figure):

    def __init__(self, a, b, center):
        super().__init__(center)
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value

    @property
    def perimeter(self):
        return 2*(self._a+self._b)

    @property
    def area(self):
        return self._a*self._b

    def grow_area(self, times):
        self._a *= sqrt(times)
        self._b *= sqrt(times)
    
    def grow_perimeter(self, amount):
        aux = self._a + self._b
        self._a += self._a*amount/(2*aux)
        self._b += self._b*amount/(2*aux)

    @property
    def distance_to_center(self):
        return sqrt(self._a**2+self._b**2)/2
    
    @property
    def angles(self):
        angles  = []

        angles.append(0)
        angles.append(pi)
        angles.append(2*asin(self._b/(2*self.distance_to_center)))
        angles.append(pi+2*asin(self._b/(2*self.distance_to_center)))

        return angles

class EquilateralTriangle(Figure):

    def __init__(self, l, center):
        super().__init__(center)
        self._l = l

    @property
    def l(self):
        return l

    @l.setter
    def l(self, value):
        if value >0 :
            self._l = value

    @property
    def perimeter(self):
        return 3*self._l

    @property
    def area(self):
        return (sqrt(3)*self._l**2)/4

    def grow_area(self, times):
        self._l *= sqrt(times)

    def grow_perimeter(self, amount):
        self._l += amount/3

    @property
    def distance_to_center(self):
        return self._l/sqrt(3)

    @property
    def angles(self):
        angles = []
        angles.append(0)
        angles.append(2*pi/3)
        angles.append(4*pi/3)
        return angles

# Testing the Solution

if __name__ == "__main__":

    figures = list()
    figures.append(EquilateralTriangle(5, [0, 0]))
    figures.append(Rectangle(6, 8, [0, 0]))
    print(*figures, sep="\n")
    print("*" * 20)
                    

    for i in figures:
        i.grow_perimeter(0)

    print(*figures, sep="\n")
    print("*" * 20)
    
    for i in figures:
         i.grow_area(1)

    print(*figures, sep= "\n")
    print("*"*20)



    print("Before translating")
    
    for i in figures:
        print(i.vertices)
    print("*"*20)


    print("After Translating")      

    for i in figures:
        i.translate((2,-1))
        print(i.vertices)
    print("*"*20)


    print(*figures, sep="\n")
    print("*"*20)
