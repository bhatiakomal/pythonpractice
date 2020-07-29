class Student:
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
    def disp(self):
        print(f' Name:{ self.name} RollNo:{ self.roll} Address:{ self.address}')