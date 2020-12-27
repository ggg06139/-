#6.24 (2) 182526 황승현

import string

src_str = string.ascii_uppercase
dst_str = ''.join(list(src_str)[3:] + list(src_str)[:3])


def ciper(a):
    Index = src_str.index(a)
    Alphabet = dst_str[Index]

    return Index, Alphabet

A1 , A2 = ciper('A')
B1 , B2  = ciper('B')

print(f'src_str의 A 인덱스 : {A1}')
print(f'dst_str의 0번째 알파벳 : {A2}')
print(f'src_str의 B 인덱스 : {B1}')
print(f'dst_str의 1번째 알파벳 : {B2}')