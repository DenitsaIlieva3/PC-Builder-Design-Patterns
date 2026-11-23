
class ComponentProduct:

    def __init__(self, name, category, price, performance_points):#Това е специален метод в Python, който се изпълнява при създаване на нов обект.
        self.name = name
        self.category = category
        self.price = price
        self.performance_points = performance_points

    def get_details(self):
        return (
            f"{self.name} | "
            f"Category: {self.category} | "
            f"Price: {self.price:.2f} EUR | "
            f"Performance: {self.performance_points} points"
        )
