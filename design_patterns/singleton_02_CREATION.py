def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    return get_class 

@singleton
class AppSettings:
    def __init__(self):
        self.theme = 'Anything'
        self.color = 'red'

@singleton
class Teste:
    def __init__(self):
        pass


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    print(as1)
    print(as2)