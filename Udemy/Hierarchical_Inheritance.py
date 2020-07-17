'''class Father:
    def showF(self):
        print("Father Class method")
class Son(Father):
    def showS(self):
        print("Son Class method")
class Daughter(Father):
    def showD(self):
        print("Daughter Class method")
s=Son()
s.showS()
s.showF()
d=Daughter()
d.showF()
d.showD()'''

class Father:
    def __init__(self):
        print('Father class Constructor')
    def showF(self):
        print("Father Class method")
class Son(Father):
    def __init__(self):
        super().__init__()                       #Calling Father Class Constructor
        print('Son class Constructor')
    def showS(self):
        print("Son Class method")
class Daughter(Father):
    def __init__(self):
        super().__init__() 
        print('Daughter  class Constructor')
    def showD(self):
        print("Daughter Class method")
s=Son()
print()
d=Daughter()



