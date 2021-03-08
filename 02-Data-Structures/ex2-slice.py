if __name__ == "__main__":

    data = (400, 20, 1, 4, 10, 11, 12, 500)

    a = data[1:3]
    print(f"1: {a}")

    a = data[3:]
    print(f"2: {a}")

    a = data[:5]
    print(f"3: {a}")

    a = data[2::2]
    print(f"4: {a}")

    a = data[::-1]
    print(f"5: {a}")

