def fibo(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

a = int(input('fibo(n)의 n을 입력하세요: '))
print(f'fibo({a}) = ',fibo(a))


def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

a = int(input('fibo(n)의 n을 입력하세요: '))
print(f'fibo({a}) = ',fibo(a))