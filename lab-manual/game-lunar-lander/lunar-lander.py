from __future__ import division
from visual import *

scene.range=20

ground = box(pos=vector(0,-10.05,0), size=(40.0,1,1), color=color.white)
spaceship = box(pos=vector(0,8,0), size=(2,5,2), color=color.yellow)

spaceship.m = 1
spaceship.v = vector(0,0,0)
g=1/6*vector(0,-10,0)
Fthrust=vector(0,0,0)

dt = 0.01
t = 0

scale=5.0
FgravArrow = arrow(pos=spaceship.pos, axis=scale*spaceship.m*g, color=color.red)
FthrustArrow = arrow(pos=spaceship.pos, axis=Fthrust, color=color.cyan)


#scene.mouse.getclick()

while 1:
        rate(100)
        Fgrav=spaceship.m*g
        if scene.kb.keys:
            k = scene.kb.getkey()
            if k == "up":
                Fthrust=vector(0,4,0)
            else:
                Fthrust=vector(0,0,0)
        Fnet=Fgrav+Fthrust
        spaceship.v = spaceship.v + (Fnet/spaceship.m)*dt
        spaceship.pos = spaceship.pos + spaceship.v*dt
        if(spaceship.pos.y-spaceship.height/2<ground.pos.y+ground.height/2):
                print("spaceship has landed, v= ", mag(spaceship.v))
                break
        t = t+dt
        FgravArrow.pos=spaceship.pos
        FgravArrow.axis=scale*Fgrav
        FthrustArrow.pos=spaceship.pos
        FthrustArrow.axis=scale*Fthrust
