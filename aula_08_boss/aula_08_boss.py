"""

* Create variables for name(str), age(int),
* height(float) and weight(float) from a person
* create a variable with actual year
* get the birth year based on the present year and person's age
* show a text with the values on screen using F-Strings

"""

name = 'Boris'
age = 24
height = 1.65
weight = 67.5
actual_year = 2021
birth_year = actual_year - age

print('{name} is {age} years old, weighs {weight}, and measures {height}.'.format(name=name, age=age, weight=weight, height=height))
print("{name}'s IMC is: {imc:.2f}.".format(name=name, imc=(weight / (height ** 2))))
print("{name} was born at: {birth_year}.".format(name=name, birth_year=birth_year))