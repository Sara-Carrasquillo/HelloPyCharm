# Writing a Python single line comment is with a #
"""
A multi line comment is always with three quotation marks
"""
# Imports always go up top!

# Python basics that helped me get used to Pycharm
def python_basics():

    # - Variables and printing -

    # Output should look like ---> Welcome to Python!
    print("Welcome to Python!")

    # Here we have some basic variables in the wild
    # \ n is for a newline so each one prints on a new line
    knock = "Knock Knock...\n"
    question1 = "Who's there?\n"
    answer1 = "Variable.\n"
    question2 = "Variable who?\n"
    answer2 = "This is a way of creating a variable and printing it.\n"

    """ --- Output should look like ---
        Knock Knock...
        Who's there?
        Variable.
        Variable who?
        This is a way of creating a variable and printing it.
    """
    print(knock + question1 + answer1 + question2 + answer2)

    # -- Arithmetic Operations --
    a = 10
    b = 3
    c = 10

    # Basic arithmetic operations
    addition = a + b  # 10 + 3 = 13
    subtraction = a - b  # 10 - 3 = 7
    multiplication = a * b  # 10 * 3 = 30
    division = a / b  # 10 / 3 ≈ 3.333...
    floor_division = a // b  # 10 // 3 = 3 (integer division)
    modulo = a % b  # 10 % 3 = 1 (remainder)
    exponentiation = a ** b  # 10 ** 3 = 1000 (10 raised to the power of 3)

    #
    print("Arithmetic Operations:")
    print(f"Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}, "
          f"Division: {division:.2f}, Floor Division: {floor_division}, Modulo: {modulo}, "
          f"Exponentiation: {exponentiation}\n")

    # ----- Comparison Operators -----

    # Equality: compares if two values are equal.
    print(f"a == b: {a == b}")  # False, because 10 is not equal to 3
    print(f"a == c: {a == c}")  # True, because 10 is equal to 10

    # Not equal: checks if two values are not equal.
    print(f"a != b: {a != b}")  # True

    # Greater than: checks if the left operand is greater.
    print(f"a > b: {a > b}")  # True

    # Less than: checks if the left operand is smaller.
    print(f"a < b: {a < b}")  # False

    # Greater than or equal to and less than or equal to.
    print(f"a >= c: {a >= c}")  # True (10 >= 10)
    print(f"a <= c: {a <= c}")  # True (10 <= 10)

    # Chaining comparison operators:
    # Checks if b is between a and c (in this case, since a == c, it's only True if b equals a and c).
    print(f"a <= b <= c: {a <= b <= c}")  # False, because 3 is not between 10 and 10

    # Casting is specifying a data type
    wholenumbers = int(5)  # Integer
    decimalnumbers = float(5.0)  # Float
    stringvariable = str("Five")  # String
    trueorfalse = bool(True)  # Boolean
    cannotchange = tuple((1, 2, 3, 4, 5))  # Tuple (immutable)
    canchange = list([1, 2, 3, 4, 5])  # List (mutable)
    dictionary = dict({"name": "Alice", "age": 30})  # Dictionary
    uniqueset = {1, 2, 2, 3, 4}  # Set (unique items)
    immutable_set = frozenset([1, 2, 3, 4])  # Frozen set (immutable)
    complexnumber = complex(2, 3)  # Complex number (2+3j)
    bytedata = bytes("Hello", encoding="utf-8")  # Bytes (immutable)
    mutable_bytedata = bytearray("Hello", encoding="utf-8")  # Bytearray (mutable)
    memoryviewdata = memoryview(bytedata)  # Memoryview (of bytes)
    nonedata = None  # NoneType

    # Output should look like:
    # Integer: 5, Float: 5.0, String: Five, Boolean: True, Tuple: (1, 2, 3, 4, 5),
    # List: [1, 2, 3, 4, 5], Dictionary: {'name': 'Alice', 'age': 30}, Set: {1, 2, 3, 4},
    # Frozen Set: frozenset({1, 2, 3, 4}), Complex: (2+3j), Bytes: b'Hello',
    # Bytearray: bytearray(b'Hello'), Memoryview: [72, 101, 108, 108, 111], NoneType: None
    print(f"Integer: {wholenumbers}, Float: {decimalnumbers}, String: {stringvariable}, "
          f"Boolean: {trueorfalse}, Tuple: {cannotchange}, List: {canchange}, "
          f"Dictionary: {dictionary}, Set: {uniqueset}, Frozen Set: {immutable_set}, "
          f"Complex: {complexnumber}, Bytes: {bytedata}, Bytearray: {mutable_bytedata}, "
          f"Memoryview: {list(memoryviewdata)}, NoneType: {nonedata}\n")

    # Conditional statements and loops
    ifnumber = 5

    # Equality Operator (==) compares two values to determine if they are equal.
    if ifnumber == 0:
        print(f"{ifnumber} is zero.")
    elif ifnumber % 2 == 0:
        print(f"{ifnumber} is even.")
    else:
        print(f"{ifnumber} is odd.")

    # For loop for printing numbers
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i)

    # Using the range function another way
    print(*range(1, 6))

    # Functions calls with simple calculation area of a rectangle
    def rectangle( w, l):
       return  w * l
    width = 5
    length = 10
    print(f"The area of the rectangle is {rectangle(width, length)}.")


