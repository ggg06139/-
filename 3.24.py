#3.24

a = int(input('숫자를 입력하세요 : '))
b =[]

for i in range(1,a+1):
    c = (1/i)**2
    b.append(c)
print(f'결과는 {sum(b)}입니다.')






intNum = int(input('숫자를 입력하세요 : '))
iResult = 0

for i in range(1,intNum+1):
    iResult += 1/i**2

print(f'결과는 {iResult}입니다.')
