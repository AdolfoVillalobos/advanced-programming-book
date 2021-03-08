from collections import namedtuple

Register = namedtuple("Register", "ID_NUMBER name age")
c1 = Register("123454-6", "Christian", 20)
c2 = Register("12323212-5", "Adolfo", 5)

print(c1.ID_NUMBER)
print(c2.ID_NUMBER)


def compute_geometry(a,b):

    Features = namedtuple("Geometrical", "area perimeter mpa mpb")
    area = a*b
    perimeter = 2*(a+b)
    mpa = a/2
    mpb = b/2
    return Features(area, perimeter, mpa, mpb)

data = compute_geometry(20.0, 10.0)
print(data.area)

