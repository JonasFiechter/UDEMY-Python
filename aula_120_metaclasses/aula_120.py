class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        print(namespace)

class A:
    def fala(self):
        self.b_fala()


class B(A):
    pass
