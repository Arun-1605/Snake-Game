from turtle import  Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

isGameOn = True



while isGameOn:
    screen.update()
    time.sleep(0.1)
    # print(snake.head.distance(food))
    snake.move()
    if snake.head.distance(food) < 15:
        
        food.refresh()
        snake.extend()
        score.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        isGameOn=False
        score.game_over()
        
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            isGameOn = False
            score.game_over()
    





screen.exitonclick()



















