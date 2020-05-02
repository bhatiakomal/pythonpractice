'''def ab():
    print("Komal Bhatia")
    ab()
ab()'''

i=0
def ab():
    global i
    i=i+1
    print("Komal Bhatia",i)
    ab()
ab()