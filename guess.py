import random

def guess_number(secret_number, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        guess = int(input("Guess the secret number: "))
        if guess == secret_number:
            print("Congratulations! You guessed the secret number {} correctly!".format(secret_number))
            break
        elif guess < secret_number:
            print("The secret number is higher than your guess. Try again.")
        else:
            print("The secret number is lower than your guess. Try again.")
        attempts += 1
    else:
        print("Sorry, you've run out of attempts. The secret number was {}.".format(secret_number))

def main():
    print("Welcome to the Guess the Secret Number Game!")
    print("I've selected a secret number between 1 and 100. Try to guess it!")
    secret_number = random.randint(1, 100)
    max_attempts = 5
    guess_number(secret_number, max_attempts)

if __name__ == "__main__":
    main()
