#  Word Game
from time import *


def print_word(word_entry, i_got_it_list, tried_word):
    tried_word = ''
    for l in word_entry:
        sleep(0.4)
        if l == ' ':
            tried_word += ' '
            print('-', end='')
        elif l in i_got_it_list:
            tried_word += l
            print(l, end='')
        else:
            tried_word += '*'
            print('*', end='')
    return tried_word


def main():
    print('** WORD GAME **')
    run = True
    i_got_it_list = ''
    missed_list = ''
    tried_word = ''
    word_entry = input('\nCall your mates, ask then to close their eyes and'
                       ' Input a secret word: ').upper()

    for i in range(50):
        print('*')

    word_tip = input('Input any tip: ')

    for i in range(50):
        print('*')
    print()
    tries = 4 + len(word_entry) // 1.5

    print(f'the tip is: {word_tip}')

    while run:

        if len(missed_list) > 0:
            print(f'\n MISSED LIST --> {missed_list}')

        print()
        print(f'\nYou got {int(tries)} tries left...')
        letter_entry = input('\nInput any letter: ').upper()

        if len(letter_entry) > 1:
            print(f'\nThis is not a letter !!!')
            continue

        if letter_entry in missed_list or letter_entry in i_got_it_list:
            print('\nYou already tried this one...')
            continue

        elif letter_entry not in word_entry:
            missed_list += letter_entry
            missed_list += ' '
            print(f'\nwrong choice {missed_list}')
            print(f'\nThe tip is: {word_tip}')

        else:
            print('\nYou got it!')
            i_got_it_list += letter_entry

        print('----->', end=' ')
        tried_word = print_word(word_entry, i_got_it_list, tried_word)
        print()

        if str(tried_word) == str(word_entry):
            print('\n** YOU WIN **')
            break

        tries -= 1

        if tries <= 0:
            print(f'\n** YOU LOSE **'
                  f'\nThe word was: {word_entry}')
            break


if __name__ == '__main__':
    main()
