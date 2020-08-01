#It is used to replace a sub string in a string with another sub string
class Replace():
    def show(self):
        sentence1 = 'Her name is Jessica'
        print(sentence1.replace('Jessica','Alisa'))
obj=Replace()
obj.show()


class Replace():
    def show(self):
        sentence1 = input("Enter Your String")
        print(sentence1.replace('Jessica','Alisa'))
obj=Replace()
obj.show()
#Why do not input method is work here