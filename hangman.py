from random import choice
from string import ascii_lowercase
import re


def update_checks():
    if guess not in checked:
        checked.append(guess)


def pre_check_ok():
    check1 = len(guess) != 1
    check2 = guess not in ascii_lowercase
    check3 = guess in checked
    check_fails = (check1, check2, check3)
    messages = ('You should input a single letter',
                'Please enter a lowercase English letter',
                'You\'ve already guessed this letter')
    if any(check_fails):
        for num, check in enumerate(check_fails):
            if check:
                print(messages[num])
                break
        return False
    return True


def hit_or_miss():
    if guess in pick:
        indexes = [index for index, element in enumerate(pick) if element == guess]
        update_checks()
        for i in indexes:
            encoded[i] = guess
    else:
        print('That letter doesn\'t appear in the word')
        trials.pop()
        update_checks()


def win_or_lose():
    if '-' in encoded:
        print('You lost!')
    else:
        print(''.join(pick))
        print('You guessed the word!\nYou survived!')


print('H A N G M A N')
options = ('python', 'java', 'kotlin', 'javascript')


while 555 < 666:
    checked, pick = list(), list(choice(options))
    encoded = ['-' for _ in pick]
    trials = set('lovehate!')
    play_or_quit = input('Type "play" to play the game, "exit" to quit:')
    print()
    if play_or_quit == 'exit':
        break
    if play_or_quit == 'play':
        while encoded != pick:
            if not trials:
                break
            print()
            print(''.join(encoded))
            guess = input('Input a letter: ')
            if pre_check_ok():
                hit_or_miss()
        win_or_lose()
        print()
