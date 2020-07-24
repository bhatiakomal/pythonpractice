from  threading import Thread
class MyExam(Thread):
    def solve_Question(self):
        self.q1()
        self.q2()
        self.q3()
    def  q1(self):
        print("Question1 solved")
    def  q2(self):
        print("Question2 solved")
    def  q3(self):
        print("Question3 solved")
mye=MyExam()
t=Thread(target=mye.solve_Question)
t.start()