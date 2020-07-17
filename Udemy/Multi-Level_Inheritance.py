'''class Father:
    def showF(self):
        print("Father Class method")
class SonS(Father):
    def showS(self):
        print("Son Class method")
class GrandSon(SonS):
    def showG(self):
        print("GrandSon Class method")
g=GrandSon()
g.showG()
g.showS()
g.showF()'''

class Father:
    def __init__(self):
        print('Father Class Constructor')
    def showF(self):
        print("Father Class method")
class SonS(Father):
    def __init__(self):
        super().__init__()                    #Calling Father Class Constructor
        print('Son Class Constructor')
    def showS(self):
        print("Son Class method")
class GrandSon(SonS):
    def __init__(self):
        super().__init__()                   #Calling Son class constructor
        print('GrandSon Class Constructor')
    def showG(self):
        print("GrandSon Class method")
g=GrandSon()
