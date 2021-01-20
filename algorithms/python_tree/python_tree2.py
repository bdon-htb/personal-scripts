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
        """Precondition: A node of the same name does not already exist in
        self.contents
        """
        self.content.append(node)
        self.nodes[node.name] = node

    def add_content(self, c):
        """Add c to self.content. Accepts both CodeTreeNode and lines of code (str)
        """
        if isinstance(obj, CodeTreeNode):
            self.add_node(obj)
        else: # Assume c is a string.
            self.content.append(c)

    def get_node(self, url: str):
        """Get the node at the given url endpoint. If the endpoint
        doesn't exist return None
        """
        url = url.split('/')
        if self.name == url[-1]: # At endpoint
            return self
        elif len(url) > 1 and url[1] in self.nodes:
            next_node = self.nodes[url[1]] # Set the next node
            url = '/'.join(url[1:]) # Trim front of list and convert back to string.
            return next_node.get_node(url)
        else: # Can't find the endpoint in the current node.
            return None

t = CodeTreeNode('file.py')
n = CodeTreeNode('      class Bob:\n')
t.add_node(n)
x = t.get_node('file.py/Bob')
print(x.get_node('file.py/Bob').name)
