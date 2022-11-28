import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
ball_width = 20
lives=5

x_val = 150
y_val = 200
x_direction = 4
y_direction = 4
x_padd = 0
y_padd = 20
# -- Initialise PyGame
pygame.init()
font = pygame.font.SysFont('Calibri', 25, True, False)
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False


# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


### -- Game Loop
while not done and lives>0: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        #End If
    keys = pygame.key.get_pressed() 
         ## - the up key or down key has been pressed
    
    if keys[pygame.K_UP]:
        y_padd = y_padd - 5
    if keys[pygame.K_DOWN]: 
        y_padd = y_padd + 5
    #Next event
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        #End I]f
    #Next event
# -- Game logic goes after this comment
    text = font.render("Lives left: " + str(lives), True, WHITE)
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if x_val +x_direction< x_padd+15 and y_val>=y_padd and y_val<=y_padd+60 :
        x_direction = (x_direction*-1)+1  # SPEED INCREASES
    if x_val < -20:
        x_val = 150
        y_val = 200
        x_direction = 4
        y_direction = 4
        lives=lives-1   #lose a life
    elif x_val >620:
        x_direction = x_direction*-1
    if y_val < 0:
        y_direction = y_direction*-1
    elif y_val>460:
        y_direction = y_direction*-1
   
# -- Screen background is BLACK
    screen.fill (BLACK) 
# -- Draw here 
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd,y_padd,15,60))
    screen.blit(text, [250, 250])

# -- flip display to reveal new position of objects 
    pygame.display.flip()
# - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()
