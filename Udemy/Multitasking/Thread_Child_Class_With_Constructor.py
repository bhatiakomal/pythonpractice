from  threading import Thread
class Myvthread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child Class Thread constructor")
    def run(self):
        pass
t=Myvthread()
t.start()
print("Main Thread")