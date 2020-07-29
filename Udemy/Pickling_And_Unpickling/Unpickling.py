with open('student.dat',mode='rb') as f:
    #load o read a pickled object from a binary file and return it into a object
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
    print("Unpickling is done!!!")
    obj1.disp()
    obj2.disp()