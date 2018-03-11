class Cat:
    def __init__(self):
        print("Initializing cat class...")
    print("meow")

class Dog:
    def __init__(self):
        print("Initializing dog class...")
    print("woof woof woof")

# Test function
if __name__ == "__main__":
    # Testing the initialization
    FirstClass = Cat()
    print(type(FirstClass))
    # Testing the initialization
    SecondClass = Dog()
    print(type(SecondClass))