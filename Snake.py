import math
class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################
        self.__offsets__ = {'Right': self.go_right, 'Left': self.go_left, 'Up': self.go_up, 'Down': self.go_down}
        self.shape = []
        self.direction = ''
        self.color = 'yellow'
        self.window_size = window_size
        self.GAME_OVER = False
        ###########################################

    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.direction != 'Down':
            self.direction = 'Up'
            x = self.shape[0].xcor()
            y = self.shape[0].ycor()
            self.shape[0].setpos(x,y+20)
            for i in range(1,len(self.shape)):
                    tempx = self.shape[i].xcor()
                    tempy = self.shape[i].ycor()
                    self.shape[i].setx(x)
                    self.shape[i].sety(y)
                    x = tempx
                    y = tempy
        return None
        ##########################################
    
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
    
        if self.direction != 'Up':
            self.direction = 'Down'
            x = self.shape[0].xcor()
            y = self.shape[0].ycor()
            self.shape[0].setpos(x,y-20)
            for i in range(1,len(self.shape)):
                    tempx = self.shape[i].xcor()
                    tempy = self.shape[i].ycor()
                    self.shape[i].setx(x)
                    self.shape[i].sety(y)
                    x = tempx
                    y = tempy              
        return None
        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'Right':
            self.direction = 'Left'
            x = self.shape[0].xcor()
            y = self.shape[0].ycor()
            self.shape[0].setpos(x-20,y)
            for i in range(1,len(self.shape)):
                tempx = self.shape[i].xcor()
                tempy = self.shape[i].ycor()
                self.shape[i].setx(x)
                self.shape[i].sety(y)
                x = tempx
                y = tempy              
        return None
        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'Left':
            self.direction = 'Right'
            x = self.shape[0].xcor()
            y = self.shape[0].ycor()
            self.shape[0].setpos(x+20,y)
            for i in range(1,len(self.shape)):
                tempx = self.shape[i].xcor()
                tempy = self.shape[i].ycor()
                self.shape[i].setx(x)
                self.shape[i].sety(y)
                x = tempx
                y = tempy             
        return None
        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        ############## WRITE BELOW ###############
        (x1,y1) = self.shape[0].pos()
        (x2,y2) = current_food_position
        distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        if distance < 20:
            return True
        else:
            return False


        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """
        ############## WRITE BELOW ###############
        if self.shape[0].xcor() > 250:
            self.shape[0].setx(-250)

        if self.shape[0].xcor() < -250:
            self.shape[0].setx(250)

        if self.shape[0].ycor() > 250:
            self.shape[0].sety(-250)

        if self.shape[0].ycor() < -250:
            self.shape[0].sety(250)

        return None
        ##########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """

        ############## WRITE BELOW ###############
        for i in range(1, len(self.shape)):
            if self.shape[0].distance(self.shape[i]) < 20:
                self.GAME_OVER = True
                self.shape.clear()
                self.direction = ''
                break
        ##########################################









