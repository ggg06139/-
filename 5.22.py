#5.22

n = int(input('n을 입력하시오 : '))
c = []

for i in range(0,n+1):
    a = list(range(1+(n*i), (i+1)*n+1))
    c.append(a)
    a = []

for k in range(1,n+1):
    if k % 2 != 0:
        c[k][::-1]
print(c)