"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        print('INIT')


a = A()