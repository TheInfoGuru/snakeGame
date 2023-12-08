from turtle import Screen, Turtle


class GameScreen(Screen):
    def __init__(self):
        super().__init__()
        super().setup(width=600, height=600)
        super().bgcolor("black")
        super().title("My Snake Game")


screen = GameScreen()
