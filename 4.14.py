#4.14

def sort3(num1, num2, num3):
    result = []
    iList = [num1, num2, num3]
    iList = sorted(iList)
    for x in iList:
        x = str(x)
        result.append(x)
    result = ' '. join(result)
    return result

print('세 수를 입력하세요 :')
a = int(input())
b = int(input())
c = int(input())
k = sort3(a,b,c)
print(f'정렬된 리스트는 다음과 같습니다: {k}')

A = input('세 수를 입력하세요 :\n')
B = input()
C = input()

setList = []

setList.append(A)
setList.append(B)
setList.append(C)
    
setList = sorted(setList)

print('정렬된 리스트는 다음과 같습니다:',setList[0],setList[1],setList[2])
