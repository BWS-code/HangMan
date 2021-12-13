from random import choice


print(' '.join('hangman'.upper()), end='\n\n')
words = ('python', 'java', 'kotlin', 'javascript')
pick = choice(words)
trials = set('helloworld!')
guessed = set()
while trials and set(pick) != guessed:
    print(''.join([letter if letter in guessed else '-' for letter in pick]))
    entry = input('Input a letter:')
    (guessed.add(entry), print()) if entry in set(pick) - guessed \
        else \
    (trials.pop(), print('No improvements{slash_n}'.format(slash_n='\n' if trials else ''))) if entry in guessed \
        else \
    (trials.pop(), print('That letter doesn\'t appear in the word{slash_n}'.format(slash_n='\n' if trials else '')))
print(f'{pick}\nYou guessed the word!\nYou survived!' if trials else 'You lost!')
