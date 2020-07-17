#Constructor In inheritence:
'''class Father():
    def __init__(self):
        self.money=2000
        print("Father class Constructor")
    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def disp(self):
        print("Son's class instance Method:",self.money)
s=Son()
s.disp()
print(s.money)
s.show()'''

class Father():
    def __init__(self,m):
        self.money=m
        print("Father class Constructor")
    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def disp(self):
        print("Son's class instance Method:",self.money)
s=Son(5000)
s.disp()
print(s.money)
s.show()