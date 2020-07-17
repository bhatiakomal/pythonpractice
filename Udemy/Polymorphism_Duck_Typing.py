class Duck:
    def walk(self):
        print('tapak tapak hahaahaha')
class Horse:
    def walk(self):
        print('tabdak tabdak tabdak tabdak')
class Cat:
    def talk(self):
        print('Meow Meow Meow Meow')
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)
c=Cat()
myfunction(c)