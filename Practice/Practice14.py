def longest_word(wordz_list):
    word_len=[]
    for i in wordz_list:
        word_len.append((len(i),i))
    word_len.sort()
    return word_len[-1][1]
print(longest_word(["Komalbhatia","Arti","Suraj","Ankit"]))

def long_word(x):
    y=[]
    for i in x:
        y.append((len(i),i))
    y.sort()
    return y[-1][1]
print(long_word(["Ankitanadda","Komal","Aarti"]))