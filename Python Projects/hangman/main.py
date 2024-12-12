import random

fruits = [
    'apple', 'banana', 'orange', 'mango', 'strawberry', 'pineapple', 'blueberry',
    'grape', 'watermelon', 'peach', 'cherry', 'pear', 'lemon', 'lime', 'kiwi',
    'pomegranate', 'avocado', 'papaya', 'coconut', 'fig', 'guava', 'dragon fruit',
    'lychee', 'raspberry', 'blackberry', 'plum', 'apricot', 'cantaloupe',
    'tangerine', 'passion fruit', 'grapefruit'
]

guess_limit = 7
user_guess = 10
word_to_guess = random.choice(fruits)
word_length = len(word_to_guess)


guessed_word = ["_"] * word_length

while "_" in guessed_word and user_guess > 0:
    guess = input("Guess a letter: ").lower()

    if guess in word_to_guess:
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[index] = guess
        print("good job!")
    else:
        user_guess -= 1
        print(f"sorry that is the wrong answer, you only have {user_guess} guesses left")

    print("Current word: ", " ".join(guessed_word))

if "_" not in guessed_word:
    print("Congrats! you have guessed the word: "+ word_to_guess)
else:
    print(f"sorry, you're out of guesses! the word is: {word_to_guess}")