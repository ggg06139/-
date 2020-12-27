#6.24 (3) 182526 황승현

import string

src_str = string.ascii_uppercase
dst_str = ''.join(list(src_str)[3:] + list(src_str)[:3])


def ciper(a):
    Index = src_str.index(a)
    Alphabet = dst_str[Index]

    return Index, Alphabet

result = []

sInput = input('문장을 입력하시오 : ')
sInput = list(''.join(sInput))

for i in sInput:
    if i in list(src_str):
        result.append(ciper(i)[1])
    else:
        result.append(i)

result = ''.join(result)

print(f'암호화 된 문장 : {result}')