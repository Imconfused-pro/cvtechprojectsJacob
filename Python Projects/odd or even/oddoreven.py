number = 0

while True:
    guess = int(input("Enter a number: "))
    number +=2

    if guess == number:
        print("your number is even!")
    else:
        print("your number is odd")

    print("press 'q' to quit")

    # 'break' the program quits if the player hits the letter 'q'
    if guess == "q":
        print("thanks for playing")
        break

    
# when user quits program with 'q'. 

# Error pops up 
# 
#  'ValueError: invalid literal for int() with base 10: 'q'