from n_tree import Tree

class TreePreOrder(Tree):

    def __repr__(self):

        def traverse_tree(root):

            ret = ""

            # Visit root node

            ret += "node_id: {}, parent_id: {} -> value: {} \n".format(root.node_id, root.parent_id, root.value)

            for child in root.children.values():
                ret += traverse_tree(child)

            return ret

        return traverse_tree(self)

if __name__ == "__main__":

    T = TreePreOrder(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 4, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)

    print(T)
