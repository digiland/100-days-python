import pandas

# read csv file using pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    user = input("Enter a word: ").upper()
    try:
        code_list = [alphabet[letter] for letter in user]
    except KeyError:
        print("Invalid word")
        generate()
    else:
        print(code_list)


generate()
