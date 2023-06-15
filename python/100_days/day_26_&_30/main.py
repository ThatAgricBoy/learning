import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

game_on = True
while game_on:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Enter only letters of the alphabet")
    else:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        new_word = input("Do you have more words to check?: Yes, No: ").upper()
        if new_word == "NO":
            game_on = False




