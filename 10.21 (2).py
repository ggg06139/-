def reverse_generator(l):
    for i in range(len(l)-1,-1,-1):
        yield l[i]

def last_odd(l):
    a = reverse_generator(l)
    for i in range(len(l)):
        b = next(a)
        if b % 2 != 0:
            return b
            break

numbers = [1,2,3,4,5,6,7,8,9,10,12,14,16]
print('마지막 홀수는 :', last_odd(numbers))
