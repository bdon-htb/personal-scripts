# The last python_tree implementation was pretty lossy and didn't properly account for content spread out across the file.
from typing import List

class CodeTreeNode:
    """A hierarchical recursive tree structure for python code.
    """
    def __init__(self, code_block: str):
        self.fullname = code_block # line of code (with whitespace) that defines the code block the node represent
        self.name = self._clean_block_name(code_block)
        self.content = [] # A sequential arrangement of the node's content
        self.nodes = {} # Hashmap for quick access to child nodes.

    def _clean_block_name(self, code_block: str) -> str:
        """Returns copy of code_block without whitespace and class / function definition
        """
        if '#' in code_block: # Code block contains comment for some reason.
            code_block = code_block[:code_block.find('#')] # Remove comment
        return code_block.replace('class','').replace('def','').replace(':','').strip()

    def get_name(self) -> str:
        return self.name

    def get_content(self) -> str:
        return self.content

    def get_all_nodes(self) -> str:
        return self.nodes

    def add_node(self, node):
        """Add node to the CURRENT node.

        Precondition: The name of node is not in self.contents
        """
        self.content.append(node)
        self.nodes[node.name] = node

    def add_content(self, c):
        """Add c to self.content. Accepts both CodeTreeNode and lines of code (str)
        """
        if isinstance(c, CodeTreeNode):
            self.add_node(c)
        else: # Assume c is a string.
            self.content.append(c)

    def get_node(self, url: str):
        """Get the node at the given url endpoint. If the endpoint
        doesn't exist return None

        Precondition: url is a non-empty string.
        """
        url = url.split('/')
        if len(url) == 1 and self.name == url[0]: # At endpoint
            return self
        elif len(url) > 1 and url[1] in self.nodes:
            next_node = self.nodes[url[1]] # Set the next node to search.
            url = '/'.join(url[1:]) # Trim front of list and convert back to string.
            return next_node.get_node(url)
        else: # Can't find the endpoint in the current node.
            return None

    def insert(self, url, item):
        """Insert item into tree at the given url's endpoint.

        Precondition: all nodes in url already exist.

        Because this tree is designed to be lossless, cannot create nodes automatically
        without their fullname
        """
        url = url.split('/')
        if len(url) == 1 and self.name == url[0]: # At endpoint
            self.add_content(item)
        else: # Else; assume there's a next node
            try:
                next_node = self.nodes[url[1]] # Set the next node to search.
            except KeyError:
                raise Exception(f"Child node '{url[1]}' does not exist in parent node '{self.name}'")

            url = '/'.join(url[1:]) # Trim front of list and convert back to string.
            next_node.insert(url, item)

# TODO: Implement.
def make_code_tree(filename: str) -> CodeTreeNode:
    """Create a CodeTree from a python file.

    Precondition: file is a valid python file without errors.
    """
    url = filename
    tree = CodeTreeNode(url)
    last_indent = 0
    indent_spacing = 0
    with open(filename, 'r') as f:
        for line in f:
            pass
    return tree

t = CodeTreeNode('file.py')
t.insert('file.py', 'x = y')
t.insert('file.py', CodeTreeNode('def test:'))
t.insert('file.py/test', 'y = 2')
print(t.get_node('file.py/test').get_content())
print(t.get_content())
t.insert('file.py/Eman', 'y = 2')
