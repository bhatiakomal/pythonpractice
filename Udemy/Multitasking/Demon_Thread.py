'''from threading import Thread
def disp():
    print('Daemon Thread')
t1=Thread(target=disp)
#isdaemon method tell us that whether the thread is Daemon or non Daemon
print('Befor:',t1.isDaemon())
#setDaemon is used to make non Daemon thread into Daemon thread
t1.setDaemon(True)
print('After:',t1.isDaemon())
#It should be start after making it Daemon
t1.start()'''

#We can also use its property
from threading import Thread
def disp():
    print('Daemon Thread')
t1=Thread(target=disp)
#isdaemon method tell us that whether the thread is Daemon or non Daemon
print('Befor:',t1.daemon)
t1.daemon=True
#setDaemon is used to make non Daemon thread into Daemon thread
print('After:',t1.daemon)
t1.daemon=True
#It should be start after making it Daemon
t1.start()



