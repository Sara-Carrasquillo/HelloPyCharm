# Intermediate Python review
# Imports always go at the top
import requests # External module for HTTP requests
import functools # For creating decorators
from functools import reduce # Import from functools

# -Advanced Functions-

def python_intermediate():

    # Nested function factorial example
    # A factorial is like 5! = 5*4*3*2*1 = 120
    def factorial(n):
        # Base case: factorial of 0 is 1
        if n == 0:
            return 1
        # Error for negative numbers
        elif n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        # Recursive case: factorial of n is n * factorial(n-1)
        else:
            return n * factorial(n - 1)

    # Output should look like ---> Factorial of 5 is 120
    print("Factorial of 5 is", factorial(5))

    # Lambda function example: square of any number
    square = lambda x: x**2
    # Output should look like ---> Using lambda the square of 6 is 36
    print("Using lambda the square of 6 is", square(6))

    # --Comprehensions--

    # List of numbers for Map / Filter / Reduce
    numbers = [1, 2, 3, 4, 5]

    # MAP applies the function to each element
    squared_numbers = list(map(square, numbers))
    # Output should look like ---> Squared numbers using map: [1, 4, 9, 16, 25]
    print("Squared numbers using map:", squared_numbers)

    # FILTER returns only those elements that satisfy the condition (even numbers here)
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    # Output should look like ---> Even numbers using filter: [2, 4]
    print("Even numbers using filter:", even_numbers)

    # REDUCE applies a function cumulatively to the items in the list
    sum_numbers = reduce(lambda x, y: x + y, numbers)
    # Output should look like ---> Sum of numbers using reduce: 15
    print("Sum of numbers using reduce:", sum_numbers)

    # ---Exception Handling---
    def safe_division(a: float, b: float) -> float:
        if b == 0:
            print("ERROR: Division by zero")
            # Return a default float value (0.0) when division by zero occurs
            return 0.0
        else:
            return a / b

    # Output should look like ---> Safe division 10 / 2 = 5.0
    print("Safe division 10 / 2 =", safe_division(10, 2))
    # Output should show an error message and then ---> Safe division 10 / 0 = None
    print("Safe division 10 / 0 =", safe_division(10, 0))

    # Classes and Inheritance

    # Define a base class 'Animal'
    class Animal:
        # Initialize with a name attribute
        def __init__(self, name: str) -> None:
            self.name = name

        # Returns a generic animal sound (to be overridden by subclasses)
        @staticmethod
        def speak() -> str:
            return "animal sound..."

        # Returns a string representation of the Animal object
        def __str__(self) -> str:
            return f"Animal: {self.name}"

    # Define a subclass 'Dog' that inherits from Animal
    class Dog(Animal):
        # Overrides the speak method to return 'Woof!'
        def speak(self) -> str:
            return "Woof!"

    # Define a subclass 'Cat' that inherits from Animal
    class Cat(Animal):
        # Overrides the speak method to return 'Meow!'
        def speak(self) -> str:
            return "Meow!"

    """ 
    Polymorphism example list of animals and printing their sounds
     Output should look like ---> 
        Animal: Buddy says Woof!
        Animal: Whiskers says Meow!
        Animal: Animal says animal sound...
     """
    animals = [Dog("Buddy"), Cat("Whiskers"), Animal("Animal")]
    for animal in animals:
        print(f"{animal} says {animal.speak()}")

    # File I/O with Context Managers

    def file_io_demo() -> None:
        filename = "intermediate_python.txt"

        # Writing to the file using 'with' ensures the file is properly closed.
        with open(filename, "w") as file:
            file.write("This is an intermediate Python example.\n")
            file.write("We use context managers for safe file I/O.\n")

        # Reading from the file
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)

    # Call the function to demonstrate file I/O
    file_io_demo()

    # ---Decorators---
    #  Adds extra behavior before or after the function runs without changing the function’s own code.
    def debug(func):
        # @functools.wraps(func) helps us keep the original function's name and docstring, this keeps the original function's info.
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

    # 'debug' is a decorator that will add extra printing around the function call.
    @debug
    def add(a: int, b: int) -> int:
        # Return the sum of two integers
        return a + b

    @debug
    def greet(greeting: str, name: str, punctuation: str = "!") -> str:
        return f"{greeting} {name}{punctuation}"

    sum_result = add(10, 20)
    print(f"Sum of 10 and 20: {sum_result}\n")

    message1 = greet("Hello", "Alice")
    print(f"Greeting: {message1}\n")

    message2 = greet("Hi", "Bob", punctuation="!!!")
    print(f"Greeting: {message2}\n")

    # ---Generators---
    def my_generator(n):
        # Start with the first number (0)
        current = 0
        # Continue looping until current reaches n
        while current < n:
            # Yield the current number, pausing the function here
            yield current
            # Increment current to get the next number on the next iteration
            current += 1

    # When we call my_generator(5), it returns a generator object.
    # The for loop automatically calls next() on the generator to get each yielded value.
    for value in my_generator(5):
        # Output should look like ---> 0, then 1, then 2 (each on a new line)
        print(value)

    # ---External Modules and Libraries---
    try:
        # Attempt to connect to GitHub's API via a GET request
        response = requests.get("https://api.github.com")

        # Check if we received a successful response (HTTP 200)
        if response.status_code == 200:
            print("Success! We connected to GitHub's API.")
            print("Status Code:", response.status_code)
        else:
            # If the status code is not 200, indicate that we received a response but something unexpected occurred.
            print("Connected to GitHub's API, but received an unexpected status code:", response.status_code)
    except Exception as e:
        # This block handles any errors (like network issues or an invalid URL)
        print("Error connecting to GitHub's API:", e)







