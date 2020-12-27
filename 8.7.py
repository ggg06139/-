f = open('number1to10.txt','w+',encoding='utf-8')
for i in range(1,11):
    i = str(i)
    f.write(i)
    f.write('\n')
f.close()

f = open('number1to10.txt','r+',encoding='utf-8')
ff = open('numberby10.txt','w+',encoding='utf-8')
for _ in range(10):
    a = f.readline().rstrip()
    a = int(a)*10
    a = str(a)
    ff.write(a)
    ff.write('\n')
f.close()
ff.close()

f = open('number1to10.txt','r+',encoding='utf-8')
ff = open('numberby10.txt','r+',encoding='utf-8')
fff = open('merge.txt','w+',encoding='utf-8')

for _ in range(10):
    b = f.readline().rstrip()
    c = ff.readline().rstrip()
    fff.write(f'{b} : {c}')
    fff.write('\n')
f.close()
ff.close()
fff.close()
