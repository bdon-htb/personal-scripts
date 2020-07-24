import random

def fact(n: int):
    """A recursive implementation of factorials.
    Calculates factorial of n.

    Precondition: n is a positive integer or 0.
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def main():
    num = random.randint(1, 10)
    print(f'The factorial of {num} is {fact(num)}')

if __name__ == '__main__':
    main()
