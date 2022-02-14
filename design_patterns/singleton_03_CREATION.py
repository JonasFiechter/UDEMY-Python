"""
__call__ -> retorna a função de chamada com parentesis ()
"""
# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('Inside CALL')
#         return super().__call__(*args, **kwargs)

# class People(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('inside NEW')
#         return super().__new__(cls)

#     def __init__(self, name):
#         print('inside INIT')
#         self.name = name
    
#     def __call__(self):
#         print(f'inside CALL inside class {self.__class__.__name__}')


# def main():
#     entry_name = str(input('Place any name: '))
#     var_01 = People(entry_name)
#     var_01()
#     print(var_01.name)


# if __name__ == '__main__':
#     main()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]

class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.color = 'red'
        self.font_size = '18px'


if __name__ == '__main__':
    v1 = AppSettings()
    v1.color = 'new_blue'
    v2 = AppSettings()
    print(f'O parametro "color" da instancia v1 é: {v1.color}'
          f'\nO parametro "color" da instancia v2 é: {v2.color}')