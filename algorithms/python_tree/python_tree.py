from typing import TextIO, Dict, Union

# ==============
# Custom Classes
# ==============
class CodeTree:
    """Custom file tree implementation for python code.
    Uses a "url" system for search.
    """
    def __init__(self, filename: str):
        self.root = Node(filename)

    def insert(self, url: str, item: str):
        """Insert item at the given url's endpoint. If the locations before the url
        endpoint are missing Nodes, add them automatically.
        """
        node = self.root
        inserted = False
        url_list = url.split('/')
        index = 1
        while not inserted:
            # If at the endpoint.
            if url == node.url:
                node.add_content(item) # Insert content.
                inserted = True
            else:
                next_location = url_list[index] # Go to next location in url.
                # If we're not at the endpoint and the node doesn't exists.
                if next_location not in node.next:
                    relative_url = url[:url.find(next_location) + (len(next_location))]
                    next_node = Node(relative_url) # Create the node.
                    node.add_next(next_node) # Add node to next.

                node = node.next[next_location]
                index += 1

    def get_item(self, url: str) -> Union[str, None]:
        """Get the content at the given url. If the url endpoint is
        empty or doesn't exist return None.
        """
        node = self.root
        item = None
        url_list = url.split('/')
        location, endpoint = url_list[0], url_list[-1]
        index = 0
        while index <= len(url_list) - 1:
            if url == node.url:
                item = node.content if node.content != '' else None
                index += 1
            else:
                index += 1
                location = url_list[index]
                if node.next.get(location):
                    node = node.next[location]
                else: # Location doesn't exist.)
                    return None
        return item

    def pretty_print(self):
        """Recursively print all the nodes in the current CodeTree.
        """
        self._print_nodes(self.root, 0)

    def _print_nodes(self, node, depth):
        if node.is_endpoint():
            print(('-' * depth) + str(node))
        else:
            print(('-' * depth) + str(node))
            for n in node.next.values():
                self._print_nodes(n, depth + 1)

class Node:
    def __init__(self, url=''):
        self.url = url
        self.name = url.split('/')[-1]
        self.next = {}
        self.content = ''

    def __contains__(self, n) -> bool:
        """Return bool value based on if n is the name of any
        of the child nodes.
        """
        return n in self.next

    def __str__(self):
        return f'{self.name} -> {self.content}'

    def is_endpoint(self) -> bool:
        return len(self.next) == 0

    def add_content(self, s: str):
        """Append s to the Node's content attribute.
        """
        self.content += s

    def add_next(self, next: 'Node'):
        """Add a leaf node to current Node.
        """
        self.next[next.name] = next

# ===============
# General Methods
# ===============
def is_comment(s: str) -> bool:
    """Return whether s is a python comment or not.
    """
    return s.lstrip().startswith('#')

def is_code(s: str) -> bool:
    """Return whether s is a line of python or not according to these
    rules:
    - It's NOT an empty line.
    - It's NOT a line consisting of only comments.
    """
    return not s.isspace() and not is_comment(s)

def is_block(s: str) -> str:
    """Return whether s is a class or function definition
    Precondition: Python syntax is correct (won't check for colon : )
    """
    s = s.lstrip()
    return s.startswith('def ') or s.startswith('class ')

def get_block_name(s: str) -> str:
    """Get the name of function / class
    Precondition: s is non-empty and is a valid block.
    """
    definition = s
    if '(' in s:
        definition = definition.split('(')[0]
    else:
        definition = s.split(':')[0]
    return definition.replace('def', '').replace('class', '').strip()

def indent_len(s: str) -> int:
    """Get the size of the string's indentation.
    """
    return len(s) - len(s.lstrip())

def update_url(url, current_block, indent, last_indent):
    if len(url.split('/')) == 1: # If at root location.
        url += '/' # Add forward slash so the splitting works properly.

    if indent < last_indent: # The current indentation is less. Which means we're moving up the url.
        # Move up and replace endpoint.
        url = '/'.join(url.split('/')[:-2]) # Remove last endpoint and block above.
    elif indent == last_indent: # The indentation has not changed.
        url = '/'.join(url.split('/')[:-1]) # Remove endpoint.

    # If the current indentation is greater we're moving down the url. Just add.
    url += '/' + current_block # Make current_block new endpoint.
    return url

def make_file_tree(filename: str) -> 'FileTree':
    """Create a CodeTree from a python file.
    """
    url = filename
    tree = CodeTree(url)
    have_default = False # Flag for getting the default implementation.
    default_indent = 0
    last_indent = 0 # Keep track of previous line's indentation.
    code_lines = '' # Hold on to all the code belong to the current block.
    current_block = '' # The name of the current block

    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip() # Remove any escape characters.
            indent = indent_len(line) # Get the current line's indentation.
            if is_code(line):
                # Get the file's indentation spacing if we don't have it yet.
                if indent != 0 and not have_default:
                    default_indent = indent
                    have_default = True

                if is_block(line):
                    tree.insert(url, code_lines) # Insert the previous block's code.
                    current_block = get_block_name(line)
                    url = update_url(url, current_block, indent, last_indent) # Update the url to the current block's
                    code_lines = '' # Empty code_lines
                    last_indent = indent # Update indentation
                else:
                    code_lines += line + '\n' # Add line of code to current blocks.

        tree.insert(url, code_lines) # Insert any leftover code.
    return tree

if __name__ == '__main__':
    t = make_file_tree('test_code.py')
    t.pretty_print()
    print(t.get_item('test_code.py/M/argh'))
