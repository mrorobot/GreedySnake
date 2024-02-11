from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboared import Scoreboard
# from boundary import Boundary
# boundary=Boundary()

food=Food()
score=Scoreboard()

game=Snake()
screen=Screen()
screen.setup(600,600)
screen.title('Snake Game')
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(game.up,"Up")
screen.onkey(game.down,"Down")
screen.onkey(game.right,"Right")
screen.onkey(game.left,"Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    game.movement()
    i=0.1
    if game.bodies[0].distance(food)<15:

        food.refresh()
        game.extend()
        score.inc_score()
        time.sleep(i)
        i+=0.05
    if game.bodies[0].xcor()>285 or game.bodies[0].xcor()<-285 or game.bodies[0].ycor()<-285 or game.bodies[0].ycor()>290:
        score.update_high_score()
        game.reset_snake()

        # score.game_over()
        # game_on= False
    for segment in game.bodies[1:]:
        if game.bodies[0].distance(segment)<=10:
            game.reset_snake()
            score.update_high_score()
            # game_on=False
            # score.game_over()

screen.exitonclick()