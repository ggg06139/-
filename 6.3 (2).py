#6.3 (2) 182526 황승현

menu = {'Americano' : '3,000원' , 'Ice Americano' : '3,500원' , 'Cappuccino' : '4,000원' , 'Cafe Latte' : '4,500원' , 'Espresso' : '3,600원'}

for key in menu:
    print(f'{key:<20s}가격 : {menu[key]}')

select = input('위의 메뉴 중 하나를 선택하세요 : ')

if (select in menu) == True:
    print(f'{select}는 {menu[select]} 입니다. 결제를 부탁합니다.')
else:
    print(f'미안합니다. {select}는 메뉴에 없습니다.')