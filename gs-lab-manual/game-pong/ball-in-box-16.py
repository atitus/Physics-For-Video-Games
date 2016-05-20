from visual import *

scene.range=10
scene.width=600
scene.height=600

boxcolor=color.yellow
ballcolor=color.white

#create graphical objects
ceiling=box(pos=(0,10,0), length=20,width=1,height=2, color=boxcolor)
floor=box(pos=(0,-10,0), length=20,width=1,height=2, color=boxcolor)
leftwall=box(pos=(-10,0,0), length=2, width=1, height=20, color=boxcolor)
rightwall=box(pos=(10,0,0), length=2, width=1, height=20, color=boxcolor)
ball=sphere(pos=(0,0,0), radius=0.5, color=ballcolor)

#define variables
ball.v=vector(5,8,0)
t=0
dt=0.01
COR=0.5

while 1:
    rate(100)

    #move ball
    ball.pos=ball.pos+ball.v*dt

    #check for collisions
    #ceiling
    if(ball.pos.y+ball.radius > ceiling.pos.y-ceiling.height/2):
        ball.v.y=-ball.v.y
    #floor
    elif(ball.pos.y-ball.radius < floor.pos.y+ceiling.height/2):
        ball.v.y=-ball.v.y
    #right wall
    elif((ball.pos.x+ball.radius)>rightwall.pos.x-rightwall.length/2):
        ball.v.x=-ball.v.x
    #left wall
    elif((ball.pos.x-ball.radius)<leftwall.pos.x+leftwall.length/2):
#        ball.v.x=-ball.v.x #elastic
        ball.pos=ball.pos-ball.v*dt
        ball.v.x=-COR*ball.v.x #inelastic

    
    t=t+dt
