#!/usr/bin/env python3
### MARS ROVER traversing script
### This script will establish the locations of the 2 rovers on a 10x10 grid. The rovers will take turns making moves, and will perform 3 instructions before handing off to the next rover.
### 1) Identify current position (x,y,[N, S, E, or W])
### 2) Move to determined coordinates [M,L,R]: M_ove forward one space, L_eft 90degrees, R_ight 90degrees
### 3) Output final position (x,y,[N, S, E, or W])

### I will be programming the rovers to move inwards, spiraling clockwise, starting from the outer positions as defined in rover_a_start and rover_b_start, respectively

###               Rover starting positions, visual
#             ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#         9  |   |   |   |   |   |   |   |   |   | B |
#             ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#         8  |   |   |   |   |   |   |   |   |   |   |
#             ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    y    7  |   |   |   |   |   |   |   |   |   |   |
#             ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    c    6  |   |   |   |   |   |   |   |   |   |   |
#    o        ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    o    5  |   |   |   |   |   |   |   |   |   |   |
#    r        ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    d    4  |   |   |   |   |   |   |   |   |   |   |
#    i        ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    n    3  |   |   |   |   |   |   |   |   |   |   |
#    a        ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    t    2  |   |   |   |   |   |   |   |   |   |   |
#    e        ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#    s    1  |   |   |   |   |   |   |   |   |   |   |
#             ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
#         0  | A |   |   |   |   |   |   |   |   |   |
#              0   1   2   3   4   5   6   7   8   9
#                         x coordinates

# Define global variables
# define compass list, going clockwise
direction = ["N", "E", "S", "W"]

#starting positions of rovers = [x,y,"[N,S,E,W]"]
rover_a_start = [0,0,"N"]
rover_b_start = [9,9,"S"]
rover_a = rover_a_start
rover_b = rover_b_start
movement_data = []

# Grid data store
mars_grid = []
grid_max_x = 9
grid_max_y = 9


# build grid array
def build_grid():
    ### Build the 10x10 grid with a T/F flag (default False), to track if area has been traversed
    # local coordinate variables for x and y
    global mars_grid
    _count_x = 0
    _count_y = 0

    while not _count_x > grid_max_x:
        mars_grid.append([])
        while not _count_y > grid_max_y:
            mars_grid[_count_x].insert(_count_y,False)
            _count_y += 1
        _count_x += 1
        _count_y = 0
    return # returns mars_grid[x][y] = true/false

# tests against all items in nested lists, return True if all values are True in any nested lists.
###NOTE: The python functions any()/all() only work on 1 dimensional lists (top level). Built in python functions not optimized for 2 or more dimensions. So I am iterating through the 2nd dimension explicitly.
def list_test(_list):
    for _i in range(grid_max_x):
        # tests if all items in _list[n] are True (have already been traversed).
        if not all(_list[_i]):
            return(False)
    return(True)

# check if rovers current facing direction is valid (next move forward will be inside the grid)
def check_valid_direction(_rover_id):
    if _rover_id[1] == grid_max_y and _rover_id[2] == "N":
        return(False)
    elif _rover_id[0] == grid_max_x and _rover_id[2] == "E":
        return(False)
    elif _rover_id[1] == 0 and _rover_id[2] == "S":
        return(False)
    elif _rover_id[0] == 0 and _rover_id[2] == "W":
        return(False)
    else:
        return(True)

# figure out direction heading and move in that direction
def calculate_move(_heading):
    if _heading == "N":
        return(1)
    elif _heading == "E":
        return(1)
    elif _heading == "S":
        return(-1)
    elif _heading == "W":
        return(-1)
    else:
        quit("Error in calculate_move")
    return

def rotate_clockwise(_rover_id):
    # rotate rover clockwise
    _heading_id = ""
    _move_string = ""
    _move_string = _move_string + "R"
    # get the index number of the direction list
    _heading_id = direction.index(_rover_id[2])
    if _heading_id == 3: # if facing west(direction[3]) reset to North(direction[0])
        _rover_id[2] = direction[0]
    else:
        _rover_id[2] = direction[_heading_id + 1] # add 1 to the index to change the direction to the next clockwise direction. Example: North to East, East to South, etc...
    return(_move_string)

# program movements for rovers
def move_rover(_rover_id):
    global mars_grid
    _move_string = ""
    _heading_id = ""

    # fix orientation if needed
    while not check_valid_direction(_rover_id):
        # rotate clockwise
        _move_string = _move_string + str(rotate_clockwise(_rover_id))

    # move rover forward until it reaches a spot already traversed, or reaches edge of grid
    _move_space = calculate_move(_rover_id[2])
    _x = _rover_id[0]
    _y = _rover_id[1]

    if _rover_id[2] == "N" or _rover_id[2] == "S":
        _previous = _y
        _count = _y + _move_space
        try:
            while not mars_grid[_x][_count]:
                _move_string = _move_string + "M"
                mars_grid[_x][_count] = True
                _previous = _count
                _count += _move_space
                if _count >= grid_max_y + 1 or _count <= -1:
                    break
        except IndexError as error:
            quit("Error executing move_rover(): " + str(error))
        _y = _previous


    if _rover_id[2] == "E" or _rover_id[2] == "W":
        _previous = _x
        _count = _x + _move_space
        try:
            while not mars_grid[_count][_y]:
                _move_string = _move_string + "M"
                mars_grid[_count][_y] = True
                _previous = _count
                _count += _move_space
                if _count >= grid_max_y + 1 or _count <= -1:
                    break
        except IndexError as error:
            quit("Error executing move_rover(): " + str(error))
        _x = _previous


    _move_string = _move_string + str(rotate_clockwise(_rover_id))
    _new_rover_id = [_x,_y,_rover_id[2]]
    return(_move_string,_new_rover_id) # returns _rover_id's resting position after movement

### Execute commands below this line
# build the grid
build_grid()

# mark rovers starting position as traversed
mars_grid[rover_a_start[0]][rover_a_start[1]] = True
mars_grid[rover_b_start[0]][rover_b_start[1]] = True

# Move the rovers
print("rover a starting position: " + str(rover_a_start))
print("rover b starting position: " + str(rover_b_start))
print("---------------------------------------------------")
while not list_test(mars_grid):
    # Rover A movement
    movement_data = []
    print("rover a start: " + str(rover_a))
    movement_data = move_rover(rover_a)
    # Test to see if there is movement
    if movement_data[1] == rover_a:
        quit("Error: No new movement in Rover A. Exiting to prevent infinite loop.")
    else:
        rover_a = movement_data[1]
        print("rover a movement: " + str(movement_data[0]))
        print("rover a stop: " + str(rover_a))
        print("---------------------------------------------------")

    # Rover B movement
    movement_data = []
    print("rover b start: " + str(rover_b))
    movement_data = move_rover(rover_b)
    # Test to see if there is movement
    if movement_data[1] == rover_b:
        quit("Error: No new movement in Rover B. Exiting to prevent infinite loop.")
    else:
        rover_b = movement_data[1]
        print("rover b movement: " + str(movement_data[0]))
        print("rover b stop: " + str(rover_b))
        print("---------------------------------------------------")
