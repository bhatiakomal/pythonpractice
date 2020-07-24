from threading import Thread,current_thread
def disp():
    print("child thread object",current_thread()) #From this we can know name of thread
t=Thread(target=disp())
t.start()
print("main Thread",current_thread())
print()

from threading import Thread,current_thread
def disp():
    print("child thread Name",current_thread().getName())
t1=Thread(target=disp)
t1.start()
print("main Thread Name",current_thread().getName())

#Changing name of thread
from threading import Thread,current_thread
def disp():
    print("Default child thread Name",current_thread().getName())
    current_thread().setName('Doc thread')
    print('New child thread Name',current_thread().getName())
t1=Thread(target=disp)
t1.start()
print("main Thread Name",current_thread().getName())
current_thread().setName('Geekyshows Thread')
print('New child thread Name', current_thread().getName())

#From .name we can also find name of thread and also change the name
from threading import Thread,current_thread
def disp():
    print("Default Child Name:",current_thread().name)
t=Thread(target=disp)
t.start()
print('Main thread:',current_thread().name)
