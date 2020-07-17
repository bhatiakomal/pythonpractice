'''class MyClass:
    def sum(self,a):
        print('1st sum is :',a) #This is for java
    def sum(self):
        print('2nd sum is:')
obj=MyClass()
obj.sum()
obj.sum(5)

class MyClass:
    def sum(self,a,b,c):
        s=a+b+c
        return s
obj=MyClass()
print(obj.sum(20,50,60))

class MyClass:
    def sum(self,a=None,b=None,c=None):
        s=a+b+c
        return s
obj=MyClass()
print(obj.sum(20,50,60))'''

class MyClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            s='Provide at least two numbers'
        return s
obj=MyClass()
print(obj.sum(20,50))
print(obj.sum(20,50,90 ))
print(obj.sum(20))
