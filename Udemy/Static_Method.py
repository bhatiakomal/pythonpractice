#Static method without parameter:
print('Static method without parameter:')
class Mobile():
    @staticmethod         #Decorartor
    def show_model():     #Static Method
        print("Vivo")
vivo=Mobile()
vivo.show_model()       #Calling Static Method

print()
class Mobile():
    fp='Yes'
    @staticmethod         #Decorartor
    def show_model():     #Static Method
        print("Fingerprint:",Mobile.fp)
vivo=Mobile()
vivo.show_model()       #Calling Static Method
print()

print('Static method with parameter:')
class Mobile():
    @staticmethod         #Decorartor
    def show_model(m,p):     #Static Method
        model=m
        price=p
        print('Model:',model,'Price:',price)
vivo=Mobile()
vivo.show_model('Vivo Y71',10000)       #Calling Static Method