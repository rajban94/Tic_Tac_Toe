import turtle as t

w = t.Screen()
w.bgcolor('black')

b = t.Turtle()
b.color('white')
b.penup()
b.goto(-150,150)
b.pendown()
b.speed(0)
b.hideturtle()

t1 = t.Turtle()
t1.left(90)
t1.color('white')
t1.speed(0)

global tog,pos,box1,box2,box3,box4,box5,box6,box7,box8,box9,row1,row2,row3,col1,col2,col3,dia1,dia2,circle_won,cross_won

def start_play_again():
    global tog,pos,box1,box2,box3,box4,box5,box6,box7,box8,box9,row1,row2,row3,col1,col2,col3,dia1,dia2,circle_won,cross_won
    tog = 0
    box1,box2,box3,box4,box5,box6,box7,box8,box9 = 0,0,0,0,0,0,0,0,0
    circle_won,cross_won = 0,0
    row1,row2,row3,col1,col2,col3,dia1,dia2 = [],[],[],[],[],[],[],[]

def draw(x,y):
    global tog,pos,box1,box2,box3,box4,box5,box6,box7,box8,box9,row1,row2,row3,col1,col2,col3,dia1,dia2,circle_won,cross_won
    
    if(-330 < x < -180 and 20 < y < 50):
        t1.reset()
        t1.left(90)
        t1.color("white")
        t1.speed(0)
        start_play_again()
        t1.hideturtle()

    if (-150 < x < -50 and 50 < y < 150 and box1 == 0): #1
        pos = (-130,100)
        box1 = 1
        if (tog == 0):
            row1.append(0)
            col1.append(0)
            dia1.append(0)
        else:
            row1.append(1)
            col1.append(1)
            dia1.append(1)
        cir_or_cross()
        
    if (-50 < x < 50 and 50 < y < 150 and box2 ==0): #2
        pos = (-30,100)
        box2 = 1
        if (tog == 0):
            row1.append(0)
            col2.append(0)
        else:
            row1.append(1)
            col2.append(1)
        cir_or_cross()

    if (50 < x < 150 and 50 < y < 150 and box3 ==0): #3
        pos = (70,100)
        box3 = 1
        if(tog == 0):
            row1.append(0)
            col3.append(0)
            dia2.append(0)
        else:
            row1.append(1)
            col3.append(1)
            dia2.append(1)
        cir_or_cross()

    if (-150 < x < -50 and -50 < y < 50 and box4 ==0): #4
        pos = (-130,0)
        box4 = 1
        if(tog == 0):
            row2.append(0)
            col1.append(0)
        else:
            row2.append(1)
            col1.append(1)
        cir_or_cross()
        
    if (-50 < x < 50 and -50 < y < 50 and box5 ==0): #5
        pos = (-30,0)
        box5 = 1
        if(tog == 0):
            row2.append(0)
            col2.append(0)
            dia1.append(0)
            dia2.append(0)
        else:
            row2.append(1)
            col2.append(1)
            dia1.append(1)
            dia2.append(1)
        cir_or_cross()

    if (50 < x < 150 and -50 < y < 50 and box6 ==0): #6
        pos = (70,0)
        box6 = 1
        if(tog == 0):
            row2.append(0)
            col3.append(0)   
        else:
            row2.append(1)
            col3.append(1)
        cir_or_cross()

    if (-150 < x < -50 and -150 < y < -50 and box7 ==0): #7
        pos = (-130,-100)
        box7 = 1
        if(tog == 0):
            row3.append(0)
            col1.append(0)
            dia2.append(0)
        else:
            row3.append(1)
            col1.append(1)
            dia2.append(1)
        cir_or_cross()
        
    if (-50 < x < 50 and -150 < y <- 50 and box8 ==0): #8
        pos = (-30,-100)
        box8 = 1
        if(tog == 0):
            row3.append(0)
            col2.append(0) 
        else:
            row3.append(1)
            col2.append(1)
        cir_or_cross()

    if (50 < x < 150 and -150 < y < -50 and box9 ==0): #9
        pos = (70,-100)
        box9 = 1
        if(tog == 0):
            row3.append(0)
            col3.append(0)
            dia1.append(0)
        else:
            row3.append(1)
            col3.append(1)
            dia1.append(1)
        cir_or_cross()

    if(len(row1) == 3):
        if(row1[0] == row1[1] == row1[2]):
            draw_grid_line((-145,100),90,t1,290)
            if(row1[0] == 0):
                circle_won = 1
            else:
                cross_won = 1
                
    if(len(row2) == 3):
        if(row2[0] == row2[1] == row2[2]):
            draw_grid_line((-145,0),90,t1,290)
            if(row2[0] == 0):
                circle_won = 1
            else:
                cross_won = 1

    if(len(row3) == 3):
        if(row3[0] == row3[1] == row3[2]):
            draw_grid_line((-145,-100),90,t1,290)
            if(row3[0] == 0):
                circle_won = 1
            else:
                cross_won = 1

    if(len(col1) == 3):
        if(col1[0] == col1[1] == col1[2]):
            draw_grid_line((-100,145),180,t1,290)
            if(col1[0] == 0):
                circle_won = 1
            else:
                cross_won = 1

    if(len(col2) == 3):
        if(col2[0] == col2[1] == col2[2]):
            draw_grid_line((0,145),180,t1,290)
            if(col2[0] == 0):
                circle_won = 1
            else:
                cross_won = 1

    if(len(col3) == 3):
        if(col3[0] == col3[1] == col3[2]):
            draw_grid_line((100,145),180,t1,290)
            if(col3[0] == 0):
                circle_won = 1
            else:
                cross_won = 1

    if(len(dia1) == 3):
        if(dia1[0] == dia1[1] == dia1[2]):
            draw_grid_line((-145,145),135,t1,415)
            if(dia1[0] == 0):
                circle_won = 1
            else:
                cross_won = 1

    if(len(dia2) == 3):
        if(dia2[0] == dia2[1] == dia2[2]):
            draw_grid_line((145,145),225,t1,415)
            if(dia2[0] == 0):
                circle_won = 1
            else:
                cross_won = 1
    if(len(row1) == 3 and len(row2) == 3 and len(row3) == 3 and
       len(col1) == 3 and len(col2) == 3 and len(col3) == 3 and len(dia1) == 3 and
       len(dia2) == 3 and circle_won == 0 and cross_won == 0):
           t1.pu()
           t1.goto(-135,-250)
           t1.pd()
           t1.color('yellow')
           t1.write("Match Tie", font = ("Arial",20))
           
    if(circle_won == 1):
        t1.pu()
        t1.goto(-80,-250)
        t1.pd()
        t1.color('green')
        t1.write("Circle_won", font = ("Arial",20))
    if(cross_won == 1):
        t1.pu()
        t1.goto(-80,-250)
        t1.pd()
        t1.color('green')
        t1.write("Cross_won", font = ("Arial",20))

def cir_or_cross():
    global tog, pos
    if tog == 0:
            draw_circle(pos)
            tog = 1
    else:
        draw_cross(pos)
        tog = 0

def draw_grid_line(pos,angle,tur,dist):
    tur.penup()
    tur.goto(pos)
    tur.right(angle)
    tur.pendown()
    tur.forward(dist)

def draw_circle(pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.color('white')
    t1.pensize(2)
    t1.circle(-30)

def draw_cross(pos):
    x,y = pos
    x = x+5
    y = y+25
    t1.pensize(2)
    draw_grid_line((x,y),135,t1,70)
    t1.penup()
    y = y-50
    draw_grid_line((x,y),270,t1,70)
    t1.left(45)

for i in range(4):
    b.forward(300)
    b.right(90)

draw_grid_line((-150,50),0,b,300)
draw_grid_line((-150,-50),0,b,300)
draw_grid_line((-50,150),90,b,300)
draw_grid_line((50,150),0,b,300)

#### Draw Title ####
b.penup()
b.goto(-80,200)
b.pendown()
b.color('skyblue')
b.write('Tic Tac Toe Game', font=('arial',15))

#### draw button ####
b.penup()
b.goto(-330,50)
b.color("cyan")
b.pendown()
b.left(90)
b.begin_fill()
for i in range(2):
    b.forward(150)
    b.right(90)
    b.forward(30)
    b.right(90)
b.end_fill()

b.color("magenta")
b.penup()
b.goto(-320,25)
b.write("Start/Play Again", font = ("Arial",14))

w.onscreenclick(draw)
t.done()