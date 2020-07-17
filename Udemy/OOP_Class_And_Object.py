'''class Myclass:
    def show(self):
        print('I am method')
x=Myclass()
x.show()'''

'''class Mobile():
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print('Medel:',self.model)
realme=Mobile()
realme.show_model()
print(realme.model)
#Reassign value
realme.model='RealMe Pro2'
print(realme.model)
realme.show_model()

class Mobile():
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        price=1000 #variable assigned by me
        print('Medel:',self.model,'Price=',price)
realme=Mobile()
realme.show_model()
print(realme.model)
#Reassign value
realme.model='RealMe Pro2'
print(realme.model)
realme.show_model()

#Argument:
class Mobile():
    def __init__(self,m):
        self.model=m
    def show_model(self,p):
        price=p
        print('Medel:',self.model,'Price=',p)
realme=Mobile('RealMe X')
realme.show_model(1000)'''

class Mobile():
    def __init__(self,m):
        self.model=m
    def show_model(self,p):
        price=p
        print('Medel:',self.model,'Price=',p)
realme=Mobile('RealMe X')
realme.show_model(1000)
print(id(realme))
print()
redmi=m=Mobile('RedMi 7s')
redmi.show_model(2000)
print(id(redmi))
print()
geek=Mobile('Python')
geek.show_model(500)
print(id(geek))