from visual import *

track=box(pos=vector(0,-0.075,0), size=(3,0.05,0.1), color=color.white)

ball=sphere(pos=vector(-1.4,0,0), radius=0.05, color=color.cyan)

ball.v=0.3*vector(1,0,0)

print(ball.v)

dt=0.01
t=0

while 1:
    rate(200)
    ball.pos = ball.pos + ball.v*dt
    t=t+dt
#    print(t,ball.pos)


    
