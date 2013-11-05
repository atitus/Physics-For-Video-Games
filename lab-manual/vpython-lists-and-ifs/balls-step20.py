from visual import *

#scene.background=color.white
scene.range=5
scene.autoscale=False

ball1=sphere(pos=(-5,3,0), radius=0.2, color=color.magenta)
ball2=sphere(pos=(-5,1,0), radius=0.2, color=color.cyan)
ball3=sphere(pos=(-5,-1,0), radius=0.2, color=color.yellow)
ball4=sphere(pos=(-5,-3,0), radius=0.2, color=color.orange)

ball1.v=0.5*vector(1,0,0)
ball2.v=1*vector(1,0,0)
ball3.v=1.5*vector(1,0,0)
ball4.v=2*vector(1,0,0)

ballsList = [ball1, ball2, ball3, ball4]

t=0
dt=0.01

while 1:
    rate(100)
    for thisball in ballsList:
        thisball.pos=thisball.pos+thisball.v*dt
        if thisball.pos.x>5:
            thisball.v=-1*thisball.v
        elif thisball.pos.x<-5:
            thisball.v=-1*thisball.v
    t=t+dt

