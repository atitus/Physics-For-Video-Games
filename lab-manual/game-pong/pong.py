from visual import *

def pause():
    while True:
        rate(50)
        if scene.mouse.events:
            m = scene.mouse.getevent()
            if m.click == 'left': return
        elif scene.kb.keys:
            k = scene.kb.getkey()
            return

scene.range=20
scene.width=600
scene.height=450

boxcolor=color.yellow
ballcolor=color.white
paddlecolor=color.green

#create graphical objects
ceiling=box(pos=(0,12,0), length=50,width=1,height=2, color=boxcolor)
floor=box(pos=(0,-12,0), length=50,width=1,height=2, color=boxcolor)
ball=sphere(pos=(0,0,0), radius=0.5)

paddle2=box(pos=(18,0,0), length=0.5, width=1, height=5, color=paddlecolor)

leftwall1=box(pos=(-18,-7,0), length=0.5, width=1, height=10, color=boxcolor)
leftwall2=box(pos=(-18,7,0), length=0.5, width=1, height=10, color=boxcolor)

#set the initial velocity of the ball
initialVelocity=3*vector(-5,-4,0)
ball.velocity=initialVelocity

dt=0.01

#scores
player1score=0
player2score=0

pause()

while 1:
    while 1:
        rate(100)

        #move the ball
        ball.pos=ball.pos+ball.velocity*dt

        #check for collisions
        if(ball.pos.y+ball.radius > ceiling.pos.y-ceiling.height/2):
            ball.pos=ball.pos-ball.velocity*dt
            ball.velocity.y=-ball.velocity.y
        if(ball.pos.y-ball.radius < floor.pos.y+ceiling.height/2):
            ball.pos=ball.pos-ball.velocity*dt
            ball.velocity.y=-ball.velocity.y

        if((ball.pos.x+ball.radius)>paddle2.pos.x-paddle2.length/2):
            if(ball.pos.y<paddle2.pos.y+paddle2.height/2 and ball.pos.y>paddle2.pos.y-paddle2.height/2):
                ball.pos=ball.pos-ball.velocity*dt
                ball.velocity.x=-ball.velocity.x

        if((ball.pos.x-ball.radius)<leftwall1.pos.x+leftwall1.length/2):
            if(ball.pos.y<leftwall1.pos.y+leftwall1.height/2 and ball.pos.y>leftwall1.pos.y-leftwall1.height/2):
                ball.pos=ball.pos-ball.velocity*dt
                ball.velocity.x=-ball.velocity.x
            elif(ball.pos.y<leftwall2.pos.y+leftwall2.height/2 and ball.pos.y>leftwall2.pos.y-leftwall2.height/2):
                ball.pos=ball.pos-ball.velocity*dt
                ball.velocity.x=-ball.velocity.x
            
        #check to see if ball is at edge of window
        if(ball.pos.x>18):
            player1score = player1score + 1
            print("\nscore: player1=", player1score, ", player2=", player2score)
            break
            
        if(ball.pos.x<-18):
            player2score = player2score + 1
            print("\nscore: player1=", player1score, ", player2=", player2score)
            break

        #get mouse position and move paddle2
        mouse=scene.mouse.pos
        if(mouse.y-paddle2.height/2>floor.y+floor.height/2 and mouse.y+paddle2.height/2<ceiling.pos.y-ceiling.height/2):
            paddle2.pos.y=mouse.y
        else:
            if(mouse.y-paddle2.height/2<floor.y+floor.height/2):
#                paddle2.pos.y=floor.y+floor.height/2+paddle2.height/2
                paddle2.pos=(18,0,0)
            elif(mouse.y+paddle2.height/2>ceiling.y-floor.height/2):
#                paddle2.pos.y=ceiling.y-ceiling.height/2-paddle2.height/2
                paddle2.pos=(18,0,0)


    ball.pos=vector(0,0,0)
    ball.velocity=-ball.velocity
    paddle2.pos=vector(18,0,0)
    pause()
