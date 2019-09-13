"""

THIS AN INTERACTIVE DICTIONARY

This program loads .json file into python. It contain the list of words
and their meaning

"""

import json  # allows you to load .json file
from difflib import get_close_matches


data = json.load(open('076 data.json'))  # this loads the json file into python


def translate(word):  # function to return the json file to the user

    word = word.lower()  # check for upper and lower case letters

    # check for non-existing words
    if word in data:
        return data[word]

    # check for Proper Nouns
    elif word.title() in data:
        return data[word.title()]

    # check for acronyms(with all letters in upper case) eg: USA, NATO etc.
    elif word.upper() in data:
        return data[word.upper()]

    # check for similar words
    elif len(get_close_matches(word, data.keys())) > 0:
        word_suggest = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? (Y / N) ").lower()
        if word_suggest == "y":  # prompts the user to confirm similarity check
            return data[get_close_matches(word, data.keys())[0]]

        # if the use says no to the suggested word
        elif word_suggest == "n":
            return "The word you entered does not exist, please double check."

        # if the user input is neither 'y' nor 'n'
        else:
            return 'We did not understand you entry.'

    else:
        return "The word you entered does not exist, please double check."


# prompts the user to enter a word
word = input("Enter a word: ")

output = translate(word)  # cast the function to a variable

# iterating through the list to get the definitions instead of a list of it

if type(output) == list:
    for data in output:
        print(data)

else:
    print(output)


