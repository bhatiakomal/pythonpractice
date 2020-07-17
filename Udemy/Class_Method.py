print('Class method without parameter:')
#Class method without parameter:
class Mobile():
    @classmethod     #Decorator
    def show_model(cls):   #Class method
        print("RealMe X")
realme=Mobile()
Mobile.show_model()      #Calling Class Method

print()
class Mobile():
    fp="Yes"         #class Variable
    @classmethod     #Decorator
    def show_model(cls):   #Class method
        print('fingerprint',cls.fp)
realme=Mobile()
Mobile.show_model()

print()
#Class method with parameter:
print("Class method with parameter:")
class Mobile():
    @classmethod     #Decorator
    def show_model(cls,r):#Class method
        cls.ram=r
        print("RealMe X")
        print("RAM:",cls.ram)
realme=Mobile()
Mobile.show_model('4GB')


