import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Heli")
done = False
clock = pygame.time.Clock()
# LOAD Images Here!
# Initialize some variables
while not done:
    # GAME UPDATE
    # KEYBOARD AND MOUSE HERE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    # DRAWING HERE
    pygame.draw.rect(screen, (0,255,0) , [20,20,30,40], 2)
    # Display what we have drawn before
    pygame.display.flip()
    clock.tick(30)
pygame.quit()