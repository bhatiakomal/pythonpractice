#Accessor Method Or Getter Method:
'''class Mobile():
    def __init__(self):
        self.model="RealMe"
    def get_model(self):
        return self.model
realme=Mobile()
m=realme.get_model()
print(m)

#Mutator Method Or Setter Method:
class Mobile():
    def __init__(self):
        self.model="RealMe"
    def set_model(self):
        self.model='RealMe X2'
realme=Mobile()
print(realme.model)
realme.set_model()
print(realme.model)'''

class Mobile():
    def set_model(self,m):
        self.model=m
realme=Mobile()
realme.set_model("RealMe X Pro")
print(realme.model)
