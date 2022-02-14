class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    def __getitem__(self, index):
        try:
            return self.__items[index]
        except:
            raise ValueError('List index out of range')

    def __delitem__(self, index):
        try:
            del self.__items[index]
        except:
            raise ValueError('List index out of range')

    def __setitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)
        else:
            self.__items[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__} {self.__items}'


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Jospe')

    lista[3] = 'Johnson'
    print(lista)