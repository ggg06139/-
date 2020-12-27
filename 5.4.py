#5.4

a = list(range(2,7))
print('a =',a)

b = []
lena = len(a)

for i in range(1,lena+1):
    b.append(a.pop())

print('b =',b)