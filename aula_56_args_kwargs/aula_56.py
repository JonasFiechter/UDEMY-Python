#
# *args
# **kwargs

def func(*args):
    print(args)

list = [1, 2, 3, 4]

func(*list)

def func_02(*args, **kwargs):
    print(args, kwargs['name'])

func_02(*list, name='Lover')

def func_03(**kwargs):
    print(kwargs.get('age'))

func_03(age=10)