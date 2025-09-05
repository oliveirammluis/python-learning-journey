class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self, message):
        print(f"{self.name} said: {message}")

    def is_adult(self):
        return self.age >= 18