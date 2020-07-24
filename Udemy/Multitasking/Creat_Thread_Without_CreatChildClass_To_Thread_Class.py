from  threading import Thread
class Myvthread(Thread):
    def disp(self,a,b):
        print(a,b)
myt=Myvthread()
t=Thread(target=myt.disp,args=(10,20))
t.start()