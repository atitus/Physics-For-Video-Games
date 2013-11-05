from __future__ import division
from visual import *
from visual.graph import *
from physutil import *

scene.background=color.white
scene.width=700
scene.height=200

# Define track and cart objects
track = box(pos=vector(0,-0.05,0), size=(3.0,0.05,.10), color=(0.8,0.8,0.8))
cart = box(pos=vector(-1.0,0,0), size=(0.3,0.08,0.12), color=color.green)
cart.pos.y=track.pos.y+track.height/2+cart.height/2
dot = sphere(pos=cart.pos+vector(0,0,cart.width/2), color=color.orange, radius=cart.length/10)

# Define axis
#axis = PhysAxis(track, 10, axisColor=color.black, labels=["10","20","30","40","50"])

# Set up graph window
#graph = PhysGraph()

# Set up cart velocity and verify
mcart = 0.80
vcart = vector(0.5,0,0)
print('cart velocity =', vcart)

# Set up timing data
deltat = 0.01
t = 0
tf = 4

# Set up motion map
motionMap = MotionMap(cart, tf, 5, markerType="breadcrumbs", markerScale=1, markerColor=color.orange, labelMarkerOffset=vector(0,0.3,0), labelColor=color.black)

# Main update loop; perform physics updates and drawing
while t < tf:

    # Required to make animation visible / refresh smoothly
    rate(100)
   
    # Update and draw motion map artifacts
    motionMap.update(t)

    # Cart physics update
    cart.pos = cart.pos + vcart*deltat
    dot.pos = dot.pos + vcart*deltat

    # Update timer
    t = t+deltat
#    timerDisplay.update(t)

    # Update graph plot
#    graph.plot(t, cart.pos.x)

# Verify final results!
print("final velocity = ",vcart)
print("final position = ", cart.pos)
