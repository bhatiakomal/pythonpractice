'''class Father:
    def showF(self):
        print("Father Class method")
class Mother:
    def showM(self):
        print("Mother Class method")
class Son(Father,Mother):
    def showS(self):
        print("Son Class method")
s=Son()
s.showS()
s.showF()
s.showM()'''

class Father:
    def __init__(self):
        super().__init__()  # Calling parent Class constructor
        print('Father class constructor')
    def showF(self):
        print("Father Class method")
class Mother:
    def __init__(self):
        super().__init__()  # Calling parent Class constructor
        print('Mother class constructor')
    def showM(self):
        print("Mother Class method")
class Son(Father,Mother):
    def __init__(self):
        super().__init__()            #Calling parent Class constructor
        print('Son class constructor')
    def showS(self):
        print("Son Class method")
s=Son()
