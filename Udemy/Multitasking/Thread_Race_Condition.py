from  threading import Thread,current_thread
class Flight():
    def __init__(self,avialble_seats):
        self.aviable_seats=avialble_seats
    def reserve(self,need_seats):
        print('Availble seats:',self.aviable_seats)
        if self.aviable_seats>=need_seats:
            name=current_thread().name
            print(f'{need_seats}seat is alloted for {name}')
            self.aviable_seats-=need_seats
        else:
            print('Sorry all seats has alloted')
f=Flight(1)
t1=Thread(target=f.reserve,args=(1,),name='Komal')
t2=Thread(target=f.reserve,args=(1,),name='Aarti')
t1.start()
t2.start()
