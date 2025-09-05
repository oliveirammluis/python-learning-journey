from person import Person

def main():
    person1 = Person("Alice", 20)
    person2 = Person("Bob", 15)

    person1.talk("Hello, world!")
    person2.talk("I want ice cream!")

    print(f"Is {person1.name} an adult? {person1.is_adult()}")
    print(f"Is {person2.name} an adult? {person2.is_adult()}")

if __name__ == "__main__":
    main()
