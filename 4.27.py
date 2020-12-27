#4.27

'''
def unit_fraction(frac):
    i = 1
    while (1 / i) >= a:
        i += 1
    b = i
    c = min(abs(a-(1/b)),abs(a-(1/(b-1))))
    
    if (abs(a-(1/b)) == c):
        return f'1/{b}'
    elif (abs(a-(1/(b-1))) == c):
        return f'1/{b-1}'


#접근 방법을 주어진 소수보다 한단계 작은 단위분수를까지만 비교 대상으로 삼는다.

a = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
A = unit_fraction(a)
AResult = 1 / int(A[2:])
print(f'가장 가까운 단위 분수는 {unit_fraction(a)}이며, 이 값은 {AResult}입니다.')
'''

def unit_fraction(frac):
    i = 1
    save = 0
    nice = 0

    while True:
        if 1 / i < frac:
            save = i
            break
        elif 1 / i == frac:
            nice = i
            break
        i += 1

    if nice == i:
        return f'1 / {str(nice)}'
    else:
        if abs(1/save) > abs(1/save-1):
            return f'1 / {str(save-1)}'
        elif abs(1/save-1) > abs(1/save):
            return f'1 / {str(save)}'

print(unit_fraction(0.2223423))