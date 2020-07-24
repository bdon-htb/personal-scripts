from typing import Union
import operators as op

# Dictionary format: Operator character: custom Operator object.
OPERATORS = {'+': op.Addition(),
            '-': op.Subtraction(),
            '*': op.Multiplication(),
            '/': op.Division()}

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
        if s[index] == '(':
            L.append(s[index])
            if index + 1 > len(s):
                start = index
            else:
                start = index + 1
        elif s[index] in OPERATORS or s[index] == ')':
            L.append(s[start:index])
            L.append(s[index])
            if index + 1 > len(s):
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

def calculate(s: str) -> Union[float, int]:
    """Calculate an expression in reverse polish notation.
    Precondition: Expression is valid.
    """
    s = s.split(' ') # Tokenize string.
    index = 0
    operand_stack = []
    while index < len(s):
        if s[index].isdigit():
            operand_stack.append(int(s[index]))
        elif s[index] in OPERATORS:
            operator = OPERATORS[s[index]]
            x = operand_stack[-2]
            y = operand_stack[-1]
            operand_stack = operand_stack[:-2] + [operator.execute(x,y)] # cut down list.

        index += 1
    return operand_stack[0]

def main():
    s = input('Expression: ')
    s = extract_data(s)
    print('Extracted Data: ', s)
    print('Output: ', shunting_yard(s))
    print('Calculated: ', calculate(shunting_yard(s)))

if __name__ == '__main__':
    main()
