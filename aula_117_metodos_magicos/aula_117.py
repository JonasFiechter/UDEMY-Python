"""
https://rszalski.github.io/magicmethods/
"""

# This method inherits from the python base class 
class A:
    def __new__(cls, *args, **kwargs): # Class constructor
        return object.__new__(cls) # same as super().__new__(cls)

    def __init__(self):
        print('INIT')


a = A()

class B:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_already_exists'): # This will create the class atribute for the first time
            cls._already_exists = super().__new__(cls) # the attr is the object of class itself
        
        return cls._already_exists 

    def __init__(self):
        print(f'Inside init {__class__.__name__}')

b = B()
b1 = B()
b2 = B()
print(b1 == b2)
print(len(b1))