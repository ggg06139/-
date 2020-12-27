#4.28

def factorical(k):
    result = 1
    for i in range(1,k+1):
        result *= i
    return result

def euler(n):
    Result = 0
    for k in range(n+1):
        Result += 1 / factorical(k)
    Result = round(Result,5)
    return Result

print(f'euler( 5) = {euler(5):10f}')
print(f'euler(20) = {euler(20):10f}')