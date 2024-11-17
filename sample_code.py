def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print("Addition of 2 and 3 is:", add(2, 3))
    print("Subtraction of 5 from 10 is:", subtract(10, 5))
    print("Multiplication of 4 and 5 is:", multiply(4, 5))
    print("Division of 10 by 2 is:", divide(10, 2))
