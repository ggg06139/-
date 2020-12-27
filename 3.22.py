#3.22
for k in range(2,25):
    for a in range(k,k+1):
        if a == 2:
            n = '소수'
        elif a % 2 == 0:
            n = '합성수'
        else:
            for i in range(3,a,2):
                if a / i == a // i:
                    n = '합성수'
                    break
                elif a / i != a // i:
                    n = '소수'
    print(f'{a} : {n}')
