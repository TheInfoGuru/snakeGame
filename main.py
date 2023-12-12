from turtle import Screen, Turtle

SEGMENT_SIZE = 20


class Snake:
    def __init__(self):
        self.segments = [SnakeSegment().setx(-20 * i) for i in range(3)]
        self.heading = 90
        self.segments.set_heading()

    def add_segment(self):
        pass

    def move_snake(self):
        pass

    def set_heading(self):
        for segment in self.segments:
            segment.setheading(self.heading)


class SnakeSegment(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.mode = "logo"



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

    screen.mainloop()


if __name__ == "__main__":
    main()
