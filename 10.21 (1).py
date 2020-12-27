def reverse_generator(l):
    for i in range(len(l)-1,-1,-1):
        yield l[i]

numbers = [1,2,3,4,5,6,7,8,9,10,12,14,16]

for num in reverse_generator(numbers):
    print(num, end=' ')
