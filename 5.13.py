#5.13 182526 황승현

a = input('10개의 수를 입력하세요: ').split()
a = list(map(int,a))

mean = sum(a)/len(a)                #평균

sdList = [(i-mean)**2 for i in a]
sd = (sum(sdList)/len(a))**0.5      #표준편차
sd = round(sd,2)                    #표준편자 소수점 두 번째 자리까지 표기

print(f'합 : {sum(a)}')
print(f'평균 : {mean}')
print(f'표준편차 : {sd}')