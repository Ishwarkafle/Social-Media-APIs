import numpy as np

rng = np.random.default_rng()

num = int(input("Guess the number between 1 and 10: "))

while True:
    random_number = rng.integers(1, 11)

    if num == random_number:
        print("You are correct!")
        break
    else:
        print("Ehh ehh try again")
        print("Number was:", random_number)
        num = int(input("Guess again: "))