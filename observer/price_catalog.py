
from observer.subject import Subject


class PriceCatalog(Subject):

    def __init__(self):
        super().__init__() #извикваме конструктора на родителския клас, за да се създаде списъкът с наблюдатели.
        self._components = {} #създаваме речник, в който ще съхраняваме компонентите.

    def add_component(self, component): #добавя компонент в каталога.
        self._components[component.name] = component

    def get_component(self, component_name):
        return self._components.get(component_name)

    def get_all_components(self):
        return self._components.copy()

    def update_price(self, component_name, new_price): #променя цената на избран компонент и уведомява наблюдателите.

        if component_name not in self._components:
            print("Component not found!")
            return

        component = self._components[component_name]

        old_price = component.price
        component.price = new_price

        self.notify(component, old_price, new_price)
