from random import randrange
from turtle import *

from freegames import square, vector

# Initialize variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Function to change the snake's direction
def change(x, y):
    aim.x = x
    aim.y = y

# Function to check if the head is inside boundaries
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Function to move the snake forward one segment
def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

# Set up the game window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Define key bindings for changing direction
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Start the game
move()
done()
