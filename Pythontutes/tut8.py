mystr="harry is good boy"
print(len(mystr))
#len is used for determine lenght of string and counting is start from 0
print(mystr[0])
print(mystr[0:4])
print(mystr[0:5])
#this is called string slicing
print(mystr[0:18])
print(mystr[0:80])#we don't have string of 80 but system can give us upto its length
print(mystr[0:5:2])
print(mystr[0:])#it takes full length of string
print(mystr[:5])#it takes 0 by default
print(mystr[: :])#it also write whole string [0:length:1]
print(mystr[::2])#it left one character and one takes and so on
print(mystr[::3])#it left two character and one takes and so on
print(mystr[::9])
print(mystr[::68778])#This all is clled extended slicing
print(mystr[-4:-2])#if -ve sign is occur then start learning string from behind
print(mystr[13:15])#we can change -ve sign with +ve sign by count all charater from starting
print(mystr[::-1])#this can make string opposite
print(mystr[::-2])#ye pehle string ko ulta krega after that ye 1 character skip krega
#Some other functions
print(mystr.isalnum())
mystr="harryisgoodboy"
print(mystr.isalnum())#if we remove space from string output is true but if dont then it is false

mystr="harry is goodboy"
print(mystr.isalpha())

mystr="harryisgoodboy"
print(mystr.isalpha())

mystr="harry is goodboy"
print(mystr.endswith("boy"))

mystr="harry is goodboy"
print(mystr.endswith("bdoy"))

mystr="harry is goodboy"
print(mystr.count("b"))

mystr="harry is goodboy"
print(mystr.count("o"))

mystr="harry is goodboy"
print(mystr.capitalize())

mystr="harry is goodboy"
print(mystr.find("is"))

mystr="harry is goodboy"
print(mystr.lower())

mystr="harry is goodboy"
print(mystr.upper())

mystr="harry is goodboy"
print(mystr.replace("is","was"))

mystr="harry is goodboy"
print(mystr.title())

mystr="harry is goodboy"
print(mystr.strip())

mystr="harry is good boy"
print(mystr.startswith(""))

mystr="harry is goodboy"
print(mystr.splitlines())




