from linked_binary_tree import BinaryTree, Node


class BinaryTreePreOrderTraversal(BinaryTree):

    def __repr__(self):
        def traverse_tree(node, side="root"):
            ret = ""
            if node is not None:
                ret += f"{node} -> {side}\n"
                ret += traverse_tree(node.left_child, "left") 
                ret += traverse_tree(node.right_child, "right") 
            return ret
        return traverse_tree(self.root_node)


if __name__ == "__main__":

    T = BinaryTreePreOrderTraversal()
    T.add_node(4)
    T.add_node(1)
    T.add_node(5)
    T.add_node(3)
    T.add_node(20)

    print(T)
