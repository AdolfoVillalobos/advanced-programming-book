# The traverse is level by level, hierarchichally.

from n_tree import Tree
from collections import deque

class TreeBFS(Tree):

    def __repr__(self):

        def traverse_tree(root):

            ret = ""
            Q = deque()
            Q.append(root)

            visited = []
            
            while len(Q) > 0:
                p = Q.popleft()

                if p.node_id not in visited:
                    visited.append(p.node_id)

                    ret += "node_id: {}, parent_id: {} -> value :{}\n".format(p.node_id, p.parent_id, p.value)
                    for child in p.children.values():
                        Q.append(child)

            return ret
        return traverse_tree(self)

if __name__ == '__main__':
    # We add items to the tree
    T = TreeBFS(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 4, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)
    print(T)
