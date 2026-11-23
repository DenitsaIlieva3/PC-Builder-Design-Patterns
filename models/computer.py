
from abc import ABC, abstractmethod
#ABC – позволява ни да създаваме абстрактни базови класове.

#abstractmethod – обозначава метод, който задължително трябва да бъде реализиран от наследяващите класове.


class Computer(ABC):
    """
    Abstract base class for all computer configurations.
    """

    @abstractmethod
    def get_description(self): #Връща описание на конфигурацията
        pass

    @abstractmethod
    def get_price(self):#Връща нейната цена
        pass

    @abstractmethod
    def get_performance(self):#Връща производителността ѝ
        pass
