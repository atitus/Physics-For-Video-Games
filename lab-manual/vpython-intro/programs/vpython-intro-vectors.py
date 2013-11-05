from __future__ import division
from visual import *

tennisball=sphere(pos=(0,6,0), radius=1, color=color.orange)

box(pos=(0,0,0), length=78, height=4, width=36, color=color.green)

print(tennisball.pos)

tennisball.pos=vector(32,7,-12)

print(tennisball.pos)
