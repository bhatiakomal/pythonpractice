#This is used capitalization every 1st word of the sentence
class Title():
    def disp(self):
        sentence1 = input('Enter your sentence:')
        print("And the output is:",sentence1.title())
obj=Title()
obj.disp()