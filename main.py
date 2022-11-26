from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

ball = Ball()
screen = Screen()
player1 = screen.textinput("Who will be Player 1", "Enter a name: ")
player2 = screen.textinput("Who will be Player 2", "Enter a name: ")
target_score = int(screen.textinput("Target score?", "Enter a number: "))
score = Scoreboard(player1, player2)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pongy pongy pongy")
screen.tracer(0)

left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
        score.update_score(player1, player2)

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()
        score.update_score(player1, player2)

    if score.l_score == target_score:
        score.winner(player1)
        game_is_on = False
    elif score.r_score == target_score:
        score.winner(player2)
        game_is_on = False

screen.exitonclick()
