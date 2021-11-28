import turtle
import os
win_main=turtle.Screen()
win_main.title("pong_game by @Gayatrichaudhari")
win_main.bgcolor("white")
win_main.setup(width=900,height=600)
win_main.tracer(0)


#score couter
score_a=0
score_b=0
#sec A
sec_a=turtle.Turtle()
sec_a.speed(0)    
sec_a.shape("square")
sec_a.color("black")
sec_a.shapesize(stretch_wid=5,stretch_len=1)
sec_a.penup()
sec_a.goto(-350,0)
#sec B
sec_b=turtle.Turtle()
sec_b.speed(0)    
sec_b.shape("square")
sec_b.color("black")
sec_b.shapesize(stretch_wid=5,stretch_len=1)
sec_b.penup()
sec_b.goto(350,0)

#ball
sec_ball=turtle.Turtle()
sec_ball.speed(0)    
sec_ball.shape("circle")
sec_ball.color("black")
sec_ball.penup()
sec_ball.goto(0,0)
sec_ball.dx=0.55
sec_ball.dy=0.55
#sec_a func
def sec_a_up():
    y=sec_a.ycor()
    y+=20
    sec_a.sety(y)
def sec_a_down():
    y=sec_a.ycor()
    y-=20
    sec_a.sety(y)
def sec_b_up():
    y=sec_b.ycor()
    y+=20
    sec_b.sety(y)
def sec_b_down():
    y=sec_b.ycor()
    y-=20
    sec_b.sety(y)

pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0  player B: 0",align="center",font=("courier",22,"normal"))
#keyboard binding for sec a
win_main.listen()
win_main.onkeypress(sec_a_up,"w")
win_main.onkeypress(sec_a_down,"s")
win_main.onkeypress(sec_b_up,"Up")
win_main.onkeypress(sec_b_down,"Down")

#main loop
while True:
    win_main.update()

    sec_ball.setx(sec_ball.xcor()+sec_ball.dx)
    sec_ball.sety(sec_ball.ycor()+sec_ball.dy)

    if sec_ball.ycor()>290:
        sec_ball.sety(290)
        sec_ball.dy*=-1
        os.system("play beep.mp3&")
    
    if sec_ball.ycor()<-290:
        sec_ball.sety(-290)
        sec_ball.dy*=-1

    if sec_ball.xcor()>390:
        sec_ball.goto(0,0)
        sec_ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("courier",22,"normal"))
    
    if sec_ball.xcor()<-390:
        sec_ball.goto(0,0)
        sec_ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_a,score_b),align="center",font=("courier",22,"normal"))
    #sec and ball collision
    if (sec_ball.xcor()>340 and sec_ball.xcor()<350) and (sec_ball.ycor()<sec_b.ycor()+50 and sec_ball.ycor()>sec_b.ycor()-50):
        sec_ball.setx(340)
        sec_ball.dx*=-1
    
    if (sec_ball.xcor()<-340 and sec_ball.xcor()>-350) and (sec_ball.ycor()<sec_a.ycor()+50 and sec_ball.ycor()>sec_a.ycor()-50):
        sec_ball.setx(-340)
        sec_ball.dx*=-1