#4.24

a = input('여러 단어로 이루어진 글을 입력하세요: ').split()

a = ' '.join(a)

a = a.replace('.',' ')
a = a.replace(':',' ')
a = a.replace(',',' ')

a = a.split()

a = sorted(a)
print('정렬 결과 :')
print(a)
