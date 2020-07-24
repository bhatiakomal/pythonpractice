#Thread Communication Event
from threading import Thread,Event
from time import sleep
def  light_switch():
    sleep(3)
    e.set()
    print('Green Light On')
    sleep(5)
    print("Red light On")
    e.clear()
def traffic():
    e.wait()
    while e.is_set():
        print("You can go.....")
e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=traffic)
t1.start()
t2.start()




