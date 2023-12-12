from turtle import Screen, Turtle

SEGMENT_SIZE = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = [SnakeSegment() for i in range(3)]
        [segment.setx(-20 * i) for i, segment in enumerate(self.segments)]
        self.heading = 0

    def add_segment(self):
        pass

    def move(self):
        for segment in self.segments:
            segment.forward(3)

    def set_heading(self):
        for segment in self.segments:
            segment.setheading(self.heading)


class SnakeSegment(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color("white")


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    return screen


# def create_snake(snake=None):
#     if snake is None:
#         snake = [SnakeSegment().setx(-20 * i) for i in range(3)]
#     return snake


def main():
    screen = setup_screen()
    snake = Snake()
    snake.set_heading()
    while True:
        snake.move()

    screen.mainloop()


if __name__ == "__main__":
    main()
