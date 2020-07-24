from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
class Child(Father):
    def disp(self):
        print('child class')
        print('defining abstract method')
c=Child()
c.disp()