import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.Font('arial.ttf',25)

Point = namedtuple('Point', 'x,y')

#RGB COLORS
WHITE = (255,255,255)
RED = (200,0,0)
BLACK = (0,0,0)
BLUE1 = (0,0,255)
BLUE2 = (0,100,255)

BLOCK_SIZE = 20
SPEED = 40

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGame():
    # en ve boy
    def __init__(self, w = 640, h = 480):
        self.w = w
        self.h = h
    
        # pygame ekranı ayarlama
        self.display = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        #başlangıç durumları
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2 , self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x=random.randint(0,(self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y=random.randint(0,(self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()  


    def play_step(self):
        # 1. user input al

        # 2. hareketi yap

        # 3. oyunun bitip bitmediğini kontrol et

        # 4. hareket et ya da _place_food (yemeği yemiş)
        
        # 5. ui ve clock güncelle
        self.update_ui()
        self.clock.tick(SPEED) 

        # 6. oyun bitişini ve sonucu döndür
        game_over = False
        return game_over, self.score
    
    def update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display,BLUE1, pygame.Rect(pt.x,pt.y,BLOCK_SIZE,BLOCK_SIZE)) # 20 ye 20 rectangle
            pygame.draw.rect(self.display,BLUE1, pygame.Rect(pt.x+4,pt.y+4,12,12)) # x+4 konumundan 12 ye 12 rectanngle

        pygame.draw.rect(self.display,RED,pygame.Rect(self.food.x,self.food.y,BLOCK_SIZE,BLOCK_SIZE))

        text = font.render("Score: " + str(self.score),True,WHITE)
        self.display.blit(text, [0,0])
        pygame.display.flip()

if __name__ == '__main__':
    game = SnakeGame()

    # loop
    while True:
        game_over, score = game.play_step()

        #oyun bitişi kontrolü
        if game_over == True:
            break   #döngüden çıkış

    pygame.quit()