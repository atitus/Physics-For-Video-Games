from visual import *

def rad(degrees): #converts an angle in degrees to an angle in radians
    radians=degrees*pi/180
    return radians

scene.range=20
scene.width=800
scene.height=800

#tilt angle
phi=rad(20)

#create objects
ground = box(pos=vector(0,0,0), size=(40,1,40), color=color.green)
ramp = box(pos=vector(0,20*sin(phi),-40*cos(phi)), size=(40.0,1,40), axis=(0,sin(phi),-cos(phi)), color=color.white, material=materials.wood)
ramp2 = box(pos=vector(0,20*sin(phi),40*cos(phi)), size=(40.0,1,40), axis=(0,sin(phi),cos(phi)), color=color.white, material=materials.wood)
ball = sphere(pos=vector(-15,0,0), radius=1, color=color.white)
#xaxis = arrow(pos=vector(0,0,0), axis=20*vector(1,0,0), color=color.white)
#yaxis = arrow(pos=vector(0,0,0), axis=20*vector(0,1,0), color=color.white)

#
theta=rad(90)
ball.r=vector(-20,ball.radius+ground.height/2,0)
ball.pos=ball.r
launchspeed=5
ball.v=launchspeed*vector(0,0,-1)
m=1
g=vector(0,-10,0)
t=0
dt=0.1

#scene.mouse.getclick()
##xaxis.axis=rotate(xaxis.axis,-(pi/2-phi),vector(1,0,0))
##yaxis.axis=rotate(yaxis.axis,-(pi/2-phi),vector(1,0,0))

while 1:
#    rate(100)
    scene.mouse.getclick()
    if(ball.pos.z<-20):
        alpha=-(pi/2-phi)
        Fnet=m*g*sin(phi)
        ball.v=rotate(ball.v,alpha,vector(1,0,0))
    elif(ball.pos.z>20):
        alpha=(pi/2-phi)
        Fnet=m*g*sin(phi)
        ball.v=rotate(ball.v,alpha,vector(1,0,0))
    else:
        alpha=rad(0)
        Fnet=vector(0,0,0)
        
    ball.v=ball.v+Fnet/m*dt
    ball.r=ball.r+ball.v*dt
    ball.pos=rotate(ball.r,alpha,vector(1,0,0))
#    ground.axis=rotate(ground.axis,phi,vector(1,0,0))    
