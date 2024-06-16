# This is a Python script using the Pygame library to create a Sudoku game and solver. I'll explain the main components and functionality of the code:
# Initialization:
# Pygame is imported, and its font module is initialized.
# The window size is set to 503x570 pixels.
# The window title is set to "SUDOKU GAME AND SOLVER," and an icon is loaded.
# Default Sudoku Board:
# A 9x9 Sudoku grid (grid) is defined as a list of lists, representing the initial state of the Sudoku board.
# Fonts:
# Two fonts (font1 and font2) are loaded for displaying text in the game.
# Functions:
# get_cord(pos): Takes the mouse position and updates the global variables x and y based on the grid position.
# draw_box(): Draws a red box around the currently selected cell.
# draw(): Draws the Sudoku grid, including the numbers and lines.
# draw_val(val): Draws the specified value in the currently selected cell.
# raise_error1() and raise_error2(): Display error messages when wrong values are entered.
# valid(m, i, j, val): Checks if a given value is valid in the specified position of the grid.
# solve(grid, i, j): Solves the Sudoku board using a backtracking algorithm.
# instruction(): Displays instructions for the game.
# result(): Displays a message when the Sudoku puzzle is successfully solved.
# Main Loop:
# The main loop runs until the user quits the game (run = False).
# Event handling is done for mouse clicks and key presses.
# Arrow keys are used to navigate the grid, and number keys (1-9) are used to input values into cells.
# "Enter" key triggers the visualization of the solution using the solve function.
# "R" key resets the board to a new Sudoku puzzle, and "D" key resets it to the default puzzle.
# Rendering and Display:

# The window is updated and rendered in each iteration of the main loop.
# The screen is filled with a white background, and various functions are called to draw the Sudoku grid, cells, and messages.
# Termination:

# The Pygame window is closed when the user quits the game.
# Explaining functions in detail- 
# get_cord(pos)

# This function takes the mouse position (pos) as an argument.
# It updates the global variables x and y based on the grid position.
# The grid position is calculated by dividing the mouse coordinates by the cell size (dif).
# draw_box()

# This function is responsible for drawing a red box around the currently selected cell (x, y).
# It uses the Pygame draw.line function to draw horizontal and vertical lines around the cell, creating a box effect.
# draw()

# Draws the Sudoku grid, including the numbers and lines.
# The function iterates through the 9x9 grid and:
# Fills the background of cells with numbers in blue.
# Renders the default numbers on the board using font1.
# Draws horizontal and vertical lines to form the grid.
# draw_val(val)

# Takes a value (val) as an argument and draws it in the currently selected cell (x, y).
# Uses font1 to render the value at a specific position on the screen.
# raise_error1() and raise_error2()

# Display error messages when wrong values are entered.
# raise_error1() displays "WRONG !!!" at the bottom of the screen.
# raise_error2() displays "Wrong !!! Not a valid Key" at the bottom of the screen.
# valid(m, i, j, val)

# Checks if a given value (val) is valid in the specified position (i, j) of the grid (m).
# It checks if the value is not present in the same row, column, or 3x3 subgrid.
# Returns True if the value is valid, False otherwise.
# solve(grid, i, j)

# Solves the Sudoku board using a backtracking algorithm.
# The function uses recursion to fill in values for empty cells.
# It backtracks when it encounters an invalid state.
# The visualization of the solving process is achieved by updating the Pygame window during the solving process.
# instruction()

# Displays instructions for the game at the bottom of the window.
# Informs the user to press "D" to reset to default or "R" to empty, enter values, and press enter to visualize.
# result()

# Displays a message at the bottom of the window when the Sudoku puzzle is successfully solved.
# Informs the user to press "R" or "D" to reset the board.
# Main Loop

# The main loop runs until the user quits the game.
# Handles various events such as mouse clicks and key presses.
# Allows the user to navigate the grid, input values, and visualize the solution.
# Resets the board to default or empty based on user input.
