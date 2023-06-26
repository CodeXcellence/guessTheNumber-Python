import random

# generate random number
number = random.randint(0, 100)
attempts = 0

def match_num(num):
    if num == number:
        return 1
    elif num > number:
        print("You guessed a greater number.")
        return 0
    else:
        print("You guessed a smaller number.")
        return 0

while True:
    user = input("Enter a number (0 - 100): ")
    attempts += 1
    if user.isnumeric():
        user = int(user)
        if match_num(user) == 1:
            print(f"Congratulation, you guessed the number in {attempts} attempts.")
            with open("score.txt", "w") as score:
                score.write(str(attempts))
            user_in = input("Would you like to play again? Yes(y), No(n): ").lower()
            if user_in == "y":
                continue
            else:
                break
        else:
            continue
    else:
        print("Invalid input. Please input only number.\n Try again.")
        continue