# Simple Python program to greet the user

import sys

# Function to print greeting message
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Main function to run the program
def main():
    if len(sys.argv) != 3:
        print("Usage: main.exe <name> <age>")
        sys.exit(1)
    
    name = sys.argv[1]
    age = sys.argv[2]
    greet_user(name, age)

# Entry point of the program
if __name__ == "__main__":
    main()
