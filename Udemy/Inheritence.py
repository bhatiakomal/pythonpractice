#Single heritance:
class Father():
    money=1000
    def show(self):
        print('Parent class Intance Method')
    @classmethod
    def showmoney(cls):
        print("Parent Class class method:",cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent class Static Method:", a)
class Son(Father):
    def disp(self):
        print("child class Instance Method")
s=Son()
s.disp()
s.show()
s.showmoney()
s.stat()
print()
f=Father() #Calling by Parent class but this is not used in heritance
f.showmoney()
f.show()
f.stat()


