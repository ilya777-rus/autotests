class Person:
    def __init__(self, a):
        print("__init__")
        self.a = a

    def __call__(self):
        print("__caall__")
