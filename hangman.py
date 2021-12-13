from random import choice
from string import ascii_lowercase


def entry_fails():
    if len(entry) != 1:
        return 'You should input a single letter\n'
    if entry not in ascii_lowercase:
        return 'Please enter a lowercase English letter\n'
    if entry in guessed:
        return 'You\'ve already guessed this letter\n'
    return False


print(' '.join('hangman'.upper()), end='\n\n')
words = ('python', 'java', 'kotlin', 'javascript')
pick = choice(words)
trials, guessed = set('helloworld!'), set()

while trials and not guessed.issuperset(set(pick)):
    print(''.join([letter if letter in guessed else '-' for letter in pick]))
    entry = input('Input a letter:')
    
    if entry_fails():
        print(entry_fails())
    elif entry in pick:
        guessed.add(entry)
        if not guessed.issuperset(set(pick)):
            print()
    else:
        if not entry_fails():
            guessed.add(entry)
        trials.pop()
        print('That letter doesn\'t appear in the word{slash_n}'.format(slash_n='\n' if trials else ''))

print(f'You guessed the word {pick}!\nYou survived!' if trials else 'You lost!')
