"""
Pilhas e filas
Pilha(stack) - LIFO Last in First out
Fila(Queue) - FIFO First in First out
"""

from collections import deque
from time import sleep

fila = deque()
fila.append('1')
fila.append('2')
fila.append('test')

print(f'Saiu: {fila.popleft()}')
for i in fila:
    print(i, end=' ')

fila = deque(maxlen=10)

for i in range(100):
    fila.append(i)
    sleep(0.5)
    print(fila)