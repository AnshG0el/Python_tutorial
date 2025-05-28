import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Data type in python
# Run the game
guess_number()

# int - Integer
a = 10
print("Integer:", a)

# float - Decimal
b = 3.14
print("Float:", b)

# complex - Real + Imaginary
c = 2 + 3j
print("Complex:", c)

