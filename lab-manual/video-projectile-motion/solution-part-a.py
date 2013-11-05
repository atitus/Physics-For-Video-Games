from __future__ import division
from visual import *

scene.background=color.white
#scene.width=700
#scene.height=200

ball=sphere(pos=(0.52,2.66,0), radius=0.05, color=color.red)
#xaxis=arrow(pos=(-10,0,0), axis=(20,0,0), color=(0,0,0), shaftwidth=0.01, opacity=0.2)
#yaxis=arrow(pos=(0,-10,0), axis=(0,20,0), color=xaxis.color, shaftwidth=xaxis.shaftwidth, opacity=xaxis.opacity)

v=vector(3.07,4.52,0)
F=vector(0,-9.8,0)
m=1

dt=0.05
t=0

#print("\hline \n ", t, " & (",ball.pos.x,",",ball.pos.y,")"," \\\\")
print(t, ball.pos, v)

while v.y>0:
    v=v+F/m*dt
    ball.pos=ball.pos + v*dt
    sphere(pos=ball.pos, radius=ball.radius, color=color.red, opacity=0.4)
    t=t+dt
#    print("\hline \n ", t, " & (",v.x,",",v.y,")", " & (",ball.pos.x,",",ball.pos.y,")" ," \\\\")
    print(t,ball.pos,v)
