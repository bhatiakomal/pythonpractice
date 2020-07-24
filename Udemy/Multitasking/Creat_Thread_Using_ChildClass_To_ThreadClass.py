'''from threading import Thread
class Mythread(Thread):
    pass
t=Mythread()
print(t.name)'''

print()
#Run Method:
'''from threading import Thread
class Mythread(Thread):
    def run(self):
        print('Run Method')
t=Mythread()
t.start()'''

#Join Method:
from threading import Thread
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread')
t=Mythread()
t.start()
t.join()
for i in range(5):
    print("Main thread")