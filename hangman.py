from random import choice


print(' '.join('hangman'.upper()), end='\n\n')
words = ('python', 'java', 'kotlin', 'javascript')
pick = choice(words)
trials = set('helloworld!')
guessed = set()
while trials:
    print(''.join([letter if letter in guessed else '-' for letter in pick]))
    entry = input('Input a letter:')
    (guessed.add(entry), print()) if entry in pick else print('That letter doesn\'t appear in the word\n')
    trials.pop()
print('''Thanks for playing!
We'll see how well you did in the next stage''')
