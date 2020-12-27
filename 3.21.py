#3.21

a = int(input('숫자를 입력하세요 : '))

if a == 2:
    print(f'{a}는 소수입니다')
elif a % 2 == 0:
    print(f'{a}는 소수가 아닙니다')
else:
    for i in range(3,a,2):
        if a / i == a // i:
            print(f'{a}는 소수가 아닙니다')
            break
if a != 1 and a != 2 and a % 2 != 0:
    if a / i != a // i:
        print(f'{a}는 소수입니다')
