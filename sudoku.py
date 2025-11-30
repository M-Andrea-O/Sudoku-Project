

import pygame
from Board_Class import Board
from sudoku_generator import generate_sudoku
pygame.init()

WIDTH,HEIGHT = 720,800
SCREEN =pygame.display.set_mode((WIDTH, HEIGHT))

LEVEL_Easy=30
LEVEL_Medium=40
LEVEL_HARD=50

CLEARED="Game Won!"
UNSUCCESSFUL_CLEAR="Game Over :("


class Buttons:
    def __init__(self,x,y,w,h,text,color):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.text = text
        self.color= color
        self.font = pygame.font.SysFont('arial', 40)
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

    def check_clicked(self,pos):
            return pygame.self.rect.collidepoint(pos)

    def create (self):
        pygame.draw.rect(SCREEN, self.color, self.rect)
        pygame.draw.rect(SCREEN, (0,0,0), self.rect, 3)
        text = self.font.render(self.text, True, (255,255,255))
        SCREEN.blit(text, text.get_rect(center=self.rect.center))
def print_text(text,size,y,color=(0,0,0),bold=False):
        font=pygame.font.SysFont('arial', size,bold=bold)

        surf = font.render(text, True, color)
        SCREEN.blit(surf, surf.get_rect(center=(WIDTH // 2, y)))



def main_menu():
        SCREEN.fill((150,170,190))
        print_text("Welcome to Sudoku",70,HEIGHT//3.5,(0,0,0),True)
        print_text('Select Game Mode:',40,HEIGHT//2,(0,0,0),True)
        buttons=[Buttons(WIDTH//6, HEIGHT//3, 180, 80, 'EASY', (255, 165, 0)),
            Buttons(WIDTH//4, HEIGHT//3, 180, 80, 'MEDIUM', (255, 165, 0)),
            Buttons(WIDTH//2, HEIGHT//3, 180, 80, 'HARD', (255, 165, 0))]
        for button in buttons:
            button.create()
        return buttons
def game_in_progress(board):
    SCREEN.fill((150,170,190))
    board.draw()
    buttons = [Buttons(WIDTH // 6, HEIGHT // 3, 180, 80, 'RESET', (255, 165, 0)),
               Buttons(WIDTH // 4, HEIGHT // 3, 180, 80, 'RESTART', (255, 165, 0)),
               Buttons(WIDTH // 2, HEIGHT // 3, 180, 80, 'EXIT', (255, 165, 0))]
    for button in buttons:
        button.create()
    return buttons

def win():
    SCREEN.fill((150,170,190))
    print_text(CLEARED,70,HEIGHT//2,(0,0,0),True)
    button = Buttons(260, 450, 200, 80, 'EXIT', ORANGE)
    button.create()
    return button


def lose():
    SCREEN.fill(BACKGROUND_COLOR)
    print_text(UNSUCCESSFUL_CLEAR,70,HEIGHT//2,(0,0,0),True)
    button = Buttons(260, 450, 200, 80, 'RESTART', ORANGE)
    button.create()
    return button


def new_board():
    return Board(WIDTH,HEIGHT,SCREEN,Board.difficulty)




def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    game_status= "Start Up"
    board = None
    buttons = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
        if game_status== "Start Up":
            if buttons[0].check_clicked(pos):
                board=new_board("easy")
                state = "middle"
            elif buttons[1].check_clicked(pos):
                board=new_board("medium")
                state = "middle"
            elif buttons[3].check_clicked(pos):
                board=new_board("hard")
                state = "middle"

        elif game_status== "Middle":
            if buttons[0].check_clicked(pos):
                board.rest_to_origin()
            elif buttons[1].check_clicked(pos):
                game_status = "menu"
                board = None
            elif buttons[2].check_clicked(pos):
                run = False
        




if __name__=="__main__":
    main()







BACKGROUND_COLOR = (150,170,190)
ORANGE=(255, 165, 0)


