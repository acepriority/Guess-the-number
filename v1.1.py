import re
import random

print("-developed by Ace Priority")
print("-version 1.1")
print("_________________________________________________________________________")
print("_________________________________________________________________________")
print("WELCOME")
print("_________________________________________________________________________")
print("_________________________________________________________________________")
print("**Instructions**")
print("1. You have 10 chances to guess a 4-digit number.")
print("2. After each guess, I'll tell you how many digits are in the right place.")
print("_________________________________________________________________________")
print("Let's get started!")
print("                                                                         ")
print("                                                                         ")
print("                                                                         ")
print("                                                                         ")


def generate_random_number():
    return str(random.randint(1000, 9999))


def get_user_input(prompt):
    user_input = input(prompt)
    pattern = r'^\d{4}$'

    if re.match(pattern, user_input):
        return user_input
    else:
        print("Enter a value of 4 digits: ", user_input)
        return get_user_input(prompt)


def check_guess(number, user_input):
    correct_values = 0

    for i in range(len(number)):
        if number[i] == user_input[i]:
            correct_values += 1

    if number == user_input:
        print("You guessed Right!")
        return True
    else:
        print(f"{correct_values} digit(s) in the right place")
        return False


def play_game():
    while True:
        number = generate_random_number()
        chances = 10
        while chances > 0:
            user_input = get_user_input("Guess the number: ")
            if check_guess(number, user_input):
                return True # Exit the loop if the guess is correct
            chances -= 1
            print(f"You have {chances} chances left.")
            print("_________________________________________________________________________")
            print("_________________________________________________________________________")

        print("                                                                         ")
        print("                                                                         ")
        print("SORRY, you've run out of chances.")
        print(" The correct number was:", number)
        print("                                                                         ")
        print("                                                                         ")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            return False


def main():
    while True:
        if not play_game():
            break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
    print("_________________________________________________________________________")
    print("Untill we meet again")

if __name__ == "__main__":
    main()