#4.4

def change(n):
    m = n * 1.61
    return m

for i in range(1,6):
    mile = change(i)
    print(f'{i} 마일 = {mile} 킬로미터')