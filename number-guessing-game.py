import random

lowest_num = 1

highest_number =100
answer = random.randint(lowest_num,highest_number)
print(answer)
guesses =0
is_running = True

print("python number guessing game")
print(f"select a number between {lowest_num} and {highest_number}:  ")

while is_running:

    guess = input("enter your guess: ")
    guesses = guesses+1
    if guess.isdigit():
        guess =int(guess)
        

        if guess < lowest_num > highest_number:
            print("that number is out of range")
        elif guess < answer:
            print("Too low! , Try again")
        elif guess > answer:
            print("Too high!, Try again")
        else:
            print(f"correct! the answer was {answer}")
            print(f"number of guesses: {guesses}")
            is_running = False

    else: 
        print("invalid guess")
