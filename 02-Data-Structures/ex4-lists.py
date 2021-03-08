le = []
le.append((2015, 3,14))
le.append((2015, 4, 18))

print(le)


l = [1, "string", 20.5, (23,45)]
print(l)


print(l[1])


songs = ["adicted to pain", "ghost love score", "as i am"]
print(songs)

# Extend a list

new_songs = ["Elevate", "Shine"]
songs.extend(new_songs)

print(songs)

# Insert on index

songs.insert(1, "Sober")
print(songs)


# Slicing Notation

numbers = [1, 3, 4,54, 1,3, 2,25, 20]
print(numbers[2:6]) # 2nd to 6th non inclusive
print(numbers[2::]) # 2nd to last
print(numbers[:5]) # Until 5th element
print(numbers[:5:2]) #Until 5th element by 2
print(numbers[::-1]) # Reverse



## Sorting

a = numbers.sort()
print(numbers, a)

numbers.sort(reverse=True)
print(numbers)


class Piece:

    pid = 0

    def __init__(self, piece):
        Piece.pid += 1
        self.pid = Piece.pid
        self.type = piece

pieces = []

pieces.append(Piece("Bishop"))
pieces.append(Piece("Pawn"))
pieces.append(Piece("King"))
pieces.append(Piece("Queen"))

for piece in pieces:
    print(f"pid: {piece.pid} - types of piece: {piece.type}")
