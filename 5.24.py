#5.24 182526 황승현

def A(n):
    resultlist = []
    resultsum = 0
    for i in range(1,n):
        if n % i == 0:
            resultlist.append(i)

    resultsum = sum(resultlist)
    return resultlist, resultsum

for k in range(1,10001):

    Rlist, Rsum = A(k)

    if k == Rsum:
        print(f'{k}는 완전수입니다')
        print(f'{k}의 약수 : {Rlist}, 약수의 합 = {Rsum}')