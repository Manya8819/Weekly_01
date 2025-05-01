import random

secret = random.randint(1, 100)
attempts = 5

for i in range(attempts):
    guess = input(f"Attempt {i+1}/5 - Enter your guess (1-100): ")
    
    if not guess.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    guess = int(guess)
    
    if guess == secret:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry! The number was {secret}. Better luck next time.")
