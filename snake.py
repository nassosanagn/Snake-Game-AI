import pygame
import time
import random
from tkinter import *
from pygame import mixer
from pygame.constants import MOUSEBUTTONDOWN
 
pygame.init()
 
snake_head = pygame.image.load(r'C:\Users\user\Desktop\games\snake_head_5.png')    # Snake's head image
food_im = pygame.image.load(r'C:\Users\user\Desktop\games\fruit.png')               # fruit image
snakes_body = pygame.image.load(r'C:\Users\user\Desktop\games\snk.png')                      # snake's body
sound_image = pygame.image.load(r'C:\Users\user\Desktop\games\sound.png')  
no_sound_2 = pygame.image.load(r'C:\Users\user\Desktop\games\no_sound_2.png')  


# All colors used 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
green2 = (92,182,107)
dark_green = (4,75,20)
blue = (50, 153, 213)

playground_green = (168,208,75)
outside_green = (95,138,53)

game_start_width = 50;
game_start_height = 75;

# Background music for the game
mixer.music.load('background_music.mp3')
mixer.music.play(-1)

dis_width = 600
dis_height = 520
line_height = 40;
 
#dis = pygame.display.set_mode((dis_width, dis_height + line_height))
dis = pygame.display.set_mode((700,630))
pygame.display.set_caption('Snake Game by Nassos')
clock = pygame.time.Clock()
 
snake_block = 20
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.Font("whizkid.ttf", line_height)


# -------------------------------------------------- Button Code -------------------------------------------------- #

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen   
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

# -------------------------------------------------------------------------------------------------------------------- #

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    i = 1
    pygame.draw.line(dis, white, (0, line_height), (800, line_height))
    
    for x in snake_list:
        if i == len(snake_list):
            dis.blit(pygame.transform.scale(snake_head, (snake_block + 15, snake_block + 15)), (x[0], x[1]))
        else:
            dis.blit(pygame.transform.scale(snakes_body, (snake_block + 9, snake_block + 9)), (x[0], x[1]))
        i = i + 1
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    
    soundButton = button(red, 660, 10, 30, 25 , "")

    isPaused = False
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(game_start_width, dis_width + game_start_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(game_start_height, dis_height + game_start_height - snake_block) / 20.0) * 20.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if soundButton.isOver(pos):
                    if isPaused:
                       pygame.mixer.music.unpause()
                       isPaused = False
                    else:   
                       pygame.mixer.music.pause()
                       isPaused = True
                   
 
        if x1 >= (dis_width + game_start_width) or x1 < (game_start_width - snake_block) or y1 >= (dis_height + game_start_height) or y1 < (game_start_height - snake_block):
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        clickSettings = False 
        dis.fill(outside_green)               # Background is green

        if isPaused:
            dis.blit(pygame.transform.scale(no_sound_2, (30, 25)),(660,10))                            # Volume icon
        else:
            dis.blit(pygame.transform.scale(sound_image, (30, 25)),(660,10))                            # Muted icon

        pygame.draw.rect(dis, playground_green, [game_start_width, game_start_height, 600, 520])                                   # draw the play area
        # pygame.draw.line(dis, black, (game_start_width, game_start_height), (700, 100))
        
        settingsButton = pygame.Rect(750, 10, 50, 20)
        # pygame.draw.rect(dis, red, settingsButton)                                          # settings button
        mx, my = pygame.mouse.get_pos()

        if settingsButton.collidepoint((mx,my)):
            if clickSettings:
                pass

        dis.blit(pygame.transform.scale(food_im, (snake_block + 12, snake_block + 12)), (foodx, foody))
       
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(game_start_width, dis_width + game_start_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(game_start_height, dis_height + game_start_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)


 
    pygame.quit()
    quit()
 
gameLoop()