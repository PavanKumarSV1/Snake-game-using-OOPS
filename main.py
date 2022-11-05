"""
Imports:
Snake.py which contains the Snake class
Food.py which contains the Food class
Turtle module to implement game graphics
"""

import Snake
import Food
import turtle
import time

""""
The main file for the program that implements the Python game using 
the turtle module. 

Global variables:

DELAY: The value after which the main game loop reruns. This sets how 
fast the snake moves. This value is to be slowly decremented as the 
game progresses.

COUNTER: Variable to keep count of the number of elapsed frames since
the last decrement of the DELAY variable.
"""
DELAY = 100
COUNTER = 0

def game_loop() -> None:

    """
    Function that implements the main game loop. All updations are to be
    done in this function. Function should also implement GAME OVER logic
    and do the decrement in DELAY appropriately.
    :return: None
    """

    ############ DO NOT CHANGE ###########
    global DELAY
    global COUNTER
    
    ######################################
    ########## WRITE BELOW ###############

    snake_obj.keep_snake_onscreen()

    if snake_obj.check_food_collision(food_obj.position):
        segment = turtle.Turtle("square")
        segment.color('green')
        segment.penup()
        snake_obj.shape.append(segment)
        food_obj.update_random_food_position()
        food_turtle.goto(food_obj.position)
    
    if snake_obj.direction == 'Right':
            snake_obj.go_right()
    if snake_obj.direction == 'Left':
            snake_obj.go_left()
    if snake_obj.direction == 'Up':
            snake_obj.go_up()
    if snake_obj.direction == 'Down':
            snake_obj.go_down()

    snake_obj.update_snake()

    ######################################
    
    ########### DO NOT CHANGE ############
    screen.update()

    if DELAY > 10 and COUNTER == 15:
        DELAY -= 1
        COUNTER = 0

    COUNTER += 1
    if len(snake_obj.shape) != 0:
        turtle.ontimer(game_loop, DELAY)

    #######################################

if __name__ == "__main__":
    """
    The main for the program.
    DO NOT CHANGE    
    """
    
    ############ DO NOT CHANGE ############
    screen_height = 500
    screen_width = 500
    start_time = time.time()

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Python in Python")
    screen.bgcolor("blue")
    screen.tracer(0)

    snake_obj = Snake.Snake(window_size=(screen_width, screen_height))
    food_obj = Food.Food(window_size=(screen_width, screen_height))
    food_obj.update_random_food_position()

    snake_turtle = turtle.Turtle("square")
    snake_turtle.color(snake_obj.color)
    snake_turtle.penup()

    food_turtle = turtle.Turtle()
    food_turtle.shape(food_obj.shape)
    food_turtle.color(food_obj.color)
    food_turtle.pensize(food_obj.size)
    food_turtle.penup()

    screen.listen()
    screen.onkey(snake_obj.go_up, "Up")
    screen.onkey(snake_obj.go_down, "Down")
    screen.onkey(snake_obj.go_right, "Right")
    screen.onkey(snake_obj.go_left, "Left")

    snake_obj.shape.append(snake_turtle)
    food_turtle.setpos(food_obj.position)

    game_loop()
    turtle.done()
    #########################################