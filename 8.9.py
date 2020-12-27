f = open('coord.txt','r',encoding='utf-8')
a = f.readline().rstrip()
A = []
for i in f:
    i = i.rstrip()
    i = list(map(int,i.split()))
    A.append(i)
A = sorted(A)
for j in A:
    print(j[0],j[1])
