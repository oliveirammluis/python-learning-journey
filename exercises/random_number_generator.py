# Random Number Generator

import random

rand_int = random.randint(1, 10)
print("Random integer between 1 and 10:", rand_int)

rand_float = random.random()
print("Random float between 0 and 1:", rand_float)

choices = ["apple", "banana", "cherry"]
rand_choice = random.choice(choices)
print("Random choice from list:", rand_choice)
