
from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract interface for objects that observe price changes.
    """

    @abstractmethod
    def update(self, component, old_price, new_price):
        pass

