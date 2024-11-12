number = 4
user_input = input("Enter 'y' if you would like to play: ").lower()
if user_input == "y":
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("You guessed right!")
    elif abs(number-user_number) == 1:
        print("Your guess is closer by 1")
    else:
        print("Guess again!")