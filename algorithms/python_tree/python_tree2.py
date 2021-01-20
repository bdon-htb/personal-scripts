# The last python_tree implementation was pretty lossy and didn't properly account for content spread out across the file.
from typing import List, Union

class CodeTreeNode:
    """A hierarchical recursive tree structure for python code.
    """
    def __init__(self, code_block: str):
        self.fullname = code_block # line of code (with whitespace) that defines the code block the node represent
        self.name = get_block_name(code_block)
        self.content = [] # A sequential arrangement of the node's content
        self.nodes = {} # Hashmap for quick access to child nodes.

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

    def get_node(self, url: str) -> Union[CodeTreeNode, None]:
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

        Because this tree is designed to be lossless, cannot create missing
        nodes automatically without their fullname
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

def get_block_name(s: str) -> str:
    """Get the name of function / class
    Precondition: s is non-empty and is a valid block.
    """
    definition = s.strip()
    if '(' in s:
        definition = definition.split('(')[0]
    else:
        definition = s.split(':')[0]
    return definition.replace('def', '').replace('class', '').strip()

def is_block(s: str) -> str:
    """Return whether s is a class or function definition
    Precondition: Python syntax is correct (won't check for colon : )
    """
    s = s.lstrip()
    return s.startswith('def ') or s.startswith('class ')

def indent_len(s: str) -> int:
    """Get the size of the string's indentation.
    """
    return len(s) - len(s.lstrip())

# TODO: implement
def update_url(indent, last_indent, indent_spacing):
    pass

# TODO: Implement.
# TODO: Add some logging so it's easier to trace.
def make_code_tree(filename: str) -> CodeTreeNode:
    """Create a CodeTree from a python file.

    Precondition: file is a valid python file without errors or duplicates blocks.
    """
    url = filename
    tree = CodeTreeNode(url)
    indent = 0 # Current line's leading whitespace
    last_indent = 0 # Last line's leading whitespace
    indent_spacing = None # The number of spaces per indentation level
    with open(filename, 'r') as f:
        for line in f:
            url = update_url(url)
            if is_block(line):
                new_node = CodeTreeNode(line) # Create new node from code
                tree.insert(url, new_node)
            else: # Is regular line of code.
                tree.insert(url, line) # Insert code

    return tree
