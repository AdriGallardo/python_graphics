import pygame
pygame.init()

def traslacion(x,y):
    i=250+x
    j=250-y
    c=[i,j]
    return c

def conversion(x,y,z):
    j=((500-y)*z/500)+y
    i=(-x*z/500)+x
    T=traslacion(i,j)
    return T

WHITE=(255,255,255)
BLACK=(  0,  0,  0)
BLUE=(0,200,250)
RED=(0,250,0)
GREEN=(250,0,0)
BROWN=(230,187,140)
PINK=(230,178,231)

size=[500,500]
screen = pygame.display.set_mode(size)

done=False
clock = pygame.time.Clock()

z=0
while not done:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    j=0
    screen.fill(PINK)
    for z in range(200,0,-25):
        k=0
        j=j+1
        for i in range(0,400,50):
            k=k+1
            #cara del fondo
            N1=conversion(-150+i,-100,25+z)
            N2=conversion(-200+i,-100,25+z)
            N3=conversion(-200+i,-150,25+z)
            N4=conversion(-150+i,-150,25+z)
            #cara del fente
            N5=conversion(-150+i,-100,0+z)
            N6=conversion(-200+i,-100,0+z)
            N7=conversion(-200+i,-150,0+z)
            N8=conversion(-150+i,-150,0+z)
            if j%2 == 0:
                if k%2 == 0:
                    COLOR=BLACK
                else: COLOR=WHITE
            else:
                if k%2 == 0:
                    COLOR=WHITE
                else:
                    COLOR=BLACK
#        pygame.draw.polygon(screen,BLUE,[N1,N2,N3,N4],0)
#        pygame.draw.polygon(screen,RED,[N4,N3,N7,N8],0)
#        pygame.draw.polygon(screen,GREEN,[N1,N4,N8,N5],0)
#        pygame.draw.polygon(screen,GREEN,[N2,N3,N7,N6],0)
            pygame.draw.polygon(screen,COLOR,[N1,N2,N6,N5],0)
            pygame.draw.polygon(screen,COLOR,[N5,N6,N7,N8],0)
    
    M1=conversion(-190,-70,0)
    M2=conversion(-190,-118,0)
    M3=conversion(190,-118,0)
    M4=conversion(190,-70,0)
    pygame.draw.polygon(screen,BROWN,[M1,M2,M3,M4],0)
    
    pygame.display.flip()

pygame.quit()
