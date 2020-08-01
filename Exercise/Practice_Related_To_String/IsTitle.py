#It retrun true if 1st letter of every word is in upper case
class Istitle():
    def show(self):
        sentence1 = input('Enter your sentence:')
        print("And the output is:",sentence1.istitle())
obj=Istitle()
obj.show()