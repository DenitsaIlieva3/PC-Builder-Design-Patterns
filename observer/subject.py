
class Subject:

    def __init__(self):
        self._observers = []

#Създаваме празен списък _observers, в който ще съхраняваме всички обекти, които наблюдават промените.
#Защо _observers започва с _? Това е конвенция в Python, която показва, че атрибутът е предназначен за вътрешна употреба в класа.
    
    def attach(self, observer): #Добавя нов наблюдател в списъка.
        self._observers.append(observer)

    def detach(self, observer): #Премахва наблюдател от списъка.
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, component, old_price, new_price):
        for observer in self._observers:
            observer.update(component, old_price, new_price)
#Обхожда всички регистрирани наблюдатели.
#Извиква техния update().
#Изпраща им информация за компонента и промяната в цената.