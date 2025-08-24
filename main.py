from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0) 
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True
while game_is_on:
    screen.update() 
    time.sleep(0.1) 

    snake.move()

    # detect collision w food.
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # detect collision w wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision w tail.
    # if head collides with any segment in the tail then trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()