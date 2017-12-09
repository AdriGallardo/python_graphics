import pygame
pygame.init()
def abs(x):
    if x>=0:
        return x
    else:
        return -x

def traslacion(x,y):
    i=250+x
    j=250-y
    c=[i,j]
    return c
 
def conversion(x,y,z):
    j=((250-y)*z/250)+y
    i=(-x*z/250)+x
    T=traslacion(i,j)
    return T

COLOR1=(0,0,255)
COLOR2=(0,255,0)
COLOR3=(255,0,0)
COLOR4=(34,76,187)
WHITE=(255,255,255)

size=[500,500]
screen = pygame.display.set_mode(size)

done=False
clock = pygame.time.Clock() 

z=60
while not done:
    clock.tick(24)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill(WHITE)
   #cara del fondo
    N1=conversion(-50,50,50)
    N2=conversion(-150,50,50)
    N3=conversion(-150,-50,50)
    N4=conversion(-50,-50,50)
    #cara del fente
    N5=conversion(-50,50,0)
    N6=conversion(-150,50,0)
    N7=conversion(-150,-50,0)
    N8=conversion(-50,-50,0)


    pygame.draw.polygon(screen,COLOR1,[N1,N2,N3,N4],0)
    pygame.draw.polygon(screen,COLOR2,[N4,N3,N7,N8],0)
    pygame.draw.polygon(screen,COLOR3,[N1,N4,N8,N5],0)
    pygame.draw.polygon(screen,COLOR3,[N2,N3,N7,N6],0)
    pygame.draw.polygon(screen,COLOR2,[N1,N2,N6,N5],0)    
    pygame.draw.polygon(screen,COLOR1,[N5,N6,N7,N8],0)

    pygame.display.flip()
 
pygame.quit()
