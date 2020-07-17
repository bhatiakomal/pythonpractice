class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def disp(self):
        print("Student Name:",self.name)
        print("Student Roll No:",self.roll)
class User:
    #Static Method
    @staticmethod
    def show(s):
        print("User Name:",s.name)
        print('User Roll No:',s.roll)
        s.disp()
#Creating object of Student Class
stu=Student("komal",101)
User.show(stu)


