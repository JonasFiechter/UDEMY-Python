# Test class for e while

import random
import time

var_01 = input(f'Insert any number to generate: ')
var_02 = input(f'Insert another number to generate: ')

var_01 = int(var_01)
var_02 = int(var_02)


def random_coordinates():
    t = time.time()
    global var_01
    global var_02
    count_01 = 1
    run = True

    while run:
        count_02 = 0
        print(f'({var_01:0>10d},{var_02:0>10d})')
        print(f'{count_01:0>5d} {count_02:0>5d}')
        var_01 += random.randrange(var_02 + var_01)
        count_01 += 1

        if var_01 > 9999999999 or var_02 > 9999999999:
            print(f'LAST_01 = ({var_01:0>10d},{var_02:0>10d})')
            var_01 = 1
            var_02 = 1

        while run:
            print(f'({var_01:0>10d},{var_02:0>10d})')
            print(f'{count_01:0>5d} {count_02:0>5d}')
            var_02 += random.randrange(var_01 + var_02)
            count_02 += 1

            if count_02 == 2:
                break

            if var_01 > 9999999999 or var_02 > 9999999999:
                print(f'LAST_02 = ({var_01:0>10d},{var_02:0>10d})')
                var_01 = 1
                var_02 = 1
                break

            if var_01 == 40000 or var_02 == 40000:
                t2 = time.time() - t
                print(f'Process time: {t2:.2f} seconds')
                run = False
                break


random_coordinates()