#3.26

n = int(input('n을 입력하시오 : '))

for k in range(1,n+1):
    if k % 2 != 0:
        for i in range(n*(k-1)+1, n*k+1):
            print(f' {i:>2d} ',end='')
    else:
        for i in sorted(list(range(n*(k-1)+1, n*k+1)),reverse = True):
            print(f' {i:>2d} ',end='')
    print('\n')

'''
1. n만큼 배열하고 띄어쓰기
2. 다음 줄은 n*(k-1)부터 n*k만큼 배열하기
3. 만약 홀수 줄이면 그대로 짝수 줄이면 리버스
'''
