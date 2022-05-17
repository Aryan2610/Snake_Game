from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake game\scoreboard.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align="center",font=("Comic Sans MS",24,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Snake game\scoreboard.txt", mode = "w") as file:
                file.write(f"{self.highscore}") 
        self.score = 0
        self.clear()
        self.updateScoreboard()

    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.updateScoreboard()