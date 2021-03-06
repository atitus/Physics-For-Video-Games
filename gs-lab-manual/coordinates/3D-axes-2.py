from visual import *

scene.range=0.8

xaxis = arrow(pos=(-0.5,0,0), axis=(1,0,0), shaftwidth=0.05)
yaxis = arrow(pos=(0,-0.5,0), axis=(0,1,0), shaftwidth=0.05)
zaxis = arrow(pos=(0,0,-0.5), axis=(0,0,1), shaftwidth=0.05)

xlabel=label(pos=xaxis.pos+xaxis.axis+vector(0.1,0,0), text="+x")
ylabel=label(pos=yaxis.pos+yaxis.axis+vector(0,0.1,0), text="+y")
zlabel=label(pos=zaxis.pos+zaxis.axis+vector(0,0,0.1), text="+z")
