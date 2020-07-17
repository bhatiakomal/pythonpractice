class Mobile:
    def __init__(self):
        self.model='RealMe X'#Instance variable
    def show_model(self):
        print(self.model)#Acccesing instance varible instance method
realme=Mobile()
redmi=Mobile( )
geeks=Mobile( )

print(realme.model)
print(redmi.model)
print(geeks.model)
print()
redmi.model="Redmi 7s"
print(realme.model)
print(redmi.model)
print(geeks.model)