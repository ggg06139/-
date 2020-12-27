a = [x for x in range(10,50) if x != 2 and x != 3 and x % 2 != 0 and (all([ 0 for i in range(3,x,2) if x % i == 0]) == True) ]

print(a)
