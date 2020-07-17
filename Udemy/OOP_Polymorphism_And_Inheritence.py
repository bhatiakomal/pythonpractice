#Inheritence
''''class Animal():
    def __init__(self):
        print("Created Animal")
    def who_am_I(self):
        print("I am an Animal")
    def eat(self):
        print("I am eating")
class Dog(Animal):
    def __index__(self):
        Animal.__init__(self)
        print("Dog Created")
mydog=Dog()
print(mydog.eat())
myanimal=Animal()
print(myanimal.eat())
print(myanimal.who_am_I())
print(myanimal.__init__())'''

#Polymorphysim
class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" Say woof!"
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" Say mywoe!"

niko=Dog("Niko")
felix=Cat("felix")
print(niko.speak())
print(felix.speak())