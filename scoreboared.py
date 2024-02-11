from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        file=open("high_score.txt")
        self.high_score= int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        self.update_high_score()



    def update_score(self):
        self.write(f"score is:{self.score} | High score is {self.high_score}", False, align="center", font=("Ariel", 20, "normal"))

    def inc_score(self):
        self.clear()
        self.score+=1
        self.update_score()
        self.score

    def update_high_score(self):
        if self.score > self.high_score:
            self.clear
            with open("high_score.txt", mode="w") as high:
                high.write(str(self.score))
            self.high_score=self.score
        self.clear()
        self.score = 0
        self.update_score()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over", False, align="center", font=("Ariel", 20, "normal"))
