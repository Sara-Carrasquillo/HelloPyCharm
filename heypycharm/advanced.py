# Advanced Python review
# Imports always go at the top
import functools               # For functional programming tools and decorators
import json                    # For JSON serialization
import pickle                  # For object serialization
import threading               # For threading concurrency
import asyncio                 # For async concurrency
import time                    # For sleep/delay functions
import socket                  # For networking with sockets
import tkinter as tk           # For creating GUI applications
from tkinter import messagebox # For popup messages in GUI

# Flask for Web Development
from flask import Flask, jsonify

# Data science libraries
import numpy as np             # For numerical operations
import pandas as pd            # For data analysis
import matplotlib.pyplot as plt# For plotting graphs

# --- Functional Programming Section ---
def python_advanced():
    print("=== Advanced Python Concepts Demo ===\n")

    # --- Functional Programming ---
    print("== Functional Programming ==")
    # Lambda function example: square a number
    square = lambda m: m ** 2  # Using lambda to compute the square
    # List of numbers to work with
    numbers = list(range(1, 6))
    # MAP applies the lambda to each number in the list
    squared_numbers = list(map(square, numbers))
    # FILTER returns only even numbers from the list
    even_numbers = list(filter(lambda d: d % 2 == 0, numbers))
    # REDUCE applies a cumulative function (sum) to the list
    sum_numbers = functools.reduce(lambda a, b: a + b, numbers)
    # Output the results
    print("Original numbers:", numbers)                                 # Expected: [1, 2, 3, 4, 5]
    print("Squared numbers using map:", squared_numbers)                # Expected: [1, 4, 9, 16, 25]
    print("Even numbers using filter:", even_numbers)                   # Expected: [2, 4]
    print("Sum of numbers using reduce:", sum_numbers)                    # Expected: 15

    # --- Design Patterns Section ---
    print("\n== Design Patterns ==")

    # Singleton Pattern using a metaclass:
    class SingletonMeta(type):
        _instances = {}  # Dictionary to hold single instances

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]

    class Singleton(metaclass=SingletonMeta):
        def __init__(self, value):
            self.value = value  # Store a value to verify singleton behavior

    # Create two instances and check if they refer to the same object
    s1 = Singleton("first")
    s2 = Singleton("second")
    # Output should show that both instances have the same value
    print("Singleton values (should be the same):", s1.value, s2.value)

    # Factory Pattern: Create objects based on given type
    class Animal:
        def speak(self):
            raise NotImplementedError("Subclasses must implement this method")

    class Dog(Animal):
        def speak(self):
            return "Woof!"  # Dog's sound

    class Cat(Animal):
        def speak(self):
            return "Meow!"  # Cat's sound

    # Factory function returns an instance based on the animal type
    def animal_factory(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

    # Create animal instances using the factory
    dog = animal_factory("dog")
    cat = animal_factory("cat")
    # Output animal sounds
    print("Factory created dog says:", dog.speak())  # Expected: Woof!
    print("Factory created cat says:", cat.speak())  # Expected: Meow!

    # Observer Pattern: Implement a simple event system
    class Event:
        def __init__(self):
            self.subscribers = []  # List to hold subscriber functions

        def subscribe(self, func):
            self.subscribers.append(func)  # Add a subscriber

        def notify(self, *args, **kwargs):
            for subscriber in self.subscribers:
                subscriber(*args, **kwargs)  # Notify each subscriber

    # Create an event instance and subscribe a lambda function
    event = Event()
    event.subscribe(lambda msg: print("Observer received:", msg))
    # Notify subscribers with a message
    event.notify("Event triggered!")

    # --- Metaprogramming Section ---
    print("\n== Metaprogramming ==")

    # Metaclass that automatically adds an attribute to classes
    class AutoAttributesMeta(type):
        def __new__(mcs, name, bases, namespace):
            namespace['auto_attribute'] = f"Auto attribute for {name}"  # Auto-generated attribute
            return super().__new__(mcs, name, bases, namespace)

    # Create a demo class that uses the metaclass
    class MetaClassDemo(metaclass=AutoAttributesMeta):
        def __init__(self):
            self.auto_attribute = None

        pass

    # Instantiate and output the auto-generated attribute
    meta_instance = MetaClassDemo()
    print("MetaClassDemo auto attribute:", meta_instance.auto_attribute)

    # Decorator to log function calls, similar to intermediate example
    def log_call(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")  # Log call details
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")  # Log result
            return result

        return wrapper

    # Decorated function example: add two numbers
    @log_call
    def add(a, b):
        return a + b  # Return sum

    # Call the decorated function to see logging in action
    add(3, 4)

    # --- Concurrency Section ---
    print("\n== Concurrency ==")

    # Threading example: function to be run in a separate thread
    def thread_worker(name):
        print(f"[Thread] {name} is starting")  # Notify thread start
        time.sleep(1)  # Simulate work with sleep
        print(f"[Thread] {name} has finished")  # Notify thread finish

    # Function to start multiple threads
    def threading_demo():
        threads = []  # List to hold thread objects
        for i in range(3):
            # Create and start a thread
            t = threading.Thread(target=thread_worker, args=(f"Thread-{i}",))
            threads.append(t)
            t.start()
        # Wait for all threads to finish
        for t in threads:
            t.join()

    threading_demo()  # Run threading demo

    # Asyncio example: asynchronous worker function
    async def async_worker(name):
        print(f"[Async] Task {name} starting")
        await asyncio.sleep(1)  # Asynchronously sleep for 1 second
        print(f"[Async] Task {name} completed")
        return f"Result from {name}"

    # Function to run asyncio tasks concurrently
    async def asyncio_demo():
        tasks = [async_worker(f"Task-{i}") for i in range(3)]
        results = await asyncio.gather(*tasks)
        print("Asyncio results:", results)

    asyncio.run(asyncio_demo())  # Run the asyncio demo

    # --- Data Serialization Section ---
    print("\n== Data Serialization ==")

    # Define sample data as a dictionary
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}

    # JSON serialization: convert dictionary to JSON string
    json_str = json.dumps(data)
    print("JSON serialized:", json_str)

    # JSON deserialization: convert JSON string back to dictionary
    data_from_json = json.loads(json_str)
    print("JSON deserialized:", data_from_json)

    # Pickle serialization: convert object to bytes
    pickle_bytes = pickle.dumps(data)
    # Pickle deserialization: convert bytes back to object
    data_from_pickle = pickle.loads(pickle_bytes)
    print("Pickle deserialized:", data_from_pickle)

    # --- Web Development Section (Flask) ---
    print("\n== Web Development (Flask) ==")
    # Initialize the Flask application
    app = Flask(__name__)

    # Define a route to return sample JSON data
    @app.route("/api/data")
    def api_data():
        return jsonify({"message": "Hello from Flask!", "data": [1, 2, 3]})

    # Function to run the Flask app in a separate thread so it doesn't block the demo
    def run_flask():
        threading.Thread(target=app.run, kwargs={"debug": False}).start()
        time.sleep(1)  # Allow time for the Flask server to start

    run_flask()
    print("Flask app running at http://127.0.0.1:5000/api/data")

    # --- Networking Section ---
    print("\n== Networking ==")
    try:
        # Creates a TCP connection to example.com on port 80
        with socket.create_connection(("example.com", 80), timeout=5) as sock:
            # A simple HTTP GET request
            request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
            sock.sendall(request.encode())  # Send the HTTP request
            # Receives the response (first 1024 bytes)
            response = sock.recv(1024)
            print("Networking response (first 1024 bytes):")
            print(response.decode(errors='ignore'))
    except Exception as e:
        print("Networking error:", e)

    # --- GUI Programming Section (Tkinter) ---
    print("\n== GUI Programming (Tkinter) ==")
    # Create a basic GUI window using Tkinter
    root = tk.Tk()
    root.title("Tkinter GUI Demo")

    # Define a function to be called when the button is clicked
    def on_click():
        messagebox.showinfo("Information", "Button Clicked!")  # Show info popup

    # Create a button widget with a click event
    button = tk.Button(root, text="Click Me", command=on_click)
    button.pack(padx=20, pady=20)  # Place the button with padding

    # Call the Tkinter main loop in the main thread (do not run this in a separate thread)
    root.mainloop()  # This call will block until the window is closed

    # --- Data Science Section ---
    print("\n== Data Science ==")

    # Numpy: Create an array and compute its mean
    arr = np.array([1, 2, 3, 4, 5])
    print("NumPy array:", arr)
    print("Mean of array:", np.mean(arr))

    # Pandas: Create a DataFrame with random data
    df = pd.DataFrame({
        "Random_A": np.random.rand(5),
        "Random_B": np.random.rand(5)
    })
    print("Pandas DataFrame:")
    print(df)

    # Matplotlib: Plot a sine wave and save the figure as an image
    x = np.linspace(0, 2 * np.pi, 100)  # Generate 100 points between 0 and 2π
    y = np.sin(x)  # Compute sine of each point
    plt.figure()
    plt.plot(x, y, marker="o", markersize=3)
    plt.title("Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.savefig("sine_wave.png")  # Save the plot as an image file
    print("Matplotlib plot saved as sine_wave.png")