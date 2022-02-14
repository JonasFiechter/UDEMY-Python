l1 = [1, 2, 3, 4, 5, 6, 7]

ex1 = [variavel for variavel in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

l3 = '1092jdiajodma01923012kmkmadlkmasd'
ex5 = [l3[i: i + 5] for i in range(0, len(l3), 5)]

print(ex5)