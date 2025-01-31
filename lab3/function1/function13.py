import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print("\nWell,", name + ", I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)  # Случайное число от 1 до 20
    attempts = 0

    while True:
        print("\nTake a guess.")
        guess = int(input())
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("Good job,", name + "! You guessed my number in", attempts, "guesses!")
            break


guess_the_number()
