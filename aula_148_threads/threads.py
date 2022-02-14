from time import sleep
from threading import Thread
from threading import Lock

# print('Hello')
#
# for i in range(10):
#     sleep(0.5)
#     print(i, end=' ')
#
# print('World')

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()
while t1.is_alive():
    print(f'Waiting for thread "t1"')
    sleep(1)


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t2 = Thread(target=vai_demorar, args=('ok, thread 2', 5))
t2.start()
while t2.is_alive():
    print(f'Waiting for thread "t2"')
    sleep(1)