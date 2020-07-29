f=open('Members.txt',mode='a')#W= is write mode,it override the data
lst=["Komal\n",'Ankita\n','Rishi\n','Priya\n','Ankit\n','Suraj\n']
f.writelines(lst)
f.close()
