from turtle import *

color('red','yellow')
begin_fill()
speed(0)
while True:
    forward(200)
    left(130)
    if abs(pos()) < 1:
        break
end_fill()
done()