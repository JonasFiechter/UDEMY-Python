# for / while
#
# 0 10
# 1 9
# 2 8
# 3 7
# 4 6
# 5 5
# 6 4
# 7 3
# 8 2

a = 0
b = 10

for n in range(9):
    print(f'{a} {b}')
    a += 1
    b -= 1

a = 0
b = 10

print('')

while b > 1:
    print(f'{a} {b}')
    a += 1
    b -= 1

print('')

for n, a in enumerate(range(10, 1, -1)):
    print(f'{n} {a}')