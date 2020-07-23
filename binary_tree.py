import random

class BinaryTree:
    '''A binary tree. The binary tree contains a series
    of nodes where each node can have at most two children.

    values is an (unordered) list of numbers that the nodes
    will contain.

    NOTE: This implementation was done mostly blind. I watched a video on
    the topic and started from there. I only looked at code for method ideas.
    I opted for while loops instead of recursion just because I was more
    comfortable with it.
    '''

    def __init__(self, values):
        if len(values) > 0:
            self.root = Node(values[0])
            for v in values[1:]:
                self.insert(v)
        else:
            self.root = Node()

    def display(self, node='root'):
        '''Display the binary tree with an inorder printing algorithm.

        NOTE: Not gonna lie, I pretty much cheated for this one. I mostly just wanted
        to see if my implementation is correct. According to the video I followed it is.
        (because it always prints in order).
        '''
        if node == 'root':
            node = self.root

        if node.left_child:
            self.display(node.left_child)
        print(node.value)
        if node.right_child:
            self.display(node.right_child)

    def insert(self, value):
        node = self.root
        inserted = False

        while not inserted:
            if value <= node.value:
                # Check if left_child already exits.
                if node.left_child is None:
                    node.left_child = Node(value)
                    inserted = True
                else:
                    node = node.left_child
            else:
                # Check if right_child already exists.
                if node.right_child is None:
                    node.right_child = Node(value)
                    inserted = True
                else:
                    node = node.right_child

    def contains(self, value):
        node = self.root
        found = False

        while not found:
            if node is None or not node.has_children:
                break
            elif node.value == value:
                found = True
            elif node.value > value:
                node = node.left_child
            else:
                node = node.right_child

        return found

class Node():
    '''A single node of a binary tree. For any given node
    with two child nodes, left_child < right_child.
    '''

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def has_children():
        return self.left_child or self.right_child

def main():
    b = BinaryTree([random.randint(1, 20) for x in range(10)])
    b.display()
    print(b.contains(5))

if __name__ == '__main__':
    main()
