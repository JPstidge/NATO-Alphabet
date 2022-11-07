

import pandas
# Create Phonetic alphabet dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Prompt user for input.

generate = True
while generate:

    def generate_phon():
        word = input("Enter a word: ").upper()
        try:
            phonetic_word = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print("Invalid input, words only.")
            generate_phon()
        else:
            print(phonetic_word)


    generate_phon()

    again = input("Enter another word? 'y' or 'n': ").lower()
    if again == "n":
        generate = False