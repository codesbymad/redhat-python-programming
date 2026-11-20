import random

target = random.randint(1, 100)
nguesses = 0
ninvalid = 0

print("I'm thinking of a number from 1 to 100")

while True:
    try:
        guess = int(input("Try to guess my number: "))
        if guess < 1 or guess > 100:
            print(f"{guess} is not a valid guess. Please try again.")
            ninvalid += 1
            continue
    except ValueError:
        print("This is not a valid integer. Please try again.")
        ninvalid += 1
        continue

    nguesses += 1
    if guess < target:
        print(f"{guess} is too low - please guess again.")
    elif guess > target:
        print(f"{guess} is too high - please guess again.")
    else:
        print(f"{guess} is correct!")
        break

if nguesses == 1:
    print(f"You guessed my number in {nguesses} guess.")
else:
    print(f"You guessed my number in {nguesses} guesses.")

if ninvalid == 1:
    print(f"You made {ninvalid} invalid guess.")
else:
    print(f"You made {ninvalid} invalid guesses.")
