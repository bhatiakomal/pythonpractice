class Add:
    def result(self,x,y):
        print('Addition is:',x+y)
class Multi(Add):
    def result(self,a,b):
        super().result(20,40)       #calling parent methods
        print('Multiplication:',a*b)
m=Multi()
m.result(20,10)
