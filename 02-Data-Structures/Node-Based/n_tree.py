class Tree:

    def __init__(self, node_id, value=None, parent_id=None):

        self.node_id = node_id
        self.parent_id = parent_id
        self.value = value
        self.children = {}

    def add_node(self, node_id, value=None, parent_id=None):

        if self.node_id == parent_id:
            self.children.update({node_id: Tree(node_id, value, parent_id)})
        else:
            # if the node is not the parent, we search recursively:

            for child in self.children.values():
                child.add_node(node_id, value, parent_id)
    def get_node(self, node_id):
        if self.node_id == node_id:
            return self

        else:
            for child in self.children.values():
                node = child.get_node(node_id)
                if node:
                    return node

    def __repr__(self):
        def traverse_tree(root):
            ret = ""
            for child in root.children.values():
                ret += f"id-node: {child.node_id} -> parent_id: {child.parent_id} -> value: {child.value}\n"
                ret += traverse_tree(child)
            return ret

        ret = f"root:\nroot-id: {self.node_id} -> value: {self.value}\n"
        ret += traverse_tree(self)

        return ret

if __name__ == "__main__":

    T = Tree(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 9, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)

    print(T)


    # get_node method

    node = T.get_node(6)
    print("The id of the node is {}".format(node))


    node = T.get_node(1)
    print("The node has {} children".format(len(node.children)))

