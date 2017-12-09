import pygame
pygame.init()

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

print "Introduce un punto de coordenadas (x,y,z):"
print "x:"
x=input()
print "y:"
y=input()

z=0

COLOR=(12,18,103)
WHITE=(255,255,255)

size=[500,500]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    
    N=conversion(x,y,z) 
    pygame.draw.circle(screen, COLOR,N,3) 
    z=z+5
    if z >= 250:
        z = 0
  
    pygame.display.flip()

pygame.quit()
