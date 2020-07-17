'''class Dog():
    #Class Object Atribute
    #Same for any instance of the class
    species='mammal'
    def __init__(self,mybreed,name):
        self.breed=mybreed #Comes as string
        self.name=name #Comes as string
    def bark(self):
        print('Woolf! My name is{}'.format(self.name))
my_dog=Dog(mybreed='Lab',name='Franky')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark())'''

class Circle():
    pie=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*self.pie
    def get_circumference(self):
        return self.radius*self.pie*2
my_circle=Circle(30)
print(my_circle.area)
print(my_circle.get_circumference())
print(my_circle.pie)
print(my_circle.radius)
