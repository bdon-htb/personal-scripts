# Dictionary format: Operand character: Precendence value
# The higher the value, the more precendence it has.
OPERANDS = {'+':0,
            '-':0,
            '*':1,
            '/':1}

PARENTHESIS = ['(', ')']

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
        elif s[index] in OPERANDS:
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
        elif c in OPERANDS:
            if operator_stack and not (operator_stack[-1] in PARENTHESIS) and \
                OPERANDS[c] <= OPERANDS[operator_stack[-1]]:
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
    s = s.split(' ')
    for index in range(len(s)):
        if s[index] in OPERANDS:
            pass
    return

def main():
    s = input('Expression: ')
    s = extract_data(s)
    print(s)
    print(shunting_yard(s))

if __name__ == '__main__':
    main()
