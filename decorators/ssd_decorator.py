
from decorators.computer_decorator import ComputerDecorator


class SSDDecorator(ComputerDecorator):

    def __init__(self, computer, component):
        super().__init__(computer)
        self.component = component

    def get_description(self):
        return (
            f"{self._computer.get_description()} "
            f"+ {self.component.name}"
        )

    def get_price(self):
        return self._computer.get_price() + self.component.price

    def get_performance(self):
        return (
            self._computer.get_performance()
            + self.component.performance_points
        )
