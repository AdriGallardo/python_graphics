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
#    T=[i,j]
    return T


x=-50
y=25
z=25
alto=50
COLOR=(12,18,103)
COLOR2=(23,45,62)
WHITE=(255,255,255)

size = [500,500]
screen = pygame.display.set_mode(size)

done= False
clock= pygame.time.Clock()


while not done:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill(WHITE)
    N=conversion(x,y,z)
    N.append(2*abs((-x*z/250)+x))
    #calcular la altura del rectangulo:
    y2=-y
    j=((250-y)*z/250)+y
    j2=((250-y2)*z/250)+y2
    alto=abs(j-j2)
    N.append(alto)
 #   N.append(-2*x*(z-250)/(250-y))
    pygame.draw.rect(screen,COLOR2,N)
    
    z=z+1
    pygame.display.flip()

pygame.quit()

