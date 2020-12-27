#3.31
'''
ilist = []
alist = []
result_list = []
for i in range(200,300):
    ilist = []
    alist = []
    for n in range(1,i):
        if i % n == 0:
            ilist.append(n)
    isum = sum(ilist)
    for a in range(200, 300):
            for m in range(1,a):
                if a % m == 0:
                    alist.append(m)
                    if sum(ilist) == sum(alist):
                        result_list.append(a)
'''
def resultSum(n):
    A = []
    for i in range(1,n):
        if n % i == 0:
            A.append(i)
    B = sum(A)
    return B

for n in range(1,20001):
    a = resultSum(n)

    if n == resultSum(a) and a != n:
        print(f'{a}의 친화수 {n}')