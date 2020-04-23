class Operator:
    """Contains all necessary attributes and functionalities of a basic
    operator.

    name is the name of the operator. precendence is the assigned value for
    the shunting_yard algorithm's ordering. left_assoc describes the operators
    associativity (True for left, False for right).

    --Attribute Type--
    name: str
    precendence: int
    left_assoc: bool
    ------------------
    """
    def __init__(self, name = None, precendence = 0, left_assoc = True):
        self.name = name
        self.precendence = precendence
        self.left_assoc = left_assoc

    def execute(self, x, y):
        pass

class Addition(Operator):
    def __init__(self):
        super().__init__(self, 'add', 0)

    def execute(self, x, y):
        return x + y

class Subtraction(Operator):
    def __init__(self):
        super().__init__(self, 'subtract', 0)

    def execute(self, x, y):
        return x - y

class Multiplication(Operator):
    def __init__(self):
        super().__init__(self, 'multiply', 1)

    def execute(self, x, y):
        return x * y

class Division(Operator):
    def __init__(self):
        super().__init__(self, 'divide', 2)

    def execute(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ZeroDivisionError # Kinda redundant, but good to have.


# Dictionary format: Operand character: Precendence value
# The higher the value, the more precendence it has.
OPERATORS = {'+':0,
            '-':0,
            '*':1,
            '/':1}

# PARENTHESIS = ['(', ')']

operator_stack = []
output = ''

def extract_data(s: str) -> list:
    """Return a list of all items in the expression.
    Multi-digit numbers will be accounted for as one item.
    """
    # TODO: Investigate and remove redundancies
    s = s.replace(' ','')
    L = []
    start = 0
    for index in range(len(s)):
        if s[index] in PARENTHESIS:
            L.append(s[index])
            if index + 1 > len(s):
                start = index
            else:
                start = index + 1
        elif s[index] in OPERATORS:
            L.append(s[start:index])
            L.append(s[index])
            if index + 1 > len(s): # This should never be the case unless theres a user error.
                start = index
            else:
                start = index + 1

        if index == len(s) - 1:
            L.append(s[start:len(s)])
    return L


def shunting_yard(s: list) -> str:
    """Convert an index notation mathematical expression to reverse polish
    notation.

    Precondition: s is already balanced and correctly formatted.
    """
    output = ''
    for c in s:
        if c.isdigit():
            output += ' ' + c
        elif c in OPERATORS:
            if operator_stack and operator_stack[-1] in OPERATORS and \
                OPERATORS[c] <= OPERATORS[operator_stack[-1]]:
                output += ' ' + operator_stack.pop()
            operator_stack.append(c)
        elif c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack[-1] != '(' and len(operator_stack) > 0:
                output += ' ' + operator_stack.pop()
            if operator_stack[-1] == '(':
                operator_stack.pop()

    while operator_stack:
        output += ' ' + operator_stack.pop()

    return output.strip()

def calculate(s: str) -> float:
    """Calculate an expression in reverse polish notation.
    """
    # TODO: Implement.
    s = s.split(' ') # Tokenize string.
    index = 0
    operator_stack = []
    operand_stack
    while s:
        if index > len(s):
            index = 0 # Reset back to front of list.
        if s[index] in OPERATORS:
            operator_stack.append(s[index])

    return

def main():
    s = input('Expression: ')
    s = extract_data(s)
    print('Extracted Data: ', s)
    print('Output: ', shunting_yard(s))

if __name__ == '__main__':
    main()
