import turtle
import random
import time

screen = turtle.Screen()
screen.title("Ping Pong Game with Power Buffs")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

score_a = 0
score_b = 0

power_buff = turtle.Turtle()
power_buff.speed(0)
power_buff.shape("circle")
power_buff.color("yellow")
power_buff.penup()
power_buff.shapesize(stretch_wid=2, stretch_len=2)
power_buff.hideturtle()
power_active = False
active_buff = None

buff_name_tag = turtle.Turtle()
buff_name_tag.speed(0)
buff_name_tag.color("white")
buff_name_tag.penup()
buff_name_tag.hideturtle()

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

paddle_a_moving_up = False
paddle_a_moving_down = False
paddle_b_moving_up = False
paddle_b_moving_down = False
paddle_a_frozen = False
paddle_b_frozen = False

def paddle_a_up():
    global paddle_a_moving_up
    if not paddle_a_frozen:
        paddle_a_moving_up = True

def paddle_a_down():
    global paddle_a_moving_down
    if not paddle_a_frozen:
        paddle_a_moving_down = True

def stop_paddle_a_up():
    global paddle_a_moving_up
    paddle_a_moving_up = False

def stop_paddle_a_down():
    global paddle_a_moving_down
    paddle_a_moving_down = False

def paddle_b_up():
    global paddle_b_moving_up
    if not paddle_b_frozen:
        paddle_b_moving_up = True

def paddle_b_down():
    global paddle_b_moving_down
    if not paddle_b_frozen:
        paddle_b_moving_down = True

def stop_paddle_b_up():
    global paddle_b_moving_up
    paddle_b_moving_up = False

def stop_paddle_b_down():
    global paddle_b_moving_down
    paddle_b_moving_down = False

def move_paddles():
    if paddle_a_moving_up and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 10)
    if paddle_a_moving_down and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 10)
    if paddle_b_moving_up and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 10)
    if paddle_b_moving_down and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 10)
    screen.ontimer(move_paddles, 20)

def activate_random_power():
    global power_active, active_buff
    if not power_active:
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        power_buff.goto(x, y)
        power_buff.showturtle()
        power_active = True
        active_buff = random.choice(["speed", "fireball", "double", "freeze", "huge", "shrink", "slow", "invisible"])
        display_buff_name()

def display_buff_name():
    buff_name_tag.clear()
    buff_name_tag.goto(power_buff.xcor(), power_buff.ycor() + 20)
    buff_name_tag.write(active_buff, align="center", font=("Courier", 12, "normal"))

def remove_buff_name():
    buff_name_tag.clear()

def apply_power_buff(paddle):
    global power_active, active_buff, ball
    if active_buff == "speed":
        ball.dx *= 1.5
        ball.dy *= 1.5
    elif active_buff == "fireball":
        paddle.color("red")
        screen.ontimer(lambda: paddle.color("white"), 3000)
    elif active_buff == "double":
        global score_a, score_b
        score_a += 2
        score_b += 2
    elif active_buff == "freeze":
        global paddle_a_frozen, paddle_b_frozen
        if paddle == paddle_a:
            paddle_b_frozen = True
            screen.ontimer(lambda: unfreeze_paddle('b'), 3000)
        elif paddle == paddle_b:
            paddle_a_frozen = True
            screen.ontimer(lambda: unfreeze_paddle('a'), 3000)
    elif active_buff == "huge":
        paddle.shapesize(stretch_wid=12, stretch_len=1)
        screen.ontimer(lambda: paddle.shapesize(stretch_wid=6, stretch_len=1), 3000)
    elif active_buff == "shrink":
        ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
        screen.ontimer(lambda: ball.shapesize(stretch_wid=1, stretch_len=1), 3000)
    elif active_buff == "slow":
        ball.dx *= 0.5
        ball.dy *= 0.5
        screen.ontimer(lambda: reset_ball_speed(), 3000)
    elif active_buff == "invisible":
        ball.color("black")
        screen.ontimer(lambda: ball.color("white"), 3000)
    
    power_buff.hideturtle()
    power_active = False
    remove_buff_name()

def reset_ball_speed():
    ball.dx = 0.3
    ball.dy = 0.3

def unfreeze_paddle(paddle):
    global paddle_a_frozen, paddle_b_frozen
    if paddle == 'a':
        paddle_a_frozen = False
    elif paddle == 'b':
        paddle_b_frozen = False

screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeyrelease(stop_paddle_a_up, "w")
screen.onkeyrelease(stop_paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")
screen.onkeyrelease(stop_paddle_b_up, "Up")
screen.onkeyrelease(stop_paddle_b_down, "Down")

move_paddles()

def buff_timer():
    activate_random_power()
    screen.ontimer(buff_timer, 30000)

buff_timer()

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()

    if (350 > ball.xcor() > 340) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        if power_active and power_buff.distance(paddle_b) < 100:
            apply_power_buff(paddle_b)

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        if power_active and power_buff.distance(paddle_a) < 100:
            apply_power_buff(paddle_a)

    if power_active and power_buff.distance(ball) < 40:
        apply_power_buff(paddle_a if power_buff.distance(paddle_a) < power_buff.distance(paddle_b) else paddle_b)
