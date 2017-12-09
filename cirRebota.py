import pygame
from math import pi

pygame.init()

PINK=(50,100,150)
WHITE=(250,250,250)
largo=500
ancho=500
size = [ancho,largo]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

x=0
y=0
radio=10
by=1
bx=1
while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)
    
    
    pygame.draw.circle(screen,PINK,[radio+x,radio+y],radio)   
    if radio+y+radio < largo and by != 0:
        y=y+10
    else:
        y=y-10
    
        if y > 0:
           by=0
        else: 
            by=1
 #   x=x+i
    if radio+x+radio < ancho and bx != 0:
        x=x+1
    else:
        x=x-1
        if x > 0:
            bx=0
        else:
            bx=1
    pygame.display.flip()
pygame.quit()
