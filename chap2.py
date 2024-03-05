import turtle

#define constants 
WIDTH = 500
HEIGHT = 500
DELAY = 400  # Milliseconds between screen updates
offsets = {
    "up":(0,20),
    "down":(0,-20),
    "left":(-20,0),
    "right":(20,0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"



#function for tutrle to move
def move_snake():
    my_snake.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]


    # add new head to snake
    snake.append(new_head)

    #remove last segment of snake
    snake.pop(0)

    for segment in snake:
        my_snake.goto(segment[0],segment[1])
        my_snake.stamp()
    #refresh screen
    screen.update()
    #rinse and repeat
    turtle.ontimer(move_snake,DELAY)
# end move _turtle

#cereate a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("snake")
screen.bgcolor("pink")
screen.tracer(0)

#event handler
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

my_snake = turtle.Turtle("square")
my_snake.penup()

#create snake list as a list of co ordinaes
snake = [[0,0], [20,0],[40,0],[60,0]]
snake_direction = "up"

#draw a snake
for segment in snake:
    my_snake.goto(segment[0],segment[1])
    my_snake.stamp()

#set animation
move_snake()

# Finish nicely
turtle.done()