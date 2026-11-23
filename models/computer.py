
from abc import ABC, abstractmethod


class Computer(ABC):
    """
    Abstract base class for all computer configurations.
    """

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_performance(self):
        pass
