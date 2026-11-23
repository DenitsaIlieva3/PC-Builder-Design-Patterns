
from observer.observer import Observer


class PriceHistoryObserver(Observer): 

    def __init__(self):
        self._history = [] 

    def update(self, component, old_price, new_price):

        change = { 
            "component": component.name,
            "old_price": old_price,
            "new_price": new_price
        }

        self._history.append(change) 

        print(
            f"Price changed: {component.name} | "
            f"{old_price:.2f} EUR -> {new_price:.2f} EUR"
        )

    def get_history(self):
        return self._history
 