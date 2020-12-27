#3.20

a = int(input('숫자를 입력하세요 : '))
for i in range(1,a+1):
    for n in range(1,i+1):
        if n == i:
            print(' '*(a-n),end='')
            print('*'*n,end='')
    print('\n')    
