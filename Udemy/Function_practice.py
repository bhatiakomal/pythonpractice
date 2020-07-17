"""def lesser_of_two_no(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            result=a
        else:
            result=b
    else:
        if a>b:
            result=a
        else:
            result=b
    return result
rslt=lesser_of_two_no(2,20)
rslt1=lesser_of_two_no(22,18)
rsl2=lesser_of_two_no(7,21)
rslt3=lesser_of_two_no(44,9)
print(rslt)
print(rslt1)
print(rsl2)
print(rslt3)

def lesser_of_two_no(a,b):
    if a%2==0 and b%2==0:
       return min((a,b))
    else:
        return max(a,b)
rslt=lesser_of_two_no(2,20)
rslt1=lesser_of_two_no(22,18)
rsl2=lesser_of_two_no(7,21)
rslt3=lesser_of_two_no(44,9)
print(rslt)
print(rslt1)
print(rsl2)
print(rslt3)"""

#Second Exercise
"""def check_capital_Latter(text):
    wordlist=text.split()
    print(wordlist)
    first=wordlist[0]
    second=wordlist[1]
    return first[0]==second[0]
rslt=check_capital_Latter("Komal Kamal")
rslt1=check_capital_Latter('suraj Kamal')
rslt2=check_capital_Latter('Priya pratyush')
print(rslt)
print(rslt1)
print(rslt2)"""

"""def check_capital_Latter(text):
    wordlist=text.split()
    return wordlist[0][0]==wordlist[1][0]

rslt=check_capital_Latter("Komal Kamal")
rslt1=check_capital_Latter('suraj Kamal')
rslt2=check_capital_Latter('Priya pratyush')
print(rslt)
print(rslt1)
print(rslt2)"""

"""def sum_20(n1,n2):
    if n1+n2==20:
        return True
    elif n1==20:
        return True
    elif n2==20:
        return True
    else:
        return False
sum=sum_20(20,10)
sum1=sum_20(2,1)
print(sum)
print(sum1)"""

def sum_20(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
sum=sum_20(20,10)
sum1=sum_20(2,1)
print(sum)
print(sum1)
