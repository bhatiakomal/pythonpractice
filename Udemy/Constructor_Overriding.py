#Without Parameter:
'''class Father():
    def __init__(self):
        self.money=2000
        print("Father class Constructor")
    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def __init__(self):
        self.money=10000
        self.car="Lamborgini"
    def disp(self):
        print("Son's class instance Method:",self.money)
f=Father()
s=Son()
s.disp()
print(s.money)
print(s.car)
s.disp()
s.show()'''

#With Parameter:
class Father():
    def __init__(self,m):

        self.money=m
        print("Father class Constructor")
    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def __init__(self,r):
        self.money=r
        self.car="Lamborgini"
    def disp(self):
        print("Son's class instance Method:",self.money)
s=Son(900000)
s.disp()
print(s.money)
print(s.car)
s.disp()
s.show()