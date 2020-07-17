'''class outerClassName:
    def __init__(self):
        self.variable_name='value'
        self.innerClassObjectName=self.InnerClassName()
    def method_name(self):
        methodbody
    class InnerClassName():
        def __init__(self):
            self.variable_name()='value'
        def method_name(self):
            methodbody'''

class Army:                 #Outer Class
    def __init__(self):
        self.name='Komal'
        self.gn=self.Gun()   #Inner Class Object
    def show(self):
        print("Name:",self.name)
    def Gun(self):
        print("Name:",self.name)
    class Gun:
        def __init__(self):
            self.name="Ak47"
            self.capacity='75 Rounds'
            self.length='34.3 Inch'
        def dip(self):
            print("Gun Name:",self.name)
            print("Gun Capacity:", self.capacity)
            print("Gun Length:", self.length)

a=Army()
print(a.name)
print(a.show())
print()
print(a.gn.name)
g=a.gn
print()
print(g.name)
print(g.capacity)
print(g.length)
print()
g.dip()
