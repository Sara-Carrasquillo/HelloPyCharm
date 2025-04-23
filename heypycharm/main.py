
# This is my main class for running my python code
from basics import python_basics
from intermediate import python_intermediate
from advanced import python_advanced

def main():
    while True:
        # Display the main menu options
        print("\n=== Python Practice Application ===")
        print("Select a practice level:")
        print("1. Basics")
        print("2. Intermediate")
        print("3. Advanced")
        print("4. Exit")
        try:
            level = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Based on user's choice, call the corresponding function
        if level == 1:
            python_basics()
        elif level == 2:
            python_intermediate()
        elif level == 3:
            python_advanced()
        elif level == 4:
            print("Exiting the practice application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()




