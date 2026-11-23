
from decorators.computer_decorator import ComputerDecorator


class RAMDecorator(ComputerDecorator):

    def __init__(self, computer, component):
        super().__init__(computer) #Извиква конструктора на родителския клас ComputerDecorator
        self.component = component #Запазваме конкретния RAM компонент, който добавяме.

    def get_description(self):
        return (
            f"{self._computer.get_description()} "
            f"+ {self.component.name}"
        )

    def get_price(self):
        return self._computer.get_price() + self.component.price #Вече не връщаме само базовата цена. Добавяме цената на RAM паметта.

    def get_performance(self):
        return (
            self._computer.get_performance()
            + self.component.performance_points 
        )
