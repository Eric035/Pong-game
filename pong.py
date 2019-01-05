# A simple Pong game written in python
import turtle 
import os 

window = turtle.Screen()
window.title("Pong for Minna")
window.bgcolor ("black")
window.setup(width = 800, height = 600)
window.tracer (0) 

# Score 
score_a = 0
score_b = 0


# Paddle 1

p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.color("Yellow")
p1.penup()
p1.goto(-350,0)

# Paddle 2

p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.color("blue")
p2.penup()
p2.goto(350,0)

# Ball

b = turtle.Turtle()
b.speed(0)
b.shape("circle")
b.shapesize(stretch_wid=1, stretch_len=1)
b.color("red")
b.penup()
b.goto(0,0)
b.dx = 2.5
b.dy = 2.5

# Pen 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()    
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function 

def p1_up():
    y = p1.ycor()
    y += 20 
    p1.sety(y)

def p1_down():
    y = p1.ycor()
    y += -20 
    p1.sety(y)

def p2_up():
    y = p2.ycor()
    y += 20 
    p2.sety(y)

def p2_down():
    y = p2.ycor()
    y += -20 
    p2.sety(y)

# KeyBoard_binding 

window.listen()
window.onkeypress(p1_up, "w")
window.onkeypress(p1_down, "s")
window.onkeypress(p2_up, "Up")
window.onkeypress(p2_down, "Down")

# Main game loop
while True:
    window.update()

    # Ball movement
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)
    
    # Border check
    if b.ycor() > 290:              # ball is 20 by 20 pixels and upper bound is 300
        b.sety(290)
        b.dy *= -1 
        os.system("afplay bounce.wav&")

    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1
        os.system("afplay bounce.wav&")

    if b.xcor() > 390:
        b.goto (0, 0)
        b.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay bruh.mp3&")

    if b.xcor() < -390:
        b.goto (0, 0)
        b.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay bruh.mp3&")

    # Paddles and ball collide
    if (b.xcor() > 340 and b.xcor() < 350) and (b.ycor() < p2.ycor() + 40 and b.ycor() > p2.ycor() - 40):
        b.setx (340)
        os.system("afplay bounce.wav&")
        b.dx *= -1

    if (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < p1.ycor() + 40 and b.ycor() > p1.ycor() - 40):
        b.setx (-340)
        os.system("afplay bounce.wav&")
        b.dx *= -1
        
