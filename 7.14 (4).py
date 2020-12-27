import turtle as t
import random as r

t1 = t.Turtle()
t1.shape('turtle')
t1.color('black')
t1.pencolor('black')
t1.speed(10)

t2 = t.Turtle()
t2.shape('turtle')
t2.color('red')
t2.pencolor('red')
t2.speed(10)

t3 = t.Turtle()
t3.shape('turtle')
t3.color('blue')
t3.pencolor('blue')
t3.speed(10)

t4 = t.Turtle()
t4.shape('turtle')
t4.color('green')
t4.pencolor('green')
t4.speed(10)

t5 = t.Turtle()
t5.shape('turtle')
t5.color('gray')
t5.pencolor('gray')
t5.speed(10)

t6 = t.Turtle()
t6.shape('turtle')
t6.color('pink')
t6.pencolor('pink')
t6.speed(10)

tlist = [t1, t2, t3, t4, t5, t6]
for k in range(20):
    for i in tlist:
        i.penup()
        tright = r.randint(0,360)
        tfd = r.randint(1, 100)
        '''
        만약 터틀이 300구간을 넘어선다면 다음 번에 400구간 이상으로 갈 수 있기에 머리를 0,0쪽으로 돌리는 식으로 코딩했습니다.
        '''
        if (i.xcor() > 300 or i.xcor() < -300) or (i.ycor() > 300 or i.ycor() < -300):
            i.setheading(i.towards(0,0))
            i.fd(tfd)
            i.stamp()
        else:
            i.right(tright)
            i.fd(tfd)
            i.stamp()
