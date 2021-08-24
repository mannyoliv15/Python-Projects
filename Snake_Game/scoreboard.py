from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,270)

        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"score: {self.score}", move=False, align="Center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="Center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()








