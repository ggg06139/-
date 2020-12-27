#3.25

i = 1
a = 0
while True:
    a += 7
    print(f'day : {i}  달팽이의 위치 : {a} 미터')
    if a > 30:
        break
    i += 1
    a -= 5
    
print(f'\n우물을 탈출하는 데 걸린 날은 {i}일 입니다.')
