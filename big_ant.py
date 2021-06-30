# graphics library provided by Ben Dicken
# https://benjdd.com
from graphics import graphics

import math
from time import time

# frame rate of graphics element; takes around seven (7) minutes to complete when 
# ANT_SPEED = 50 and around five (5) minutes when ANT_SPEED = 100
ANT_SPEED = 100

# graphics constants:
GRID_SIZE = 100
GRAPHICS_SIZE = 400
GRID_SPACE_SIZE = 4

# direction constants:
LEFT = "l"
RIGHT = "r"
UP = "u"
DOWN = "d"

# color constants:
BLACK = "b"
WHITE = "w"

def make_grid():
    '''
    Creates a 7x7 grid of white squares. This is done by making a two-dimensional grid
    which saves the state of each grid square. It returns a 2d grid. Grid should always
    be a square.
    
     gui: the graphics object which the grid is being drawn to
    grid: a 2d array which stores the states of individual grid squares as the constants
          BLACK or WHITE
    '''
    
    grid = [[WHITE]*GRID_SIZE for i in range(GRID_SIZE)]
    
    gui = graphics(GRAPHICS_SIZE,GRAPHICS_SIZE, "Ant")
    
    return gui, grid

def update_grid(grid, ant_x_position, ant_y_position):
    '''
    Takes the grid made by the make_grid function or from a previous iteration of the
    update_grid function. It only updates the grid under the ant, it does not move the ant
    itself. It *does* take the ant's position to know which grid space to flip.
    
              grid: a 2d array which stores the states of individual grid squares as the 
                    constants BLACK or WHITE
    ant_x_position: an integer value stating the horizontal distance from the left edge of
                    the grid to the ant's square
    ant_y_position: an integer value stating the vertical distance from the top edge of 
                    the grid to the ant's square
    '''
    if grid[ant_y_position][ant_x_position] == WHITE:
        grid[ant_y_position][ant_x_position] = BLACK
    
    elif grid[ant_y_position][ant_x_position] == BLACK:
        grid[ant_y_position][ant_x_position] = WHITE
    
    return grid

def draw_grid(grid, gui):
    '''
    This function draws the grid on the visual window. It parses the grid array to 
    determine whether a given square should be black or white when printed.
    
     gui: the graphics object which the grid is being drawn to
    grid: a 2d array which stores the states of individual grid squares as the constants
          BLACK or WHITE
    '''
    grid_length = len(grid)
    for row in range(grid_length):
        for i in range(grid_length):
            if grid[i][row] == WHITE:
                pass
            elif grid[i][row] == BLACK:
                gui.rectangle(GRID_SPACE_SIZE*row, GRID_SPACE_SIZE*i, \
                GRID_SPACE_SIZE, GRID_SPACE_SIZE, "black")

def draw_ant(gui, ant_x_position, ant_y_position):
    gui.rectangle(GRID_SPACE_SIZE*ant_x_position, GRID_SPACE_SIZE*ant_y_position, \
    GRID_SPACE_SIZE, GRID_SPACE_SIZE, "red")
    
    gui.update_frame(ANT_SPEED)      

def turn_ant(grid, ant_x_position, ant_y_position, ant_direction):
    '''
    This function turns the ant. It does not handle changes in the ant's position.
    
              grid: a 2d array which stores the states of individual grid squares as the
                    constants BLACK or WHITE
    ant_x_position: an integer value stating the horizontal distance from the left edge of
                    the grid to the ant's square
    ant_y_position: an integer value stating the vertical distance from the top edge of 
                    the grid to the ant's square
     ant_direction: the current direction the ant faces, which is used to determine the
                    next direction the ant should face
    '''
    if grid[ant_y_position][ant_x_position] == WHITE:
        if ant_direction == LEFT:
            ant_direction = UP
        elif ant_direction == RIGHT:
            ant_direction = DOWN
        elif ant_direction == UP:
            ant_direction = RIGHT
        elif ant_direction == DOWN:
            ant_direction = LEFT
    
    if grid[ant_y_position][ant_x_position] == BLACK:
        if ant_direction == LEFT:
            ant_direction = DOWN
        elif ant_direction == RIGHT:
            ant_direction = UP
        elif ant_direction == UP:
            ant_direction = LEFT
        elif ant_direction == DOWN:
            ant_direction = RIGHT
    
    return ant_direction

def move_ant(grid, ant_x_position, ant_y_position, ant_direction): #FIXME: function comment
    '''
    This function moves the ant. It requires the ant's starting position and returns a new
    position based on the ant's direction.
    
              grid: a 2d array which stores the states of individual grid squares as the
                    constants BLACK or WHITE
    ant_x_position: an integer value stating the horizontal distance from the left edge of
                    the grid to the ant's square
    ant_y_position: an integer value stating the vertical distance from the top edge of 
                    the grid to the ant's square
     ant_direction: the current direction the ant faces, which is used to determine the
                    next direction the ant should faces
    '''
    # conditionals to move ant
    if ant_direction == LEFT:
        ant_x_position -= 1
    elif ant_direction == RIGHT:
        ant_x_position += 1
    elif ant_direction == UP:
        ant_y_position -= 1
    elif ant_direction == DOWN:
        ant_y_position += 1
    
    return ant_x_position, ant_y_position

def main():
    start_time = time()
    in_range = True
    gui, grid = make_grid()
    
    ant_direction_start = LEFT
    ant_x_start = math.floor(len(grid)/2)
    ant_y_start = math.floor(len(grid)/2)
    
    ant_direction = ant_direction_start
    ant_x = ant_x_start
    ant_y = ant_y_start
    
    num_steps = 0
    
    while in_range == True:
        if num_steps % 100 == 0:
            print("Number of steps taken:", end = ' ')
            print(num_steps)
        try:
            
            ant_direction = turn_ant(grid, ant_x, ant_y, ant_direction)
            
            draw_grid(grid, gui)
            draw_ant(gui, ant_x, ant_y)
            
            grid = update_grid(grid, ant_x, ant_y)
            
            ant_x, ant_y = move_ant(grid, ant_x, ant_y, ant_direction)
            
            num_steps += 1
            
            
            gui.clear()
            
            
        except IndexError:
            in_range = False    
            draw_grid(grid, gui)
            draw_ant(gui, ant_x, ant_y)
            end_time = time()
            
            print(end_time - start_time)
    
    gui.primary.mainloop()
    
    
main()