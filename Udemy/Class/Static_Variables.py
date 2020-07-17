'''class Mobile:
    fp="Yes" #Class variable
    @classmethod
    def is_fp(cls): #Class method
        print(cls.fp) # #Accessing class variable inside class
realme=Mobile()
print(Mobile.fp)'''  #Accessing class variable outside class

class Mobile:
    fp="yes"  #Class variable
    def __init__(self):
        self.model='RealMe X'#Instance variable
    def show_model(self):   #Instance Method
        print(self.model)#Acccesing instance varible instance method
    @classmethod
    def is_fp(cls):     #Class Method
        print("Finger print",cls.fp) #Accessing class variable inside class
realme=Mobile()
realme.show_model()
Mobile.is_fp()

Mobile.fp='No'
Mobile.is_fp()
