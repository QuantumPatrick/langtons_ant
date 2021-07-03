# graphics library provided by Ben Dicken
# https://benjdd.com
from graphics import graphics

import math

# direction constants:
LEFT = "l"
RIGHT = "r"
UP = "u"
DOWN = "d"

# directional ant files
ANT_LEFT = "ANT_LEFT.png"
ANT_RIGHT = "ANT_RIGHT.png"
ANT_UP = "ANT_UP.png"
ANT_DOWN = "ANT_DOWN.png"

# color constants:
BLACK = "b"
WHITE = "w"

def make_grid():
    '''
    Creates a 7x7 grid of white squares. This is done by making a two-dimensional grid
    which saves the state of each grid square. It returns a 2d grid. Grid should always
    be a square.
    '''
    grid_list = [[WHITE]*7 for i in range(7)]
    
    gui = graphics(420,420, "Ant")
    
    for i in range(7):
        for j in range(7):
            gui.line(0, 60*i, 420, 60*i, "grey")
            gui.line(60*i, 0, 60*i, 420, "grey")
    gui.update_frame(1)
    
    return gui, grid_list

def update_grid(grid, ant_x_position, ant_y_position):
    '''
    Takes the grid made by the make_grid function or from a previous iteration of the
    update_grid function. It only updates the grid under the ant, it does not move the ant
    itself. It *does* take the ant's position to know which grid space to flip.
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
    gui: the graphics object which the grid is being drawn to.
    grid: a 2d array in which each element is the predefined constant BLACK or WHITE.
    '''
    grid_length = len(grid)
    for row in range(grid_length):
        for i in range(grid_length):
            if grid[i][row] == WHITE:
                gui.rectangle(60*row,60*i,60,60, "white")
            if grid[i][row] == BLACK:
                gui.rectangle(60*row,60*i,60,60, "black")
    
    for i in range(grid_length):
        for j in range(grid_length):
            gui.line(0, 60*i, 420, 60*i, "grey")
            gui.line(60*i, 0, 60*i, 420, "grey")

def draw_ant(gui, ant_x_position, ant_y_position, direction):
    if direction == LEFT:
        gui.image(60*ant_x_position, 60*ant_y_position, 1, 1, ANT_LEFT)
    elif direction == RIGHT:
        gui.image(60*ant_x_position, 60*ant_y_position, 1, 1, ANT_RIGHT)
    elif direction == UP:
        gui.image(60*ant_x_position, 60*ant_y_position, 1, 1, ANT_UP)
    elif direction == DOWN:
        gui.image(60*ant_x_position, 60*ant_y_position, 1, 1, ANT_DOWN)
    
    gui.update_frame(5)

def turn_ant(grid, ant_x_position, ant_y_position, ant_direction):
    '''
    This function turns the ant. It does not handle changes in the ant's position.
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

def move_ant(grid, ant_x_position, ant_y_position, ant_direction):
    '''
    This function moves the ant. It does not handle changes in the ant's rotation.
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
    in_range = True
    gui, grid = make_grid()
    
    ant_direction_start = LEFT
    ant_x_start = math.floor(len(grid)/2)
    ant_y_start = math.floor(len(grid)/2)
    
    ant_direction = ant_direction_start
    ant_x = ant_x_start
    ant_y = ant_y_start
    
    
    while in_range == True:
        try:
            gui.clear()
            ant_direction = turn_ant(grid, ant_x, ant_y, ant_direction)
            
            draw_grid(grid, gui)
            draw_ant(gui, ant_x, ant_y, ant_direction)
            
            grid = update_grid(grid, ant_x, ant_y)
            
            draw_grid(grid, gui)
            draw_ant(gui, ant_x, ant_y, ant_direction)
            
            ant_x, ant_y = move_ant(grid, ant_x, ant_y, ant_direction)
            
            draw_grid(grid, gui)
            draw_ant(gui, ant_x, ant_y, ant_direction)
            
            
        except IndexError:
            in_range = False    
    
    gui.primary.mainloop()
    
    
main()
