import time

def sum1to1000000():
    sum = 0
    for i in range(1,1000001):
        sum += i
    return sum

A = time.time()
sum1to1000000()
B = time.time()
Gap = B-A
print(f'1에서 1,000,000까지의 합을 구하는 시간 : {Gap}초')