def greet(name):
    """
    Greets the user by name.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print("Welcome to devASC!")