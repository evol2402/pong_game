from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.title_art = [  # Ensure this is defined correctly
            " ____                      ____                      ",
            "|  _ \\ ___  _ __   __ _   / ___| __ _ _ __ ___   ___ ",
            "| |_) / _ \\| '_ \\ / _` | | |  _ / _` | '_ ` _ \\ / _ \\",
            "|  __/ (_) | | | | (_| | | |_| | (_| | | | | | |  __/",
            "|_|   \\___/|_| |_|\\__, |  \\____|\\__,_|_| |_| |_|\\___|",
            "                  |___/                             "
        ]
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        # Display the ASCII art at the top right corner
        self.display_ascii_art()

        # Display the scores
        self.goto(-250, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(250, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def display_ascii_art(self):
        x_position = -180  # Adjust this for your screen width
        y_position = 300  # Start from near the top of the screen

        for line in self.title_art:
            self.goto(x_position, y_position)
            self.write(line, align="left", font=("Courier", 8, "normal"))
            y_position -= 20  # Move down for the next line
