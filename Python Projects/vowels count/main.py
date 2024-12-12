vowels = ["a", "e", "i", "o", "u"]

a = 0
e = 0
i = 0
o = 0
u = 0
vowel_count = 0

main_Question = input("please enter a phrase: ")

for letters in main_Question:
    if letters in vowels:
        vowel_count += 1
        print(f"you have {vowel_count} vowels in your sentence")

