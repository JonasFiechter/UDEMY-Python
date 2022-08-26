# Setter => Function that configures a value (=) (Depends on having a Getter declared)
# Getter => Function that returns a value (.)

class Person:
    def __init__(self):
        self._name = 'Initial'

    @property # Getter
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name): # Setter: change the instance atribute value
        print('inside setter')
        self._name = new_name

p1 = Person()
print(p1.name)
p1.name = 'Declaring instance name with this will call the setter method'
print(p1.name)