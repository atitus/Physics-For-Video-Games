from visual import *

track = box(pos=vector(0,-0.05,0), size=(3.0,0.05,0.1), color=color.white)
cart = box(pos=vector(-1.4,0,0), size=(0.1,0.04,0.05), color=color.green)

cart.m = 0.8
cart.v = vector(1.03,0,0)

dt = 0.01
t = 0

scene.mouse.getclick()

while cart.pos.x < 1.5 and cart.pos.x >-1.5:
	rate(100)
#	Fnet=vector(-0.15,0,0)
#	cart.v = cart.v + (Fnet/cart.m)*dt
	cart.pos = cart.pos + cart.v*dt
	t = t+dt

