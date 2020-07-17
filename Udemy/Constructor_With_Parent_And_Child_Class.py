'''class Father():
    def __init__(self):
        self.money=500000
        print("Father class Constructor")
    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def __init__(self):
        super().__init__()
        print('Son class Constructor')

    def disp(self):
        print("Son class Instance Method",self.money)
s=Son()
s.disp()'''

class Father():
    def __init__(self,m):
        self.money=m
        print("Father class Constructor")
    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)
        self.job=j
        print('Son class Constructor')

    def disp(self):
        print("Son class Instance Method",self.money,'Job',self.job)
s=Son(800000,'Python')
s.disp()
print()
