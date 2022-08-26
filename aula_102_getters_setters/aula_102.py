class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.tag = 'Cloathing'

    def discount(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title()

    # getter
    @property
    def price(self):
        return self._price

    # setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))

        self._price = value

p1 = Product('shirt', 50)
p1.discount(15)
print(p1.name, f'R${p1.price:.2f}')

p2 = Product('mug', 'R$15')
p2.discount(10)
print(f'{p2.price:.2f} {p2.name}')

print(p1.tag)