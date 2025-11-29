import pygame
from cell_class import Cell

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sudoku Cell Testing')

cell = Cell(9,0,0 ,screen)
cell2 = Cell(0,0,1 ,screen)

cell3 = Cell(7,1,2 ,screen)
cell3.select_or_not=True
# cell4 = Cell(0,0,3 ,screen)
start_game = True
while start_game is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            print(f" mouse is at ({x}, {y})")
    screen.fill((255,255,255))
    cell.draw()
    cell2.draw()
    cell3.draw()
    pygame.display.flip()

pygame.quit()




