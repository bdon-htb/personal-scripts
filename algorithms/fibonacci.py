import random


def fib(n: int):
    """A recursive implementation of the fibonacci sequence.
    Assumes that n is a postive integer 0 or greater.
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def main():
    n = random.randint(0, 10)
    print(f'The {n}th term of the fibonacci sequence is {fib(n)}')
    fib(n)

if __name__ == '__main__':
    main()
