#6.3 (1) 182526 황승현

menu = {'Americano' : '3,000원' , 'Ice Americano' : '3,500원' , 'Cappuccino' : '4,000원' , 'Cafe Latte' : '4,500원' , 'Espresso' : '3,600원'}

for key in menu:
    print(f'{key:<20s}가격 : {menu[key]}')