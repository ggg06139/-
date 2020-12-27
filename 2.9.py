#2.9

print('섭씨\t 화씨')
print('0 \t',(9/5)*0+32)
print('10\t',(9/5)*10+32)
print('20\t',(9/5)*20+32)
print('30\t',(9/5)*30+32)
print('40\t',(9/5)*40+32)
print('50\t',(9/5)*50+32)

print('섭씨\t 화씨')
for i in range(0,51,10):
    print(i,'\t',(9/5)*i+32)

print('섭씨\t화씨')
for i in range(0,51,10):
    print(f'{i}\t{(9/5)*i+32}')

iCelsius=0
print('섭씨 \t 화씨')
while iCelsius < 60:
    fFahrenheit=(9/5)*iCelsius+32
    print(iCelsius,'\t',fFahrenheit)
    iCelsius += 10
