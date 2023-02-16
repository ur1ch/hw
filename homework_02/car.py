"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.engine import Engine
from homework_02.base import Vehicle


class Car(Vehicle):
    def set_engine(self, Engine):
        self.engine = Engine