import turtle
#Setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddel A

paddel_a= turtle.Turtle()
paddel_a.shape("square")
paddel_a.color("white")
paddel_a.shapesize(stretch_wid=5, stretch_len=1)
paddel_a.speed()
paddel_a.penup()
paddel_a.goto(-350,0)

#Paddel B
paddel_b= turtle.Turtle()
paddel_b.shape("square")
paddel_b.color("white")
paddel_b.shapesize(stretch_wid=5, stretch_len=1)
paddel_b.speed(0)
paddel_b.penup()
paddel_b.goto(350,0)

#Ball

ball= turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.speed(1)
ball.penup()
ball.goto(0,0)
ball.dx= 0.2
ball.dy= -0.2

#Score
score_a= 0
score_b= 0 

#Pen 
pen=turtle.Turtle()
pen.hideturtle()
pen.goto(0,260)
pen.penup()
pen.speed(0)
pen.color("white")
pen.write("Player A: 0 Player B: 0",align="center",font=("courier",24,"normal"))



#Funtion 
def paddel_a_up():
    y= paddel_a.ycor()
    y += 20
    paddel_a.sety(y)
def paddel_a_down():
    y= paddel_a.ycor()
    y -= 20
    paddel_a.sety(y)
def paddel_b_up():
    y= paddel_b.ycor()
    y += 20
    paddel_b.sety(y)
def paddel_b_down():
    y= paddel_b.ycor()
    y -= 20
    paddel_b.sety(y)
#Keyboard bliding
wn.listen()
wn.onkeypress(paddel_a_up,"w")
wn.onkeypress(paddel_a_down,"s")
wn.onkeypress(paddel_b_up,"Up")
wn.onkeypress(paddel_b_down,"Down")
#Main game 
while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *=-1  
    if ball.ycor() < -290:
        
        ball.sety(-290)
        ball.dy *=-1  
    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *=-1  
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1  
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddel_b.ycor() + 40 and ball.ycor() > paddel_b.ycor() -40):
        ball.dx *=-1
        ball.setx(340)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddel_a.ycor() + 40 and ball.ycor() > paddel_a.ycor() -40):
        ball.dx *=-1
        ball.setx(-340)