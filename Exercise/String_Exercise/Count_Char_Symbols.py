def Count_Char_Symbol(inputstring):
    charCount=0
    symbolCount=0
    digitCount=0
    for i in inputstring:
        if i.islower() or i.isupper():
            charCount+=1
        elif i.isnumeric():
            digitCount+=1
        else:
            symbolCount+=1
    print('Char=',charCount,'Digit=',digitCount,"Symbols=",symbolCount)
Count_Char_Symbol('P@#yn26at^&i5ve')