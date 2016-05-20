from visual import *

def rad(degrees): #converts an angle in degrees to an angle in radians
    radians=degrees*pi/180
    return radians

scene.range=20
scene.width=800
scene.height=800

#create objects
ground = box(pos=vector(0,-15,0), size=(40.0,1,2), color=color.green)
tank = box(pos=vector(-18,-13,0), size=(2,2,2), color=color.yellow)
turret = cylinder(pos=tank.pos, axis=(0,0,0), radius=0.5, color=tank.color)
turret.pos.y=turret.pos.y+tank.height/2
angleBar = cylinder(pos=vector(-18,-19,0), axis=(1,0,0), radius=1, color=color.magenta)
speedBar = cylinder(pos=vector(5,-19,0), axis=(1,0,0), radius=1, color=color.cyan)

#turret
theta=rad(45)
dtheta=rad(1)
L=3
turret.axis=L*vector(cos(theta),sin(theta),0)

#bullets
bulletsList=[]
m=1
muzzlespeed=15
dspeed=1

#Bar
angleBar.axis=(5*theta)*vector(1,0,0)
speedBar.axis=(muzzlespeed/2+0.5)*vector(1,0,0)

#motion
g=vector(0,-10,0)
dt = 0.01
t = 0

while 1:
    scene.mouse.getclick()
    while 1:
        rate(100)
        if scene.kb.keys:
            k = scene.kb.getkey()
            if k == "up":
                theta=theta+dtheta
                turret.axis=L*vector(cos(theta),sin(theta),0)
                angleBar.axis=(5*theta)*vector(1,0,0)
            elif k == "down":
                theta=theta-dtheta
                turret.axis=L*vector(cos(theta),sin(theta),0)
                angleBar.axis=(5*theta)*vector(1,0,0)
            elif k == "left":
                muzzlespeed=muzzlespeed-dspeed
                speedBar.axis=(muzzlespeed/2+0.5)*vector(1,0,0)
            elif k == "right":
                muzzlespeed=muzzlespeed+dspeed
                speedBar.axis=(muzzlespeed/2+0.5)*vector(1,0,0)
            elif k==" ":
                bullet=sphere(pos=turret.pos+turret.axis, radius=0.5, color=color.white)
                bullet.v=muzzlespeed*vector(cos(theta),sin(theta),0)
                bulletsList.append(bullet)
            elif k=="Q":
                break

        if muzzlespeed>20:
            muzzlespeed=20
        if muzzlespeed<1:
            muzzlespeed=1
        if theta>rad(90):
            theta=rad(90)
        if theta<0:
            theta=0

        for thisbullet in bulletsList:
            if(thisbullet.pos.y<ground.y+ground.height/2):
                thisbullet.Fnet=vector(0,0,0)
                thisbullet.v=vector(0,0,0)
            else:
                thisbullet.Fnet=m*g
            thisbullet.v=thisbullet.v+thisbullet.Fnet/m*dt
            thisbullet.pos=thisbullet.pos+thisbullet.v*dt

        t=t+dt
