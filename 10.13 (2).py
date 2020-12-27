a = [x for x in range(2001, 2031) if (x%4 == 0 and x % 100!= 0) or (x % 400 ==0)]

print(f'2001년부터 2030년 사이의 윤년 : {a}')
