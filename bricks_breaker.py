import turtle as t
import random

screen_x = 10
screen_y = 600

wn = t.Screen()
wn.bgcolor('black')
wn.setup(screen_x,screen_y)
wn.tracer(2)

dscreen_x = 10

##### draw bricks #####

brick1,brick2,brick3,brick4 = [],[],[],[]
bricksholder = [brick1,brick2,brick3,brick4]
colors = ["tomato", "orchid", "snow2", "yellow", "tan"]
wn.register_shape('brick',((0,0),(10,0),(10,40),(0,40)))
for bricks in bricksholder:
    for i in range(11):
        bricks.append(t.Turtle())

posx = -27.5
posy = 170
for bricks in bricksholder:
    for brick in bricks:
        brick.speed(0)
        brick.color(random.choice(colors))
        brick.penup()
        brick.shape('brick')
        brick.setpos(posx*10,posy)
        posx+=5
    posx=-27.5
    posy+=20


##### draw Ball #####

x = 0
y = -200
dx = random.randint(3,8)
dy = random.randint(5,8)

ball = t.Turtle()
ball.penup()
ball.speed(0)
ball.color('deep pink')
ball.shape('circle')
ball.setpos(x,y)


##### Draw Player #####

px = 0
py = -250

player = t.Turtle()
player.penup()
player.speed(0)
player.color('blue')
player.shapesize(0.5,5,5)
player.shape('square')
player.setpos(px,py)


##### Score #####

scores = 0
score = t.Turtle()
score.penup()
score.speed(0)
score.color('cyan')
score.setpos(-240,260)
score.hideturtle()
score.write("SCORE: "+str(scores),move=False,align='center',font=('arial',15,'bold'))


##### Lives #####

lives = 3
life = t.Turtle()
life.penup()
life.speed(0)
life.color('magenta')
life.setpos(240,260)
life.hideturtle()
life.write("LIVES: "+str(lives),move=False,align='center',font=('arial',15,'bold'))


##### Paddle movement #####

def right():
    px = player.xcor()
    px+=50
    player.setpos(px,py)

def left():
    px = player.xcor()
    px-=50
    player.setpos(px,py)

wn.listen()
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")


##### Main Loop #####

while True:
    screen_x += dscreen_x
    if screen_x > 600:
        dscreen_x = 0
        if ball.xcor()>280 or ball.xcor()<-280:
            dx=-dx
        if ball.ycor()>280: #or ball.ycor()<-280:
            dy=-dy
        if y<-280:
            x=0
            y=0
            dx = random.randint(3,8)
            dy = random.randint(5,8)
            ball.setpos(x,y)
            lives-=1
            life.clear()
            life.write("LIVES: "+str(lives),move=False,align='center',font=('arial',15,'bold'))
            if lives==0:
                wn.clear()
                t.color('black')
                t.write('GAME OVER NO LIFE',align='center',font=('arial',25,'bold'))
                t.hideturtle()
                break


        if ((ball.xcor()<player.xcor()+70) and (ball.xcor()>player.xcor()-70) and (ball.ycor()<player.ycor()+20) and (ball.ycor()>player.ycor()-20)):
            dy=-dy

        for bricks in bricksholder:
            for brick in bricks:
                if brick.isvisible():
                    if ((ball.xcor()>brick.xcor()-20) and (ball.xcor()<brick.xcor()+20) and (ball.ycor()<brick.ycor()+20) and (ball.ycor()>brick.ycor()-20)):
                        brick.hideturtle()
                        scores+=5
                        score.clear()
                        score.write("SCORE: "+str(scores),move=False,align='center',font=('arial',15,'bold'))
                        dy=-random.randint(5,8)
                        # print("collision")
                        if scores == 135:
                            wn.clear()
                            t.color('green')
                            t.write('WINNER',align='center',font=('arial',25,'bold'))
                            t.hideturtle()
                            break
        
        x = int(ball.xcor())
        x+=dx
        y = int(ball.ycor())
        y+=dy
        ball.setpos(int(x),int(y))

        if player.xcor()>250:
            player.setpos(250,py)

        if player.xcor()<-250:
            player.setpos(-250,py)

    wn.setup(screen_x,screen_y)
    wn.update()

t.done()