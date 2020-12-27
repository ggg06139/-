#5.20 182526 황승현

'''
1. src를 받는다. 만약 src가 없다면 종료 있다면 2번으로
2. srclist에 src를 리스트화 한다.
3. pop리스트를 만들어서 일단 src리스트[0]을 넣고 src리스트에서는 지운다.
3. srclist의 인덱스 0과 인덱스 1이 같다면 그 문자를 src리스트에서는 지우고 pop리스트에는 넣는다.
4. 같은 문자가 더이상 없다면 result에 저장
5. join함수를 사용해서 결과값 도출
'''

src = 'asbssss'

if src == '':
    print("src = ''")
    print("output = ''")
else:
    srclist = list(src)
    poplist = []
    resultlist = []
    result = []

    while True:
        if bool(srclist) == True or bool(poplist) == True:

            if bool(poplist) == False:
                poplist.append(srclist.pop(0))

            if bool(srclist) == True:

                if srclist[0] == poplist[0]:
                    poplist.append(srclist.pop(0))

                else:
                    resultlist = poplist
                    result.append(resultlist[0])
                    result.append(len(resultlist))
                    poplist = []
                    resultlist = []

            else:
                resultlist = poplist
                result.append(resultlist[0])
                result.append(len(resultlist))
                poplist = []
                resultlist = []
                break

        else:
            break

    result = [str(x) for x in result]
    result = ''.join(result)

    print(f"src = '{src}'")
    print(f"output = '{result}'")