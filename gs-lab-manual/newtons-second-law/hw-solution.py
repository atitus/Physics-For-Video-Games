from __future__ import division
from visual import *
from visual.graph import *
from physutil import *

scene.background=color.white
#scene.width=700
#scene.height=200

ball=sphere(pos=(-4.5,0,0), radius=0.05, color=color.red)
#xaxis=arrow(pos=(-10,0,0), axis=(20,0,0), color=(0,0,0), shaftwidth=0.01, opacity=0.2)
#yaxis=arrow(pos=(0,-10,0), axis=(0,20,0), color=xaxis.color, shaftwidth=xaxis.shaftwidth, opacity=xaxis.opacity)

v=vector(5.74,8.19,0)
F=vector(0,-10,0)
m=1

dt=0.25
t=0

#print("\hline \n ", t, " & (",ball.pos.x,",",ball.pos.y,")"," \\\\")
print(t, ball.pos, v)

while t<1.6:
    v=v+F/m*dt
    ball.pos=ball.pos + v*dt
    sphere(pos=ball.pos, radius=ball.radius, color=color.red, opacity=0.4)
    t=t+dt
#    print("\hline \n ", t, " & (",v.x,",",v.y,")", " & (",ball.pos.x,",",ball.pos.y,")" ," \\\\")
    print(t,ball.pos,v)
