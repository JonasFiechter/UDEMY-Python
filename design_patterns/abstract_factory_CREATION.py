"""
ABSTRACT FACTORY é um padrão de criação que fornece uma interface para criar famílias de objetos relacionados
ou dependentes sem especificar suas classes concretas. Geralmente ABSTRACT FACTORY conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre FACTORY METHOD E ABSTRACT METHOD é que FACTORY METHOD utiliza herança, enquanto ABSTRACT
METHOD usa a composição.

Princípio: programe para interfaces, não para implementações
"""

import random
from abc import ABC, abstractmethod
from random import choice


class LuxuryVehicle(ABC):
    @abstractmethod
    def get_client(self):
        pass


class PopularVehicle(ABC):
    @abstractmethod
    def get_client(self):
        pass


class LuxuryCar(LuxuryVehicle):
    def get_client(self):
        print(f'{self.__class__.__name__} is getting a client')


class PopularCar(PopularVehicle):
    def get_client(self):
        print(f'{self.__class__.__name__} car is getting a client')


class Bike(PopularVehicle):
    def get_client(self):
        print(f'the {self.__class__.__name__} is getting a client')


class VehicleFactory(ABC):
    def __init__(self, type_):
        self.car = self.get_car(type_)

    @staticmethod
    @abstractmethod
    def get_car(type_: str):
        pass

    def get_client(self):
        self.car.get_client()


class NorthZoneFactory(VehicleFactory):
    @staticmethod
    def get_car(type_: str):
        if type_ == 'luxury':
            return HighGrade()
        if type_ == 'popular':
            return PopularGrade()
        if type_ == 'bike':
            return Bike()


class SouthZoneFactory(VehicleFactory):
    @staticmethod
    def get_car(type_: str):
        if type_ == 'popular':
            return PopularGrade()


if __name__ == '__main__':
    available_vehicles_north = ['luxury', 'popular', 'bike']
    available_vehicles_south = ['popular']
    for i in range(5):
        car = NorthZoneFactory(random.choice(available_vehicles_north))
        car.get_client()

    for i in range(5):
        car = SouthZoneFactory(random.choice(available_vehicles_south))
        car.get_client()
