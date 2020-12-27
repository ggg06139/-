#6.24 (1) 182526 황승현

import string

src_str = string.ascii_uppercase
print(f'src_str = {src_str}')

dst_str = ''.join(list(src_str)[3:] + list(src_str)[:3])
print(f'dst_str = {dst_str}')