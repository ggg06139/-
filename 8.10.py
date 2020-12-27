import random

f = open('randint30.txt','w',encoding='utf-8')
for _ in range(30):
    a = random.randint(1,10)
    f.write(str(a))
    f.write(' ')
f.close()

f = open('randint30.txt','r',encoding='utf-8')
a = list(map(int,f.read().split()))
for i in range(1,11):
    print(f'{i} : {a.count(i)}')
