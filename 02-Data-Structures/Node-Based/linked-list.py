class Node:

    def __init__(self, value=None):
        self.next = None
        self.value = value

class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None

    def add_node(self, value):

        if not self.head:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def __repr__(self):
        rep = ""
        current_node = self.head

        while current_node:
            rep += f"{current_node.value}"
            current_node = current_node.next
            if current_node:
                rep += " -> "

        return rep


if __name__ == "__main__":

    l = LinkedList()
    l.add_node(2)
    l.add_node(4)
    l.add_node(7)
    l.add_node(8)

    print(l)
