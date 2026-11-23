
from models.computer import Computer


class ComputerDecorator(Computer):

    def __init__(self, computer):
        self._computer = computer

    def get_description(self):
        return self._computer.get_description()

    def get_price(self):
        return self._computer.get_price()

    def get_performance(self):
        return self._computer.get_performance()

