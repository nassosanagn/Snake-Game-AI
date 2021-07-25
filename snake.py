import pygame
import time
import random

from pygame.constants import MOUSEBUTTONDOWN
 
pygame.init()
 
snake_head = pygame.image.load(r'C:\Users\user\Desktop\games\snake_head2.png')    # Snake's head image
food_im = pygame.image.load(r'C:\Users\user\Desktop\games\strawberry.png')       # Snake's head image
snk = pygame.image.load(r'C:\Users\user\Desktop\games\snk.png')                 # Snake's head image
tail = pygame.image.load(r'C:\Users\user\Desktop\games\snake_tail.jpg')

# All colors used 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
green2 = (92,182,107)
dark_green = (4,75,20)
blue = (50, 153, 213)

game_start = 100;
game_height = 600;

dis_width = 600
dis_height = 600
line_height = 30;
 
#dis = pygame.display.set_mode((dis_width, dis_height + line_height))
dis = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake Game by Nassos')
clock = pygame.time.Clock()
 
snake_block = 25
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.Font("whizkid.ttf", line_height)

 
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    i = 1
    pygame.draw.line(dis, white, (0, line_height), (800, line_height))
    
    for x in snake_list:
        if i == len(snake_list):
            dis.blit(pygame.transform.scale(snake_head, (snake_block, snake_block)), (x[0], x[1]))
        elif len(snake_list) > 2 and i == 1:
            dis.blit(pygame.transform.scale(tail, (snake_block, snake_block)), (x[0], x[1]))
        else:
            dis.blit(pygame.transform.scale(snk, (snake_block, snake_block)), (x[0], x[1]))
        i = i + 1
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# def settingsMenu():
#     while True:
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1

 
    foodx = round(random.randrange(game_start, dis_width + game_start - snake_block) / 25.0) * 25.0
    foody = round(random.randrange(game_start, dis_height + game_start - snake_block) / 25.0) * 25.0
 
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
 
        if x1 >= (dis_width + game_start) or x1 < game_start or y1 >= (dis_height + game_start) or y1 < game_start:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        clickSettings = False 
        dis.fill(dark_green)                                                                  # Background is black
        pygame.draw.rect(dis, green2, [100, 100, 600, 600])                                   # draw the play area
        pygame.draw.line(dis, black, (100, 100), (700, 100))
        
        settingsButton = pygame.Rect(750, 10, 50, 20)
        pygame.draw.rect(dis, red, settingsButton)                                          # settings button
        mx, my = pygame.mouse.get_pos()

        if settingsButton.collidepoint((mx,my)):
            if clickSettings:
                pass

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clickSettings = True

        
        #pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        dis.blit(pygame.transform.scale(food_im, (snake_block, snake_block)), (foodx, foody))
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
            foodx = round(random.randrange(game_start, dis_width + game_start - snake_block) / 25.0) * 25.0
            foody = round(random.randrange(game_start, dis_height + game_start - snake_block) / 25.0) * 25.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()