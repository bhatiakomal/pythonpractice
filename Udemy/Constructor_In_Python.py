'''class mobile:
    def __init__(self):
        print("This is example of constructor")
object_instance=mobile()

print('Constructor without Argument:')
class mobile:
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print('Model:',self.model)
realme=mobile()
realme.show_model()'''

print('Constructor  Argument')
class mobile:
    def __init__(self,m,v=80):
        self.model= m
        self.volume=v
    def show_model(self,p):
        price=p
        print('Model:',self.model,'and price:',price)
        print('volume:',self.volume)
#Passing argument to constructor
realme=mobile('RealMe X',90)#High priority is given to this ie 90 (parameter)
#Accessing method from outside class
realme.show_model(1000)
print()
redmi=mobile('Redme 7s pro',70)
redmi.show_model(2000)