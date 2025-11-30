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

    def select(self, row, col):

    def clear(self):

    def sketch(self,value):

    def place_number(self,value):

    def rest_to_origin(self):

    def is_full(self):
        for i in self.cells:
            for num in i:
                if num.value==0:
                    return False
        return True



    def update_board(self):


    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value==0:
                    return (i,j)
        return None



    def check_board(self):


