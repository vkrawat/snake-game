import pygame
import random
pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)

#window
gamewindow=pygame.display.set_mode((600,600)) 
pygame.display.set_caption('snake game')
pygame.display.update()

#game variables
exit_game=False
game_over=False
snake_x=50
snake_y=50
food_x=random.randint(20,300)
food_y=random.randint(20,300)
snake_size=10
food_size=10
fps=30
clock=pygame.time.Clock()
init_velocity=5
velocity_x=0
velocity_y=0
score=0
font=pygame.font.SysFont(None,55)
def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
    

#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=init_velocity
                velocity_y=0
            elif event.key==pygame.K_LEFT:
                velocity_x=-init_velocity
                velocity_y=0
            elif event.key==pygame.K_UP:
                velocity_y=-init_velocity
                velocity_x=0
            elif event.key==pygame.K_DOWN:
                velocity_y=init_velocity
                velocity_x=0
    snake_x+=velocity_x
    snake_y+=velocity_y
    if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
        score+=10
        print('score:',score)
        food_x=random.randint(20,300)
        food_y=random.randint(20,300)
        
        

       
    gamewindow.fill(white)
    screen_score('score:'+str(score),green,5,5)
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])#displaying snake
    pygame.draw.rect(gamewindow,red,[food_x,food_y,food_size,food_size])#displaying snake
    pygame.display.update()
    clock.tick(fps)
    

pygame.quit()
quit()
        
    
