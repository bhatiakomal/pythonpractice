'''def cap_alph(text):
    firstletter=text[0]
    inbetween=text[1:3]
    forth=text[3]
    rest=text[4:]
    return firstletter.upper()+inbetween+forth.upper()+rest
rslt=cap_alph('macdonal')
print(rslt)

def cap_alph(text):
    firsthalf=text[:3]
    secondhalf=text[3:]
    return firsthalf.capitalize()+secondhalf.capitalize()
rslt=cap_alph('macdonal')
print(rslt)'''

'''def disp(sentence):
    worldlist=sentence.split()
    reversed_wordlist=worldlist[: : -1]
    return reversed_wordlist
rslt=disp('i am home')
print(rslt)

def disp(sentence):
    worldlist=sentence.split()
    reversed_wordlist=worldlist[: : -1]
    return ' '.join(reversed_wordlist)
rslt=disp('i am home')
print(rslt)'''

def check_range(n):
    return (abs(100-n)<=10) or abs((200-n)<=10)
rslt1=check_range(90)
rslt2=check_range(104)
rslt3=check_range(150)
rslt4=check_range(209)
print(rslt1)
print(rslt2)
print(rslt3)
print(rslt4)