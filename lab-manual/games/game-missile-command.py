from __future__ import division
from visual import *
from random import *

#Aaron Titus, Physics for Video Games
#
#Missile Command
#
#Click the mouse or press a key to begin.
#Click to launch a missile that will explode at the location of the click.
#Protect the bases.
#

#pause and wait for mouse or keyboard event, then continue
def pause():
    while True:
        rate(50)
        if scene.mouse.events:
            m = scene.mouse.getevent()
            if m.click == 'left': return
        elif scene.kb.keys:
            k = scene.kb.getkey()
            return

#creates a missile that is directed from a random source to a random silo
#returns a sphere
def createMissile():
    silo=silos[randint(1,numSilos)-1]
    source=sources[randint(1,numSources)-1]
    unitVector=norm(silo.pos-source.pos)
    missileSpeed=randint(1,5)*10
    missile=sphere(radius=10, pos=source.pos, color=color.yellow)
    missile.velocity=missileSpeed*unitVector
    missile.trail = curve(color = missile.color, radius = 10)
    missile.exploded=False #flag for whether missile has collided or not
    missiles.append(missile)
    return missile

#creates a bullet that travels to the given target from the ground at x=0
#returns a sphere
def createBullet(target):
    bullet=sphere(radius=10, pos=(0,ground.pos.y+ground.height/2,0), color=color.white)
    direction=norm(target-bullet.pos)
    bullet.velocity=bulletSpeed*direction
    bullet.trail = curve(color = bullet.color, radius = 10)
    bullet.target=target
    bullet.exploded=False #flag for whether bullet has collided or not
    bullets.append(bullet)
    return bullet

#creates an explosion at the given target, with a timestamp
def createExplosion(target,time):
    explosion=sphere(radius=explosionRadius, pos=target, color=color.white, opacity=0.5)
    explosion.time=time
    explosion.active=True #flag for whether explosion is active or not
    explosions.append(explosion)

#determines whether two spheres intersect or not
#returns boolean
def collisionSpheres(sphereObj1, sphereObj2):
    dist=mag(sphereObj1.pos-sphereObj2.pos)
    if(dist<sphereObj1.radius+sphereObj2.radius):
        return True
    else:
        return False

#determines whether a point is within a sphere or not
#returns boolean
def collisionSphereAndPoint(sphereObj, targetVector):
    dist=mag(sphereObj.pos-targetVector)
    if(dist<sphereObj.radius):
        return True
    else:
        return False

#determines whether a sphere and box intersect or not
#returns boolean
def collisionSphereAndBox(sphereObj, boxObj):
    result=True
    if((sphereObj.pos.x-sphereObj.radius<boxObj.pos.x+boxObj.length/2 and sphereObj.pos.x+sphereObj.radius>boxObj.pos.x-boxObj.length/2) and (sphereObj.pos.y-sphereObj.radius<boxObj.pos.y+boxObj.height/2 and sphereObj.pos.y+sphereObj.radius>boxObj.pos.y-boxObj.height/2)):
        result=True
        dist=sqrt((sphereObj.pos.x-boxObj.pos.x)**2+(sphereObj.pos.y-boxObj.pos.y)**2)
        if(dist>sphereObj.radius+sqrt((boxObj.length/2)**2+(boxObj.width/2)**2)):
            result=False
        return result
    else:
        result=False
    return result

#determines whether a sphere intersects with any box in a list
#returns -1 if there is no intersection; otherwise it returns the last index of the object in the list that intersects with the sphere
def collisionSphereAndBoxList(sphereObj, boxList):
    result=-1
    i=0
    for b in boxList:
        if collisionSphereAndBox(sphereObj,b):
            result=i
            break
        i=i+1
    return result

#determines whether a sphere intersects with another sphere in a list
#returns -1 if there is no intersection; otherwise it returns the last index of the object in the list that intersects with the sphere
def collisionSphereAndSphereList(sphereObj, sphereList):
    result=-1
    i=0
    for s in sphereList:
        if collisionSpheres(sphereObj,s):
            result=i
            break
        i=i+1
    return result


#global lists
missiles=[] #air missiles
bullets=[] #used to shoot down the missiles
silos=[] #houses on the ground
sources=[] #sources of air missiles
explosions=[] #explosions of bullets

#initialize the seed used for the random number generator
#if null argument, it uses the system timestamp
seed()

#scene
#do not change these values because they are hardcoded in this version (sorry)
scene.range=1000
scene.width=600
scene.height=600

numSilos=6 #silos on the ground
numSources=5 #sources of air missiles
explosionTime=10 #time lag in seconds for the explosion
explosionRadius=50 #radius of explosion
bulletSpeed=100 #speed of the bullets

#create the ground
ground=box(pos=(0,-950,0), length=3000, width=10, height=100, color=color.green)

#create silos
for i in range(1,numSilos+1,1):
    s=box(pos=(-1000+i/(numSilos+1)*2000,ground.pos.y+ground.height/2+50,0), length=100, width=10, height=100, color=color.white)
    silos.append(s)

#create sources of missiles
for i in range(1,numSources+1,1):
    s=box(pos=(-1000+i/(numSources+1)*2000,1000,0), length=1, width=1, height=1, color=color.black)
    sources.append(s)

dt=0.1
t=0
visibleSilos=len(silos) #number of unexploded silos remaining

print("press a key to begin")

pause()

while 1:
    rate(100)

    #create a missile with a random delay
    if (randint(1,200)<2 or t==0):
        createMissile()

    #create a bullet with a target of the mouse click
    if scene.mouse.clicked:
        m = scene.mouse.getclick()
        createBullet(m.pos)

    #loop through all missiles
    for m in missiles:
        if(m.exploded==False): #only look at unexploded missiles (in the air)
            m.pos=m.pos+m.velocity*dt #update position of missile
            m.trail.append(pos=m.pos) #update the trail

            #check for collision with the ground
            if (m.pos.y-m.radius<ground.pos.y+ground.height/2):
                m.velocity=vector(0,0,0)
                m.visible=0
                m.trail.visible=0
                m.exploded=True

            #check for collision with a silo
            collisionWithSilo=collisionSphereAndBoxList(m,silos)
            if (collisionWithSilo!=-1):
                silos[collisionWithSilo].visible=0
                m.velocity=vector(0,0,0)
                m.visible=0
                m.trail.visible=0
                m.exploded=True

            #check for collision with an exploding bullet (explosion)
            collisionWithExplosion=collisionSphereAndSphereList(m,explosions)
            if (collisionWithExplosion!=-1):
                if (explosions[collisionWithExplosion].active==True):
                    m.velocity=vector(0,0,0)
                    m.visible=0
                    m.trail.visible=0
                    m.exploded=True
                    explosions[collisionWithExplosion].active=False
                    explosions[collisionWithExplosion].visible=0

    #loop through all bullets  
    for b in bullets:
        if(b.exploded==False):
            b.pos=b.pos+b.velocity*dt
            b.trail.append(pos=b.pos)

            #check if the bullet goes off screen
            if(b.pos.x+b.radius>scene.range.x or b.pos.y+b.radius>scene.range.y):
                b.velocity=vector(0,0,0)
                b.visible=0
                b.trail.visible=0
                b.exploded=True

            #check if the bullet is at the location of the target
            # if so, create an explosion
            if(collisionSphereAndPoint(b,b.target)):
                b.exploded=True
                b.velocity=vector(0,0,0)
                b.visible=0
                b.trail.visible=0
                createExplosion(b.target,t)

    #loop through all explosions
    for ex in explosions:
        if(ex.active==True):
            if(t>ex.time+explosionTime):
                ex.visible=0
                ex.active=False

    #check all visible silos to see if game is over
    visibleSilos=len(silos)
    for s in silos:
        if s.visible==0:
            visibleSilos=visibleSilos-1
    if visibleSilos==0:
        print("\n game over")
        break

    t=t+dt
