import turtle
import winsound

win = turtle.Screen()
win.title("PONG by Pedro")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

#score
score_a = 0
score_b = 0


#left rectangle
left_rectangle = turtle.Turtle()
left_rectangle.speed(0)
left_rectangle.shape("square")
left_rectangle.color("white")
left_rectangle.shapesize(stretch_wid = 5, stretch_len = 1)
left_rectangle.penup()
left_rectangle.goto(-350, 0)

#right rectangle
right_rectangle = turtle.Turtle()
right_rectangle.speed(0)
right_rectangle.shape("square")
right_rectangle.color("white")
right_rectangle.shapesize(stretch_wid = 5, stretch_len = 1)
right_rectangle.penup()
right_rectangle.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.06
ball.dy = 0.06

#pen (scoreboard)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #we dont want to see the turtle, just the text it's gonna write
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# funcion (left rectangle)
def left_rectangle_up():
    y = left_rectangle.ycor()
    y += 20
    left_rectangle.sety(y)

#function 2 (left rectangle)
def left_rectangle_down():
    y = left_rectangle.ycor()
    y -= 20
    left_rectangle.sety(y)

#function 3 (right rectangle)
def right_rectangle_up():
    y = right_rectangle.ycor()
    y += 20
    right_rectangle.sety(y)

#function 4 (right rectangle)
def right_rectangle_down():
    y = right_rectangle.ycor()
    y -= 20
    right_rectangle.sety(y)

# keyboard binding
win.listen()
win.onkeypress(left_rectangle_up, "w")
win.onkeypress(left_rectangle_up, "W")
win.onkeypress(left_rectangle_down, "s")
win.onkeypress(left_rectangle_down, "S")
win.onkeypress(right_rectangle_up, "Up")
win.onkeypress(right_rectangle_down, "Down")



#main game loop
while True:
    win.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking (up one)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    #border checking (down one)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #border checking (right one)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    
    #border checking (left one)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    #rectangle and ball collision (right one)
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < right_rectangle.ycor() + 40 and ball.ycor() > right_rectangle.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

    #rectangle and ball collision (left one)

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < left_rectangle.ycor() + 40 and ball.ycor() > left_rectangle.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

       