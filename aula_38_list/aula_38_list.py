import time

# Fatiamento
# append, insert, pop, del, clear, extend, +
# min, max
# range

secret_word = input('Place any word to be secret: ').upper()
discovered_letter = []
missed_letter = []
discovered = False
chance = int(len(secret_word) / 2) + 4

while not discovered:
    t = time.clock()
    discovered_word = ''
    try_letter = input(f'\nTries left = {chance}'
                       f'\nPlace any letter to fill the mysterious word: ').upper()
    if len(try_letter) > 1:
        input('This is not only a letter, try again. press ENTER to continue...')
        continue
    elif try_letter in secret_word:
        discovered_letter.append(try_letter)
    else:
        input('\nOoops, this letter does not match with the mysterious word, try again...'
              '\npress ENTER to continue...')
        missed_letter.append(try_letter)

    if try_letter in discovered_letter and discovered_letter.count(try_letter) > 1:
        input(f'\nYou already discovered letter "{try_letter.upper()}", '
              f'try another one! press ENTER to continue...')
        discovered_letter.pop(-1)
        continue
    if try_letter in missed_letter:
        input(f'\nYou already missed letter "{try_letter}"')
        continue

    if try_letter in secret_word and not discovered_letter.count(try_letter) > 1:
        print('\nWOW that matches!')

    chance -= 1

    for n, letter in enumerate(secret_word):
        if letter in discovered_letter:
            discovered_word += letter
        else:
            discovered_word += '*'
    print(f'\nLetters discovered: {str(discovered_letter)}')
    print(f'Word: {discovered_word}')

    if discovered_word == secret_word:
        print('\nCongratulations you have discovered the secret word!')
        discovered = True
    elif chance == 0:
        print(f'\nGame over'
              f'\nThe word was: {secret_word}')
        break