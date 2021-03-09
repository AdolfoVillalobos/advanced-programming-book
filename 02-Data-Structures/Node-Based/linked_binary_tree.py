class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"parent: {self.parent}, value: {self.value}"


class BinaryTree:

    def __init__(self, root_node=None):
        self.root_node = root_node

    def add_node(self, value):
        if self.root_node is None:
            self.root_node = Node(value)
        else:
            temp = self.root_node
            added = False

            while not added:
                if value <= temp.value:
                    if temp.left_child is None:
                        temp.left_child = Node(value, temp.value)
                        added = True
                    else:
                        temp = temp.left_child
                else:
                    if temp.right_child is None:
                        temp.right_child = Node(value, temp.value)
                        added = True
                    else:
                        temp = temp.right_child


    def __repr__(self):
        def traverse_tree(node, side="root"):
            ret = ""

            if node is not None:
                ret += f"{node} ->{side}\n"
                ret += traverse_tree(node.left_child, "left")
                ret += traverse_tree(node.right_child, "right")

            return ret
        return traverse_tree(self.root_node)

# Traversal Algorithms:
#   1): Pre-Order traversal: Visit the Root and then its children recursrivelly
#   2): In-Order traversal:
#   3): Post-Order traversal:





if __name__ == "__main__":

    T = BinaryTree()

    T.add_node(5)
    T.add_node(2)
    T.add_node(3)
    T.add_node(20)
    T.add_node(15)

    print(T)

