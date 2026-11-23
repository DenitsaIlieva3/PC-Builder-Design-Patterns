
from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract interface for objects that observe price changes.
    """

    @abstractmethod
    def update(self, component, old_price, new_price):
        pass

#Това е абстрактният клас Observer. 
#Той определя какво трябва да може да прави всеки обект, който наблюдава промените в цените.