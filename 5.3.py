#5.3
list1 = [3,5,7]
list2 = [2,3,4,5,6]

for i in list1:
    for k in list2:
        list3 = i * k
        print(f'{i} * {k} = {list3}')