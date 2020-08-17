l=list()
for i in range(int(input('Enter number of students:'))):
    k=list()
    name = input('Enter name:')
    score = float(input("Eneter score:"))
    k.append(name)
    k.append(score)
    l.append(k)
h=[j[1] for j in l]
m=min(h)
c=h.count(m)
for i in range(c):
    h.remove(m)
n=min(h)
q=list()
for i in l:
    if i[1]==n:
        q.append(i[0])
w=sorted(q)
for i in w:
    print(i)


