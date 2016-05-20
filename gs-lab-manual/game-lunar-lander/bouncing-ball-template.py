from visual import *

scene.range=20

ground = box(pos=vector(0,-10.05,0), size=(40.0,1,1), color=color.white)
ball = sphere(pos=(0,9,0), radius=2, color=color.yellow)

ball.m = 1
ball.v = vector(0,0,0)
g=vector(0,-10,0)

dt = 0.01
t = 0

scale=0.5
FgravArrow = arrow(pos=ball.pos, axis=scale*ball.m*g, color=color.red)

scene.mouse.getclick()

while 1:
        rate(100)
        Fgrav=ball.m*g
        Fnet=Fgrav
        ball.v = ball.v + (Fnet/ball.m)*dt
        ball.pos = ball.pos + ball.v*dt
        if(ball.pos.y-ball.radius < ground.pos.y+ground.height/2):
                ball.v=-ball.v
        t = t+dt
        FgravArrow.pos=ball.pos
        FgravArrow.axis=scale*Fgrav
