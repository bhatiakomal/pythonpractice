import pickle
class Student():
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
    def disp(self):
        print(f' Name:{ self.name} RollNo:{ self.roll} Address:{ self.address}')

#student.dat is binary file
#wb=write binary mode
#f is file object
with open('student.dat',mode='wb') as f:
    #stu1 is class object
    stu1=Student("Komal ",101," Himachal ")
    stu2 = Student("Arti ", 102, " Himachal ")
    #dump function is used to class object covert into byte string
    pickle.dump(stu1,f)
    pickle.dump(stu2, f)
    print("Pickling is done")
with open('student.dat',mode='rb') as f:
    #load o read a pickled object from a binary file and return it into a object
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
    print("Unpickling is done!!!")
    obj1.disp()
    obj2.disp()