#This is used to convert uppercase intomlowercase
class Lowercase():
    def show(self):
        sentence1 = input('Enter your sentence:')
        print("And the output is:",sentence1.swapcase())
obj=Lowercase()
obj.show()
