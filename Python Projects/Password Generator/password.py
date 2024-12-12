import random

existing_passwords = 0  # we had it in the loop which made it reset every time.because of that issue, we moved it up top
# so it would keep its count

Random = input("Do you need some passwords?: ")

run = True
while run:
    length_of_characters = 0
    numbers = random.randint(1, 20)
    letters = random.sample(population=["A", "B", "C", "D", "E", "F", "G", "H", "*", "#", "$", "!", "@", "%", "&"], k=7)

    if Random == "yes":
        print(numbers, *letters)

        length_of_characters = len(str(numbers))  # giving it a len() because it does not have a "length" directly

        for character in letters:
            length_of_characters += 1

        print(f"The length of your password is: {length_of_characters}")

        if length_of_characters >= 1:
            existing_passwords += 1
            print(f"You have made {existing_passwords} password(s).")

    choice = input("Press (Q) to quit or (C) for another one: ")

    if choice.lower() == "q":
        print("thanks for playing!")
        break
    elif choice.lower() == "c":
        run = True