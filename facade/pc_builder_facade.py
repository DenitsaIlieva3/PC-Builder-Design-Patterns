#Façade Pattern осигурява опростен интерфейс към по-сложна система от класове. 
# Той скрива вътрешната сложност и улеснява взаимодействието между потребителя 
# и отделните компоненти на системата

from configurations.base_configurations import OfficePC, GamingPC, ServerPC

from models.component import ComponentProduct

from decorators.ram_decorator import RAMDecorator
from decorators.ssd_decorator import SSDDecorator
from decorators.gpu_decorator import GPUDecorator

from observer.price_catalog import PriceCatalog
from observer.price_history_observer import PriceHistoryObserver


class PCBuilderFacade:

    def __init__(self):
        self.computer = None
        self._added_components = set()

        self.price_catalog = PriceCatalog() #Създадохме каталог за цените.
        self.price_history_observer = PriceHistoryObserver() #Създадохме наблюдател за историята.

        self.price_catalog.attach(self.price_history_observer) #Регистрирахме наблюдателя чрез attach().

        self._initialize_components() #Извикахме _initialize_components(), който по-късно ще добави наличните компоненти в каталога.


    def _initialize_components(self):

        components = [
            ComponentProduct("Kingston Fury 32GB", "RAM", 80.00, 15),
            ComponentProduct("Samsung 990 PRO 1TB", "SSD", 100.00, 10),
            ComponentProduct("NVIDIA RTX 4070", "GPU", 450.00, 40)
        ]

        for component in components:
            self.price_catalog.add_component(component)


    def create_computer(self, computer_type):

        if computer_type == "office":
            self.computer = OfficePC()

        elif computer_type == "gaming":
            self.computer = GamingPC()

        elif computer_type == "server":
            self.computer = ServerPC()

        else:
            raise ValueError("Invalid computer type!")

        self._added_components.clear()

        return self.computer

    
    def add_component(self, component_name):

        if self.computer is None:
            raise ValueError("Create a computer first!")

        component = self.price_catalog.get_component(component_name)

        if component is None:
            raise ValueError("Component not found!")

        if component_name in self._added_components:
            raise ValueError("This component has already been added!")

        if component.category == "RAM":
            self.computer = RAMDecorator(self.computer, component)

        elif component.category == "SSD":
            self.computer = SSDDecorator(self.computer, component)

        elif component.category == "GPU":
            self.computer = GPUDecorator(self.computer, component)

        else:
            raise ValueError("Unsupported component category!")
        
        self._added_components.add(component_name)

        return self.computer


    def get_configuration(self):

        if self.computer is None:
            raise ValueError("No computer configuration selected!")

        return {
            "description": self.computer.get_description(),
            "price": self.computer.get_price(),
            "performance": self.computer.get_performance()
        }


    def update_component_price(self, component_name, new_price):

        self.price_catalog.update_price(component_name, new_price)


    def get_price_history(self):

        return self.price_history_observer.get_history()
    
    def get_available_components(self):
        return self.price_catalog.get_all_components()
