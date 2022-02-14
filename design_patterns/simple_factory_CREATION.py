"""
Na POO, o termo factory refere-se a uma classe ou método que é responsável por criar objetos
Simple Factory
Alguns padrões de projeto não consideram simple Factory como um.
"""
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


class VehicleFactory:
    def __init__(self, type):
        self.carro = self.get_car(type)

    @staticmethod
    def get_car(type: str):
        if type == 'luxury':
            return HighGrade()
        if type == 'popular':
            return PopularGrade()

    def get_client(self):
        self.carro.get_client()


if __name__ == '__main__':
    available_cars = ['luxury', 'popular']
    car = VehicleFactory.get_car(choice(available_cars))
    car.get_client()
    car2 = VehicleFactory.get_car('luxury')
    car2.get_client()
