#5.21 182526 황승현
'''
1. src를 나눈다.
2. 인덱스끼리 곱한다
3. 조인한다
'''
src = 'a2b3c6a3c3f1g1'

if src == '':
    print("src = ''")
    print("output = ''")

else:

    srclist = list(src)

    for i in range(len(srclist)):
        if i != 0 and i % 2 != 0:
            srclist[i] = int(srclist[i])

    resultlist1 = list(srclist[0:-1:2])
    resultlist2 = list(srclist[1::2])

    #리스트를 서로 곱하는 법

    result = []
    for x in range(len(resultlist2)):
        result.append(resultlist2[x] * resultlist1[x])

    result = ''.join(result)

    print(f"src = '{src}'")
    print(f"output = '{result}'")

'''

src = 'a2b3c6a2c3f1g1'

srclist = list(src)

a = srclist[0::2]
b = srclist[1::2]
b = list(map(int,b))
c = []

print(a)
print(b)

for i in range(len(a)):
    c.append(a[i] * b[i])

c = ''.join(c)

print(c)
'''