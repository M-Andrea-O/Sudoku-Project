import pygame
pygame.init()
from cell_class import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        self.cells=[]
        for i in range(9):
            cells=[]
            for j in range(9):
                cells.append(Cell(0,i,j,self.screen))
            self.cells.append(cells)
        self.selected_x=None
        self.selected_y=None
        
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
        if self.selected:
            prev_row, prev_col = self.selected
            self.cells[prev_row][prev_col].selected = False
        
        #new selection
        self.selected = (row, col)
        self.cells[row][col].selected = True

    def clear(self):

    def sketch(self,value):

    def place_number(self,value):

    def rest_to_origin(self):

    def is_full(self):

    def update_board(self):

    def find_empty(self):

    def check_board(self):


