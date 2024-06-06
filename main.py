# line for test
def get_name():
    return input("Please enter your name: ")


def get_age():
    return int(input("Please enter your age: "))


def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")


def main():
    name = get_name()
    age = get_age()
    greet_user(name, age)


if __name__ == "__main__":
    main()
