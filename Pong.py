import turtle
import winsound

score_left = 0
score_right = 0
wn = turtle.Screen()
wn.title("Pong by Unsubstantiated_Script")
wn.bgcolor("#6c584c")
wn.setup(width=800, height=600)
# Keeps the window from updating...making game faster
wn.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color("#dde5b6")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color("#dde5b6")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("#d62828")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Movement Functions
def paddle_left_up():
    if paddle_left.ycor() < 240:
        y = paddle_left.ycor()
        y += 20
        paddle_left.sety(y)


def paddle_left_down():
    if paddle_left.ycor() > -230:
        y = paddle_left.ycor()
        y -= 20
        paddle_left.sety(y)


def paddle_right_up():
    if paddle_right.ycor() < 240:
        y = paddle_right.ycor()
        y += 20
        paddle_right.sety(y)


def paddle_right_down():
    if paddle_right.ycor() > -230:
        y = paddle_right.ycor()
        y -= 20
        paddle_right.sety(y)


wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    # resetting the starting coordinate
    # Inverting the direction
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_right.ycor() + 50 > ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_left.ycor() + 50 > ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
