import pygame

pygame.init()

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.select_or_not=False
        self.sizeof_cell=80

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        black_color = (0, 0, 0)
        x= (self.sizeof_cell*self.col)
        y=(self.row*self.sizeof_cell)

        if self.select_or_not is True:
            bg_color = (255,0,0)
        else:
            bg_color = (150,170,190)
        bg_color2=(0,0 ,0)
        pygame.draw.rect(self.screen,bg_color,(x,y,self.sizeof_cell,self.sizeof_cell),0)
        pygame.draw.rect(self.screen,bg_color2,(x,y,self.sizeof_cell,self.sizeof_cell),2)
        number=self.value

        if number != 0:
            font = pygame.font.SysFont('comicsans', 30)
            number_str = str(number)
            number=font.render(number_str, True, black_color)

            text_location=number.get_rect(center=(x+self.sizeof_cell//2, y+self.sizeof_cell//2))
            self.screen.blit(number,text_location)




