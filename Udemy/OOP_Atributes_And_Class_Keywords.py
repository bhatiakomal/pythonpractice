'''class Sample():
    pass
my_sample=Sample()
type(my_sample)'''

'''class Dog():
    def __init__(self,mybreed):
        self.breed=mybreed
my_dog=Dog(mybreed='Lab')
print(type(my_dog))
print(my_dog.breed)'''

class Dog():
    def __init__(self,mybreed,name,spot):
        self.breed=mybreed #Comes as string
        self.name=name #Comes as string
        self.spot=spot #should be in Boolean True or false
my_dog=Dog(mybreed='Lab',name='Sammy',spot=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spot)