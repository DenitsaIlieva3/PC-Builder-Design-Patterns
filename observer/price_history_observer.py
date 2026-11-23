
from observer.observer import Observer


class PriceHistoryObserver(Observer): #наследява абстрактния клас Observer

    def __init__(self):
        self._history = [] #създава празен списък за историята на цените.

    def update(self, component, old_price, new_price):#изпълнява се автоматично, когато PriceCatalog изпрати уведомление.

        change = { #създава запис с името на компонента, старата и новата цена.
            "component": component.name,
            "old_price": old_price,
            "new_price": new_price
        }

        self._history.append(change) #добавя промяната в историята.

        print(
            f"Price changed: {component.name} | "
            f"{old_price:.2f} EUR -> {new_price:.2f} EUR"
        )

    def get_history(self):#позволява да получим всички записани промени.
        return self._history
 #PriceHistoryObserver наследява Observer, защото представлява конкретен наблюдател и трябва да реализира метода update(). 
 #Subject има различна отговорност – управлява списъка с наблюдатели и изпраща уведомления.