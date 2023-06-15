PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    names = [name.rstrip() for name in names]  # Strip the newline character

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)
