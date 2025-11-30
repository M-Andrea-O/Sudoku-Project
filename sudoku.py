

import pygame, sys
from Board_Class import Board
from sudoku_generator import generate_sudoku
pygame.init()

WIDTH,HEIGHT = 540,640
SCREEN =pygame.display.set_mode((WIDTH, HEIGHT))

LEVEL_Easy=30
LEVEL_Medium=40
LEVEL_HARD=50

CLEARED="Game Won!"
UNSUCCESSFUL_CLEAR="Game Over :("


BACKGROUND_COLOR = (150,170,190)
ORANGE=(255, 165, 0)


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
            return self.rect.collidepoint(pos)

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
        print_text("Welcome to Sudoku",60,HEIGHT//3.5,(0,0,0),True)
        print_text('Select Game Mode:',40,HEIGHT//2,(0,0,0),True)
        buttons=[Buttons(WIDTH//41, HEIGHT//3, 170, 80, 'EASY', (255, 165, 0)),
            Buttons(WIDTH//2.875, HEIGHT//3, 170, 80, 'MEDIUM', (255, 165, 0)),
            Buttons(WIDTH//1.4955, HEIGHT//3, 170, 80, 'HARD', (255, 165, 0))]
        for button in buttons:
            button.create()
        return buttons

def game_in_progress(board):
    SCREEN.fill((150,170,190))
    board.draw()
    buttons = [Buttons(WIDTH//38, HEIGHT//(5/4.4), 165, 80, 'RESET', (255, 165, 0)),
               Buttons(WIDTH//2.755, HEIGHT//(5/4.4), 165, 80, 'RESTART', (255, 165, 0)),
               Buttons(WIDTH//(5/3.45), HEIGHT//(5/4.4), 165, 80, 'EXIT', (255, 165, 0))]
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

def new_board(difficulty):

    return Board(WIDTH,HEIGHT,SCREEN,difficulty)

def main():
    pygame.init()
    FPS = pygame.time.Clock()
    game_status= "menu"
    board = None
    buttons = []
    difficulty = "easy"

    run = True
    while run:

        FPS.tick(120)

        pygame.display.flip()
        if game_status == "menu":
            buttons = main_menu()
        elif game_status == "middle":
            buttons = game_in_progress(board)
        elif game_status == "won":
            buttons = win()
        elif game_status == "lose":
            buttons = lose()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if game_status== "menu":
                    buttons = main_menu()
                    if buttons[0].check_clicked(pos):
                        difficulty = "easy"
                        board=new_board(difficulty)
                        game_status = "middle"
                    elif buttons[1].check_clicked(pos):
                        difficulty = "medium"
                        board = new_board(difficulty)
                        game_status = "middle"
                    elif buttons[2].check_clicked(pos):
                        difficulty = "hard"
                        board=new_board(difficulty)
                        game_status = "middle"
                        # print("hard")

                elif game_status== "middle":
                    if buttons[0].check_clicked(pos):
                        board.rest_to_origin()
                    elif buttons[1].check_clicked(pos):
                        game_status = "menu"
                        board = None
                    elif buttons[2].check_clicked(pos):
                        run = False
                    else:
                        row, col = board.click(pos[0], pos[1])
                        if row != None and col != None and row>=0 and col>=0:
                            board.select(row,col)
                elif game_status =="won":
                    if buttons.check_clicked(pos):
                        game_status = "menu"
                        board=None

                elif game_status=="lose":
                    if buttons[0].check_clicked(pos):
                        game_status = "menu"
                        board=None

            if event.type == pygame.KEYDOWN and game_status == "middle":
                if event.key == pygame.K_1:
                    board.sketch(1)
                elif event.key == pygame.K_2:
                    board.sketch(2)
                elif event.key == pygame.K_3:
                    board.sketch(3)
                elif event.key == pygame.K_4:
                    board.sketch(4)
                elif event.key == pygame.K_5:
                    board.sketch(5)
                elif event.key == pygame.K_6:
                    board.sketch(6)
                elif   event.key == pygame.K_7:
                    board.sketch(7)
                elif event.key == pygame.K_8:
                    board.sketch(8)
                elif event.key == pygame.K_9:
                    board.sketch(9)
                elif event.key==pygame.K_RETURN:
                    if board.selected_x is not None and board.selected_y is not None:
                        entered_val=board.cells[board.selected_x][board.selected_y].sketched_value
                        if entered_val != 0:
                            board.place_number(entered_val)


                            if board.is_full():
                                if board.check_board():
                                    game_status = "won"
                                else:
                                    game_status = "lose"
                elif event.key == pygame.K_BACKSPACE:
                    board.clear()


    pygame.quit()





        




if __name__=="__main__":
    main()









