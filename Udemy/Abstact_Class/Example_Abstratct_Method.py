from abc import ABC,abstractmethod
class DefenceForces(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print('gun=Ak47')
class Army(DefenceForces):
    def area(self):
        print('Army Area=Land')
class Navy(DefenceForces):
    def area(self):
        print('Navy Area=ocean')
class Airforce(DefenceForces):
    def area(self):
        print('Airforce Area=Sky')
a=Army()
n=Navy()
air=Airforce()
a.gun()
a.area()
air.gun()
air.area()
n.gun()
n.area()
