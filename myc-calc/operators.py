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

    def __eq__(self, other):
        if isinstance(other, Operator):
            return self.precendence == other.precendence
        return False

    def __ne__(self, other):
        if isinstance(other, Operator):
            return self.precendence != other.precendence
        return False

    def __lt__(self, other):
        if isinstance(other, Operator):
            return self.precendence < other.precendence
        raise TypeError(f"'<' not supported between '{type(self)}' and '{type(other)}'")

    def __le__(self, other):
        if isinstance(other, Operator):
            return self.precendence <= other.precendence
        raise TypeError(f"'<=' not supported between '{type(self)}' and '{type(other)}'")

    def __gt__(self, other):
        if isinstance(other, Operator):
            return self.precendence > other.precendence
        raise TypeError(f"'>' not supported between '{type(self)}' and '{type(other)}'")

    def __ge__(self, other):
        if isinstance(other, Operator):
            return self.precendence >= other.precendence
        raise TypeError(f"'>=' not supported between '{type(self)}' and '{type(other)}'")

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
        super().__init__(self, 'divide', 1)

    def execute(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ZeroDivisionError('Answer is undefined')
