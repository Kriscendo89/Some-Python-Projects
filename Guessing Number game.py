import random

top_of_range = input("Enter a number: ")    

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a valid number next time.")
    quit()

random_number = random.randint(1, top_of_range)

while True:
    guess = input("Make a guess: ")
    
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a valid number next time.")
        continue

    if guess < 1 or guess > top_of_range:
        print(f"Please enter a number between 1 and {top_of_range}.")
        continue

    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("You got it!")
        break
