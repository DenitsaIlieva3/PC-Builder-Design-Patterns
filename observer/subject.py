
class Subject:

    def __init__(self):
        self._observers = []

    
    def attach(self, observer): 
        self._observers.append(observer)

    def detach(self, observer): 
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, component, old_price, new_price):
        for observer in self._observers:
            observer.update(component, old_price, new_price)
