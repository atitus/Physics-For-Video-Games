from visual import *

#scene.background=color.white
scene.range=10
scene.autoscale=False

ball1=sphere(pos=(-10,0,0), radius=0.25, color=color.magenta)
ball2=sphere(pos=(-10,1,0), radius=0.25, color=color.cyan)
ball3=sphere(pos=(-10,2,0), radius=0.25, color=color.yellow)
ball4=sphere(pos=(-10,3,0), radius=0.25, color=color.orange)
ball5=sphere(pos=(-10,4,0), radius=0.25, color=color.blue)
ball6=sphere(pos=(-10,5,0), radius=0.25, color=color.red)
ball7=sphere(pos=(-10,6,0), radius=0.25, color=color.green)
ball8=sphere(pos=(-10,7,0), radius=0.25, color=color.white)
ball9=sphere(pos=(-10,8,0), radius=0.25, color=(0.2,0.5,1))
ball10=sphere(pos=(-10,9,0), radius=0.25, color=(1,0.5,0.2))

s=5.0

ball1.v=s*vector(0,-1,0)
ball2.v=s*vector(0,-1,0)
ball3.v=s*vector(0,-1,0)
ball4.v=s*vector(0,-1,0)
ball5.v=s*vector(0,-1,0)
ball6.v=s*vector(0,-1,0)
ball7.v=s*vector(0,-1,0)
ball8.v=s*vector(0,-1,0)
ball9.v=s*vector(0,-1,0)
ball10.v=s*vector(0,-1,0)

ballsList = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10]

t=0
dt=0.01

while 1:
    rate(100)
    for thisball in ballsList:
        thisball.pos=thisball.pos+thisball.v*dt
        if thisball.pos.x>10:
            thisball.pos=thisball.pos-thisball.v*dt
            thisball.v=s*vector(0,1,0)
        elif thisball.pos.x<-10:
            thisball.pos=thisball.pos-thisball.v*dt
            thisball.v=s*vector(0,-1,0)
        elif thisball.pos.y<-10:
            thisball.pos=thisball.pos-thisball.v*dt
            thisball.v=s*vector(1,0,0)
        elif thisball.pos.y>10:
            thisball.pos=thisball.pos-thisball.v*dt
            thisball.v=s*vector(-1,0,0)
            
    t=t+dt

