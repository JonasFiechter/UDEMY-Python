lista = [
    ['p1', 13],
    ['p4', 6],
    ['p3', 7],
    ['p2', 8]
]

def list(item):
    return item[0]

lista.sort(key=list)
print(lista)

##############################

lista = [
    ['p1', 13],
    ['p4', 6],
    ['p3', 7],
    ['p2', 8]
]

lista.sort(key=lambda item: item[0])
print(lista)

##############################

lista = [
    ['p1', 13],
    ['p4', 6],
    ['p3', 7],
    ['p2', 8]
]

print(sorted(lista, key=lambda i: i[0]))