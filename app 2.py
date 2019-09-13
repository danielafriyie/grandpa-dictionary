'''

This progam loads the .json file into python. It contain the list of words
and their meaning

'''

import json
from difflib import get_close_matches

data = json.load(open('076 data.json')) # this loads the json file into python

def translate(word): # function to return the json file to the user
    return data[word]

'''

check for errors that may arise, eg: if the word the user entered is not in the list of words
or is not a word at all or at least not an English word

'''

try: # check if the user input is in the list of words
    word = input("Enter a word: ") # prompts the user to enter a word
    word2 = word.lower() # check for upper and lower case letters
    print(translate(word))

except TypeError: # check for type errors
    print("The word you entered does not exist, please double check.")

except: # check if the user input is in the list of words or if it's a word at all
    print("The word you entered does not exist, please double check.")

