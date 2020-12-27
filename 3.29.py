#3.29

print('1)덧셈  2)뺼셈  3)곱셈  4)나눗셈')
n = int(input('어떤 연산을 원하는지 번호를 입력하세요: '))
if n == 1 or n == 2 or n == 3 or n == 4:
    print('연산을 원하는 숫자 두개를 입력하세요')
    a = int(input())
    b = int(input())
    if n == 1:
        print(f'{a}+{b}={a+b}')
    elif n == 2:
        print(f'{a}-{b}={a-b}')
    elif n ==3:
        print(f'{a}*{b}={a*b}')
    elif n == 4:
        print(f'{a}/{b}={a/b}')
else:
    print('잘못 입력하였습니다.')