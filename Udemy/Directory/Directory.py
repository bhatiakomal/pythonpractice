import os
#getcwd()-It shows current directory path
'''print(os.getcwd())'''
#os.mkdir-use to make directory
#mydir  is parent and mychilddir is child directory
'''os.mkdir('mydir/mychilddir')'''
#os.makedirs-is used to make directory with parent we can make as many we want
'''os.makedirs('parentdir/childdir/grandchilddir')'''
#Change directory
#chdir- is used to change the directory
'''print(os.getcwd())
os.chdir('mydir')
print(os.getcwd())'''

#rename-change name of directory
'''os.rename('mydir','yourname')'''

#remove  diretory
#this can remove only one directory
'''os.remove('mydir')'''

#wamt to remove whole daretory parent child grandchild
'''os.removedirs('parentdir/childdir/grandchilddir')'''



