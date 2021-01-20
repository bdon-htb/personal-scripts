# The last python_tree implementation was pretty lossy and didn't properly account for content spread out across the file.
from typing import List, Union, Any

class CodeTreeNode:
    """A hierarchical recursive tree structure for python code.
    """
    def __init__(self, code_block: str):
        self.fullname = code_block # line of code (with whitespace) that defines the code block the node represent
        self.name = get_block_name(code_block)
        self.content = [] # A sequential arrangement of the node's content
        self.nodes = {} # Hashmap for quick access to child nodes.

    def __str__(self):
        return f'{self.name} -> \n{self.content}'

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

    def get_node(self, url: List[str]) -> Union['CodeTreeNode', None]:
        """Get the node at the given url endpoint. If the endpoint
        doesn't exist return None

        Precondition: url is a non-empty string.
        """
        if len(url) == 1 and self.name == url[0]: # At endpoint
            return self
        elif len(url) > 1 and url[1] in self.nodes:
            next_node = self.nodes[url[1]] # Set the next node to search.
            return next_node.get_node(url[1:])
        else: # Can't find the endpoint in the current node.
            return None

    def insert(self, url: List[str], item):
        """Insert item into tree at the given url's endpoint.

        Precondition: all nodes in url already exist.

        Because this tree is designed to be lossless, cannot create missing
        nodes automatically without their fullname
        """
        if len(url) == 1 and self.name == url[0]: # At endpoint
            self.add_content(item)
        else: # Else; assume there's a next node
            try:
                next_node = self.nodes[url[1]] # Set the next node to search.
            except KeyError:
                raise Exception(f"Child node '{url[1]}' does not exist in parent node '{self.name}'")

            next_node.insert(url[1:], item)

    def pretty_print(self, depth=0):
        for c in self.content:
            if isinstance(c, CodeTreeNode):
                print(c.fullname, end='')
                c.pretty_print(depth + 1)
            else:
                print(c, end='')

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

def is_comment(s: str) -> bool:
    """Return whether s is a comment or not
    """
    return s.lstrip().startswith('#')

def is_code(s: str) -> bool:
    """Anything that is not an empty line or a comment
    is considered code.
    """
    return not is_comment(s) and not s.isspace()

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

# TODO: Implement.
# TODO: Add some logging so it's easier to trace.
def make_code_tree(filename: str) -> 'CodeTreeNode':
    """Create a CodeTree from a python file.

    Precondition: file is a valid python file without errors or duplicates blocks.
    """
    url = [filename] # Should never be empty.
    tree = CodeTreeNode(filename)

    indent = 0 # Current line's leading whitespace
    last_block_indent = -1
    indent_spacing = None # The number of spaces per indentation level
    line_no = 0
    with open(filename, 'r') as f:
        for line in f:
            line_no += 1
            indent = indent_len(line)
            if is_code(line):
                if indent_spacing is None and indent != 0:
                    indent_spacing = indent # Get file's indentation spacing.

                # Update url.
                if is_block(line) and indent > last_block_indent:
                    url.append(get_block_name(line)) # Add endpoint.
                elif is_block(line) and indent == last_block_indent:
                    url[-1] = get_block_name(line) # Replace endooint.
                elif indent < last_block_indent:
                    # By this point indent_spacing should not be None
                    n = (last_block_indent - indent) // indent_spacing # Calculate level.
                    url = url[:-(n+1)] # Go up url by n + 1 levels.

            if is_block(line):
                last_block_indent = indent
                tree.insert(url[:-1], CodeTreeNode(line)) # Insert block node at endpoint above.
            else:
                tree.insert(url, line)
    return tree

if __name__ == '__main__':
    filename = 'test_code.py'
    t = make_code_tree(filename)
    t.pretty_print()
