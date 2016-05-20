from __future__ import division
from visual import *
from visual.graph import *

#print "If clickToAdvance==true, then click on the scene to advance the simulation to the next calculation."

#print "Change clickToAdvance to false if you want the program to advance automatically."

#set this to true if you want to click to advance through the calculations and steps
#set this to false if you want it to advance automatically
clickToAdvance=true

t = 0

#use case 1 if clicking to advance
#use any case if not clicking to advance
case=1

if(case==1):
        dt = 0.25
        max=100
        rateTime=100

if(case==2):
        dt = 0.1
        max=2
        rateTime=100

if(case==3):
        dt = 0.01
        max=2
        rateTime=1000


floor = box(pos=vector(0,0,0), size=(20.0,0.05,10), color=color.green)
ball = sphere(pos=vector(-4.5,0.1,0), radius=0.4, color=color.white, opacity=0.5)

ball.m = 0.8
ball.v = vector(5.74,8.19,0)
ball.p = ball.m * ball.v
g = 9.8

scene.range=ball.radius*12
scene.background=color.black

trail=curve(color=ball.color)
trail.append(pos=ball.pos)

zeroVector=vector(0,0,0)

arrowScale=mag(scene.range)/mag(ball.v)/5
vArrow=arrow(pos=ball.pos, axis=vector(0,0,0), color=color.yellow, shaftwidth=0.1)
dvArrow=arrow(pos=vArrow.pos+vArrow.axis, axis=vector(0,0,0), color=color.magenta, shaftwidth=5)
vfArrow=arrow(pos=ball.pos, axis=vector(0,0,0), color=color.cyan, shaftwidth=0.1)
drArrow=arrow(pos=ball.pos,axis=vector(0,0,0), color=ball.color, shaftwidth=0.1)

print(t,ball.pos, ball.v)

if(clickToAdvance==false):
        scene.mouse.getclick()

while ball.pos.y>0:
        rate(10)
        if(clickToAdvance==true):
                scene.mouse.getclick()
        vArrow.pos=ball.pos
        vArrow.axis=ball.v*arrowScale
        if(clickToAdvance==false):
                for i in range(0,max):
                        rate(rateTime)
        Fnet=vector(0,-ball.m*g,0)
        ball.p = ball.p + Fnet*dt
        ball.v = ball.p/ball.m
        dv = Fnet/ball.m*dt
        dr = ball.v*dt

        if(clickToAdvance==true):
                scene.mouse.getclick()
        dvArrow.pos=vArrow.pos+vArrow.axis
        dvArrow.axis=dv*arrowScale
        if(clickToAdvance==false):
                for i in range(0,max):
                        rate(rateTime)

        if(clickToAdvance==true):
                scene.mouse.getclick()
        vfArrow.pos=ball.pos
        vfArrow.axis=vArrow.axis+dvArrow.axis
        if(clickToAdvance==false):
                for i in range(0,max):
                        rate(rateTime)

        if(clickToAdvance==true):
                scene.mouse.getclick()

        drArrow.pos=ball.pos
        drArrow.axis=dr

        if(clickToAdvance==false):
                for i in range(0,max):
                        rate(rateTime)
        if(clickToAdvance==true):
                scene.mouse.getclick()

        vArrow.axis=zeroVector
        dvArrow.axis=zeroVector
        vfArrow.axis=zeroVector
        ball.pos=ball.pos+ball.v*dt
        t = t+dt
        trail.append(pos=ball.pos)

        print(t,ball.pos, ball.v)
