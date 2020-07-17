'''class Mobile:
    def show_model(self):  #Isntance method with parameter
        print("RealMe X")   #instance variable and parameter
realme=Mobile()
realme.show_model()'''

class Mobile:
    def __init__(self):
        self.model='RealMe X' #'RealMe X'  is instance variable
    def show_model(self,p):  #Isntance method with parameter
        self.price=p      #instance variable and parameter
        print("Model",self.model,"Price",self.price)
realme=Mobile()
realme.show_model(1000)

