"""
Factory Method é um padrão de criação que permite definir uma interface para criar objetos, mas deixa as subclasses
decidirem quais objetos criar. O FACTORY METHOD permite adiar a instanciação para as subclasses, garantindo o baixo
acoplamento entre classes.
"""

import random
from abc import ABC, abstractmethod
from random import choice


class Vehicle(ABC):
    @abstractmethod
    def get_client(self):
        pass


class HighGrade(Vehicle):
    def get_client(self):
        print(f'{self.__class__.__name__} is getting a client')


class PopularGrade(Vehicle):
    def get_client(self):
        print(f'{self.__class__.__name__} car is getting a client')


class Bike(Vehicle):
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