number = 4
while True:
    user_input = input("Enter 'Y/n' if you would like to play: ").lower()
    if user_input == 'n':
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed right!")
    elif abs(user_number-number) == 1:
        print("You are close by 1 number!")
    else:
        print("Try again!")
