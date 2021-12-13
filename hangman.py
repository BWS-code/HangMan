from random import choice


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
pick = choice(words)
print(''.join([e if i < 3 else '-' for i, e in enumerate(pick)]))
print('You lost!' if pick != input('Guess the word:') else 'You survived!')
