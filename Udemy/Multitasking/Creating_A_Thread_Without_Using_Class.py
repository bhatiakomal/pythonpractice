from threading import Thread
def disp(a):
    print('Thread',a)
t=Thread(target=disp,args=(10,))
t.start()


from threading import Thread
def disp(a,b):
    print('Thread',a,b)
for i in range(5):
    t=Thread(target=disp,args=(10,20))
    t.start()


