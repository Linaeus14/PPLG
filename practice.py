# Import statements
import sys

# Function definitions
def greet(name):
    """
    Function to greet the user.
    Args:
    name (str): The name of the user.
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    Function to add two numbers.
    Args:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

def main():
    # print(add_numbers(10,5))
    # print(greet("Arya"))


    # array = [8, 6, 4, 2]
    # for index in range(8, 1, -2):
    #     index += 2 # sama dengan index = index + 5
    #     print(index)

    # n = 100
    # array = []
    # for _ in range(3):
    #     array.append(n)
    #     n //= 2
    # print(array)

    n = 10
    gameLoop = True
    while gameLoop:
        print(n)
        n -= 1
        if n == 5:
            gameLoop = False

# Entry point of the program
if __name__ == "__main__":
    main()
