#https://github.com/SideekaAyoob/Python_Snake

import turtle
import random

#define constants 
WIDTH = 500
HEIGHT = 500
DELAY = 100  # Milliseconds between screen updates
offsets = {
    "up":(0,20),
    "down":(0,-20),
    "left":(-20,0),
    "right":(20,0)
}
FOOD_SIZE = 10

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

#replacing the go functions by using 1 function
def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":  # so no self-collision by pressing wrong key.
            snake_direction = "up"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"


#function for tutrle to move
def game_loop():
    my_snake.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
   
    # check for collisions
    if new_head in snake or new_head[0]<-WIDTH/2 or new_head[0] >WIDTH /2\
    or new_head[1] <- HEIGHT/2 or new_head[1] >HEIGHT/2:
        reset()
    else:
        # No collision so we can continue moving the snake.
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw snake
        for segment in snake:
            my_snake.goto(segment[0], segment[1])
            my_snake.stamp()

        # Refresh screen
            screen.title(f"snake game. Score: {score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)
# end move _turtle

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score +=1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False
# end food collisions

def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)
# end get random food pos

def get_distance(pos1, pos2):
    x1,y1 = pos1
    x2,y2= pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)  # tuple - if no second argument provided this is treated as an xs, y pair.
    game_loop()


#cereate a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("snake")
screen.bgcolor("pink")
screen.tracer(0)

#event handler
screen.listen()
bind_direction_keys()
my_snake = turtle.Turtle("square")
my_snake.penup()

#create snake list as a list of co ordinaes
snake = [[0,0], [20,0],[40,0],[60,0],[80,0]]
snake_direction = "up"
score = 0


# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)  # Default size of turtle "square" shape is 20.
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

#set animation
reset()

# Finish nicely
turtle.done()