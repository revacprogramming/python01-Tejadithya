# Strings

string = input('please enter a word: ')
character = input('please enter a letter: ')

def count(string, character):
    index = 0
    for letter in string:
        if letter == character:
            index = index + 1
    return index

answer = count(string, character)
print('the letter you entered is found', answer, 'times within the word you entered')