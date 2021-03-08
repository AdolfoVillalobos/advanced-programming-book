def compute_geometry(a,b):
    area = a*b
    perimeter = (2*a)+(2*b)
    mpa = a/2
    mpb = b/2
    
    return (area, perimeter, mpa, mpb)

if __name__ == "__main__":

    data = compute_geometry(20.0, 10.0)
    print("1: {0}".format(data))

    a = data[0]

    print(f"2: {a}")

    a, p, mpa, mpb = data

    print(f"3: {a}, {p}, {mpa}, {mpb}")


    a, p, mpa, mpb = compute_geometry(20.0, 10.0)
    print(f"4: {a}, {p}, {mpa}, {mpb}")
