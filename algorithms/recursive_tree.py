class Tree:
    """A recursive implementation of a simple tree data structure.
    Instead of a class for a Node AND a class for the Tree.
    They will be combined into one class. Nodes can be represented as
    subtrees.

    root is the root node of the tree/subtree. It will only contain a
    value.

    subtrees is a list of all subtrees of this tree.

    General recursive traversal template for Tree:
    def foo(self):
        if self.is_empty(): <- base case.
            ...
        else:
            ...
            for subtree in self.subtrees: <- recursive case.
                subtree.foo()
            ...
    """

    def __init__(self, root, subtrees=[]):
        """Initialize a new tree.

        Precondition: if root is None, thn there are no subtrees
        """
        self.root = root
        self.subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.
        """
        return self.root is None

    def __len__(self) -> int:
        """Return the the total number of items in this tree.
        """
        if self.is_empty():
            return 0
        else:
            size = 1 # Initialize. Include root.
            for subtree in self.subtrees:
                size += len(subtree)
            return size

    def __str__(self) -> str:
        if self.is_empty():
            return None
        else:
            s = f'{self.root}\n'
            for subtree in self.subtrees:
                s += str(subtree)
            return s

    def str_indented(self, depth=0) -> str:
        if self.is_empty():
            return None
        else:
            s = ' ' * depth + f'{self.root}\n'
            for subtree in self.subtrees:
                s += subtree.str_indented(depth + 1)
            return s

    def __contains__(self, value) -> bool:
        """Return True if the value is in the tree, and
        False otherwise.
        """
        if self.root == value:
            return True
        else:
            result = False
            for subtree in self.subtrees:
                if result == False:
                    result = value in subtree
        return result

    def delete_item(self, item) -> bool:
        """Delete the first occurrence of item in the tree.
        If the item has subtrees, those will also be deleted.
        """
        if self.is_empty(): # Empty case.
            return False
        elif self.root == item:
            return True
        else:
            for subtree in self.subtrees:
                deleted = subtree.delete_item(item)
                if deleted:
                    self.subtrees.remove(subtree)
            return False

def main():
    t1 = Tree(None, [])
    # 0
    print(f'Size of t1: {len(t1)}')
    t2 = Tree(5, [Tree(8), Tree(11), Tree(12, [Tree(4)]), Tree(24)])
    print(f't2:\n{t2}')
    print(f't2 indented:\n{t2.str_indented()}')
    print(4 in t2)
    # 5.
    print(f'Size of t2: {len(t2)}')
    t3 = Tree(5)
    # 1
    print(f'Size of t3: {len(t3)}\n')
    t2.delete_item(12)
    print(f't2 with 12 removed:\n{t2.str_indented()}')

if __name__ == '__main__':
    main()
