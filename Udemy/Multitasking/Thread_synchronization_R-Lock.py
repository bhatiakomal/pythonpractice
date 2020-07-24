from  threading import*
class Flight():
    def __init__(self,avialble_seats):
        self.aviable_seats=avialble_seats
        self.lock=RLock()
    def reserve(self,need_seats):
        #Acquire( ) is used to lock
        self.lock.acquire()
        self.lock.acquire()
        print('Availble seats:',self.aviable_seats)
        if self.aviable_seats>=need_seats:
            name=current_thread().name
            print(f'{need_seats}seat is alloted for {name}')
            self.aviable_seats-=need_seats
        else:
            print('Sorry all seats has alloted')
            #release () is used to release the lock
            self.lock.release()
            self.lock.release()
f=Flight(2)
t1=Thread(target=f.reserve,args=(1,),name='Komal')
t2=Thread(target=f.reserve,args=(1,),name='Aarti')
t3=Thread(target=f.reserve,args=(1,),name='Priya')
t1.start()
t2.start()
t3.start()
#By using join() we get output in increasing order ie one by one
t1.join()
t2.join()
t3.join()
print('Main Thread')