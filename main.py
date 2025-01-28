from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")

# Create a list to store the segments of the snake
snake_segments = []

# Initialize the snake with three segments
for i in range(3):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(x=-20*i, y=0)
    snake_segments.append(segment)

def snake_move():
    # Move each segment to the position of the previous segment
    for i in range(len(snake_segments)-1, 0, -1):
        new_x = snake_segments[i-1].xcor()
        new_y = snake_segments[i-1].ycor()
        snake_segments[i].goto(new_x, new_y)
    # Move the head of the snake forward
    snake_segments[0].forward(20)
    screen.ontimer(snake_move, 100)

def snake_left():
    snake_segments[0].left(90)

def snake_right():
    snake_segments[0].right(90)


screen.listen()
screen.onkey(snake_move, "Up")
screen.onkey(snake_left, "Left")
screen.onkey(snake_right, "Right")

screen.exitonclick()