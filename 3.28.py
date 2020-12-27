#3.28

n = int(input('정수를 입력하시오 : '))

fail = 0
sReverselist = []

if n < 10 and n >= 0:
    print(f'{n}은 거꾸로 정수입니다.')
else:
    i = 0
    while True:
        i의자리수 = 10 ** i
        if i의자리수 - n > 0:
            i의수 = i
            break
        elif i의자리수 == n:
            fail = i의자리수
            break
        i += 1
    
    if fail != 0:
        print(f'{n}은 거꾸로 정수가 아닙니다.')
    else:
        s = str(n)
        for k in range(i의수):
            sReverse = s[k]
            sReverselist.append(sReverse)
        sReverselist.reverse()
        iReverse =int(''.join(sReverselist))

        if iReverse == n:
            print(f'{n}은 거꾸로 정수입니다.')
        else:
            print(f'{n}은 거꾸로 정수가 아닙니다.')



'''
1. 한 자리 수면 거꾸로 정수
2. n의 자리수를 확인한다(확인하면서 1000과 같은 수면 끝낸다.)
3. n을 문자로 만들고 자리 수 하나하나를 넣는다.
4. 리벌스하고 조인하고 인트하고 확인한다.

'''
