from __future__ import division
from visual import *
from visual.graph import *
from physutil import *

scene.background=color.white
#scene.width=700
#scene.height=200

missile=sphere(pos=(500,500,0), radius=0.4, color=color.red)
xaxis=arrow(pos=(-10,0,0), axis=(20,0,0), color=(0,0,0), shaftwidth=0.01, opacity=0.2)
yaxis=arrow(pos=(0,-10,0), axis=(0,20,0), color=xaxis.color, shaftwidth=xaxis.shaftwidth, opacity=xaxis.opacity)

v=vector(-43,-25,0)

dt=2
t=0

print("\hline \n", t , " & (",missile.pos.x,",",missile.pos.y,")"," \\\\")

while t<25:
    missile.pos=missile.pos + v*dt
    sphere(pos=missile.pos, radius=missile.radius, color=color.red, opacity=0.4)
    t=t+dt
    print("\hline \n", t , " & (",missile.pos.x,",",missile.pos.y,")"," \\\\")
