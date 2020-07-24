class Tree:
    """A recursive implementation of a tree data structure.
    Instead of a class for a Node AND a class for the Tree.
    They will be combined into one class. Nodes can be represented as
    subtrees.

    root is the root node of the tree/subtree. It will only contain a
    value.

    subtrees is a list of conected subtrees to the root node.
    """

    def __init__(self, root, subtrees):
        self.root = root
        self.subtrees = subtrees

    def is_empty():
        return self.root is None

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            return
        pass
