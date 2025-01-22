number = 0

while True:
    guess = int(input("Enter a number: "))
    number +=2

    if guess == number:
        print("your number is even!")
    else:
        print("your number is odd")

    print("press 'q' to quit")

    if guess == "q":
        print("thanks for playing")
        break
