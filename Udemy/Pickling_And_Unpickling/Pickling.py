import pickle, Student
#student.dat is binary file
#wb=write binary mode
#f is file object
with open('student.dat',mode='wb') as f:
    #stu1 is class object
    stu1=Student("Komal ",101," Himachal ")
    stu2 =Student("Arti ", 102, " Himachal ")
    #dump function is used to class object covert into byte string
    pickle.dump(stu1,f)
    pickle.dump(stu2, f)
    print("Pickling is done")