import pygame
pygame.init()
from cell_class import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.original_board = [[0 for i in range(9)] for i in range(9)]

        self.cells=[]
        for i in range(9):
            cells=[]
            for j in range(9):
                cells.append(Cell(0,i,j,self.screen))
            self.cells.append(cells)
        self.selected_x=None
        self.selected_y=None
        self.cell_size= 80                                                                         #Cell.sizeof_cell has no attribute error

    def draw(self):
        """Draws the Sudoku grid and all cells"""
        #draw grid lines
        for i in range(10):
            # Bold lines for 3x3 boxes
            line_width = 4 if i % 3 == 0 else 1

            #horizontal lines
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * self.cell_size),
                (self.width, i * self.cell_size),
                line_width
            )

            #vertical lines
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * self.cell_size, 0),
                (i * self.cell_size, self.height),
                line_width
            )
            # draw all cells
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

    def select(self, row, col):
        """Select a cell at the given row and column"""
        if self.selected_x is not None and self.selected_y is not None:
             self.cells[self.selected_x][self.selected_y].select_or_not = False
        self.selected_x = row
        self.selected_y = col
        self.cells[row][col].select_or_not = True
    #new selection


    def clear(self):

        if self.selected_x is not None:
            row, col = self.selected_x,self.selected_y
            # clears only if the cell wasn't part of the original puzzle
            if self.cells[row][col].value == 0 or self.cells[row][col].sketched_value!= 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)

    def sketch(self, value):

        if self.selected_x is not None and 1 <= value <= 9:
            row, col = self.selected_x,self.selected_y

            if self.cells[row][col].value == 0:
                self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        """Place a number in the selected cell (when Enter is pressed)"""
        if self.selected_x is not None and 1 <= value <= 9:
            row, col = self.selected_x,self.selected_y
            #only
            if self.cells[row][col].value == 0:
                self.cells[row][col].set_cell_value(value)
                self.cells[row][col].set_sketched_value(0)

    def rest_to_origin(self):

        for i in range(9):
            for j in range(9):
                original_value = self.original_board[i][j]
                self.cells[i][j].set_cell_value(original_value)
                self.board[i][j] = original_value
                self.cells[i][j].set_sketched_value(0)

    def is_full(self):
        for i in self.cells:
            for num in i:
                if num.value==0:
                    return False
        return True



    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value


    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value==0:
                    return (i,j)
        return None



    def check_board(self):
        self.update_board()
        for row in range(9):
            nums = set()
            for col in range(9):
                val = self.board[row][col]
                if val == 0:
                    return False
                if val in nums:
                    return False
                nums.add(val)

        for col in range(9):
            nums = set()
            for row in range(9):
                val = self.board[row][col]
                if val in nums:
                    return False
                nums.add(val)


        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                nums = set()
                for i in range(3):
                    for j in range(3):
                        row = box_row + i
                        col = box_col + j
                        val = self.board[row][col]
                        if val in nums:
                            return False
                        nums.add(val)

        return True


