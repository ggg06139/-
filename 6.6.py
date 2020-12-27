#6.6 182526 황승현

t1 = 'a','b','c'
t2 = ('a','b','c')
t3 = ('d','e')

#(1)
print(t1 == t2)
#True

#(2)
print(t2 + t3)
#('a', 'b', 'c', 'd', 'e')

my_list = []
for x in t1:
    my_list.append(x)

#(3)
print(my_list)
#['a', 'b', 'c']

#(4)
print([x for x in t1])
#['a', 'b', 'c']

my_list = []
for x in t1:
    for y in t3:
        my_list.append(x + y)
#(5)
print(my_list)
#['ad', 'ae', 'bd', 'be', 'cd', 'ce']

#(6)
print([x + y for x in t1 for y in t3])
#['ad', 'ae', 'bd', 'be', 'cd', 'ce']
