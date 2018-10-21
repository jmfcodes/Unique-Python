"""a hangman-style game where no one is actually hanged

wordfile.txt modified from source:
http://www.ef.com/english-resources/english-vocabulary/top-3000-words/
"""

import random

# varify length input
def check_length(wordlength):
    if (wordlength == ''):
        pass
    else:
        try:
            wordlength = int(wordlength)
        except:
            print('Oops! I do not know any words that length. Let\'s play a random game!')
            wordlength = ''
    return wordlength

# picks from wordlist.txt based on length input (if any)
def pick_word(wordlength):
    wordfile = [line.strip() for line in open('wordslist.txt')]
    randomword = random.choice(wordfile).upper()
    if wordlength == '':
        return randomword

    # determine validity of length input and return appropriate choice
    sortedwords = sorted(wordfile, key=len)
    if ((len(sortedwords[-1]) < wordlength) or (wordlength < 2)):
        print('Oops! I do not know any words that length. Let\'s play a random game!')
    else:
        while len(randomword) != int(wordlength):
            randomword = random.choice(wordfile).upper()
    return randomword


def check(answer, guesses, guess):
    status = ''
    matches = 0
    for letter in answer:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == guess:
            matches += 1
    if matches > 1:
        print('Yes! The word contains {} {}\'s.'.format(matches,guess))
    elif matches == 1:
        print('Yes! The word contains the letter {}.'.format(guess))
    else:
        print('Sorry, no {}\'s.'.format(guess))
    return status

def main():
    print('\nWelcome to non-violent Hangman! Let\'s begin!')
    wordlength = check_length(input('\nChoose your word length, or leave blank for a random choice: '))
    answer = pick_word(wordlength)
    choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guesses = []
    guessed = False
    print('This word contains {} letters.'.format(len(answer)))
    while not guessed:
        text = 'Enter 1 letter or {}-letter word.\nYour choices are: {}:  '.format(len(answer), choices)
        guess = input(text)
        guess = guess.upper()
        choices = choices.replace(guess, '-')
        if guess in guesses:
            print('You already guessed {}.'.format(guess))
        elif not guess.isalpha():
            print('Please choose an alphabetic character.')
        elif len(guess) == len(answer):
            guesses.append(guess)
            if guess == answer:
                guessed = True
            else:
                print('Sorry, that is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(answer, guesses, guess)
            if result == answer:
                guessed = True
            else:
                print('\n{}'.format(result))
        else:
            print('Sorry! Try again!')
    print('Nice job! The word is {}. You won in {} tries. \nThanks for playing! '.format(answer, len(guesses)))
main()

# future iterations: repeat the game as often as the user wishes
