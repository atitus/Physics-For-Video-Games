from visual import *

scene.range=20
scene.width=700
scene.height=700

ground = box(pos=vector(0,0,0), size=(40,40,1), color=color.green)
ball = sphere(pos=vector(-18,0,0), radius=0.5, color=color.white)
ground.pos.z=ground.pos.z-ground.width/2-ball.radius
hole = cylinder(pos=(15,0,ground.pos.z+ground.width/2),axis=vector(0,0,1), radius=3*ball.radius, color=(0.8,0.8,0.8))
hole.pos.z=hole.pos.z-mag(hole.axis)*0.9
putt = arrow(pos=ball.pos, axis=(0,0,0), shaftwidth=0.5, color=color.yellow)

#ball, friction, and grav
ball.m=0.045
g=10
mu=0.1

#speed
initialspeed=5

#velocity vector
scale=initialspeed
putt.axis=scale*vector(1,0,0)
ball.v=initialspeed*vector(1,0,0)


#clock
dt=0.01
t=0

scene.mouse.getclick()

while 1:
        rate(100)

        vhat=ball.v/mag(ball.v)
        Fnet=-mu*ball.m*g*vhat
        ball.v=ball.v+Fnet/ball.m*dt
        ball.pos=ball.pos+ball.v*dt
        putt.pos=ball.pos

        scale=mag(ball.v)
        putt.axis=scale*vector(1,0,0)

        t=t+dt

