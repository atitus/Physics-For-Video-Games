from visual import *

def collisionSpheres(sphere1, sphere2):
    dist=mag(sphere1.pos-sphere2.pos)
    if(dist<sphere1.radius+sphere2.radius):
        return True
    else:
        return False

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

shooter=box(pos=(-4.5,-4.5,0), width=1, height=1, length=1, color=color.red)
shooter.v=2*vector(1,0,0)

bulletsList=[]

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

    if scene.kb.keys:
            k = scene.kb.getkey()
            if k == "right":
                shooter.v=2*vector(1,0,0)
            elif k == "left":
                shooter.v=2*vector(-1,0,0)
            elif k==" ":
                bullet=sphere(pos=shooter.pos, radius=0.1, color=color.white)
                bullet.v=shooter.v + 5*vector(0,1,0)
#                bullet.v=5*vector(0,1,0)
                bulletsList.append(bullet)
            else:
                shooter.v=vector(0,0,0)
    shooter.pos = shooter.pos + shooter.v*dt

    for thisbullet in bulletsList:
        thisbullet.pos=thisbullet.pos+thisbullet.v*dt
        for thisball in ballsList:
            if collisionSpheres(thisbullet, thisball):
                thisball.pos=vector(0,-10,0)
                thisball.v=vector(0,0,0)

    t=t+dt

