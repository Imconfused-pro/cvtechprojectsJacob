
secret_word = "among us"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < 3:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True


if out_of_guess:
    print("Out of Guesses, YOU LOSE!!")
else:
    print("you win!")