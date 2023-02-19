 # to make screen
import pygame
import random

pygame.init
#colors
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
blue=(100,149,237)
red=(178,34,34)
width=800
height=400
run=True
clock=pygame.time.Clock()
fps = 60

screen= pygame.display.set_mode((width,height))
pygame.display.set_caption('Dino')
obs_width = 30
obs_height = 30
obs_x=600
obs_y=height-110
obs=pygame.Rect(obs_x,obs_y,obs_width,obs_height)
#base
base_width=width
base_height=100
base_x=0
base_y=height-80
base=pygame.Rect(base_x,base_y,base_width,base_height)
#dino
dino_x=150
dino_y=height-120
dino_width=40
dino_height=40
dino=pygame.Rect(dino_x,dino_y,dino_width,dino_height)
gravity = -20


font=pygame.font.SysFont('Arial',40)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino.bottom == height-80:
                gravity = -20

    screen.fill(white)
    pygame.draw.rect(screen,black,base)
    pygame.draw.rect(screen,red,obs)
    pygame.draw.ellipse(screen,yellow,dino)

    obs.x=obs.x-6
    if obs.right  <0 :
        obs.left=width
    gravity=gravity+1
    dino.y=dino.y+gravity
    if dino.bottom >= height-80:
        dino.bottom=height-80
    if dino.colliderect(obs):               
        run = False

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
