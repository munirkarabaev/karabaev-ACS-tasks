import pygame
import random
import math
# -- Global Constants
## -- Define the class snow which is a sprite
class Invader(pygame.sprite.Sprite): 
 # Define the constructor for snow 
    def __init__(self, color, width, height,speed): 
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, 600) 
        self.rect.y = random.randrange(-50,0)
        self.speed = speed
        

        #End Procedure

    def update(self): 
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 480: #pushes the invader back up to the top of the screen once it hits the bottom 
            self.rect.y= 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.Surface([2,2]) #measurements of bullet
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y
        self.speed = -2  #set it moving up at constant speed
        
    def update(self):
        self.rect.y = self.rect.y+self.speed #increment position relative to speed

class Player(pygame.sprite.Sprite): 
 # Define the constructor for snow 
    def __init__(self, color, width, height): 
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 300 
        self.rect.y = 400-height
        #speed
        self.speed=0
        #lives
        self.lives = 5
        self.score_count=0
        self.bullet_count = 50
    def player_set_speed(self, num):
        #sets speed and direction
        self.speed=num
        
        #End Procedure

    def update(self):
        #updates speed
        self.rect.x = self.rect.x + self.speed
        #stops it from going out of the screen to the right and keeps it on the edge and in place
        if self.rect.x+self.speed >=630:
            self.rect.x = 630
        #stops it from going out of the screen on the left and keeps it on the edge of the screen if the player keeps on trying to move
        elif self.rect.x+self.speed <=0:
            self.rect.x = 0

    def fire(self):
        if self.bullet_count > 0:#checks if bullets are remaining
            self.bullet_count = self.bullet_count-1
            bullet = Bullet(RED, self.rect.x+4.5, self.rect.y-20) #creates the bullet object from the middle of the top of the player
            bullet_group.add(bullet)
            all_sprites_group.add (bullet_group)

            
    def hit(self):
        self.score_count = self.score_count+5 # increments score when called
        
#End Class

# -- Colours
pygame.font.init()
font = pygame.font.SysFont('Calibri', 25, True, False)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group() 

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# Create the invaders 
number_of_invader = 10 # 
player = Player(YELLOW,10,10)
for x in range (number_of_invader): 
    my_invader = Invader(BLUE, 10, 10,1) 
    invader_group.add (my_invader) # adds the new invader to the group of invader
    all_sprites_group.add (my_invader) # adds it to the group of all Sprites
    
#Next
all_sprites_group.add (player)


### -- Game Loop 
while not done and player.lives >0: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        #End If
        elif event.type == pygame.KEYDOWN: # - a key is down
        
            if event.key == pygame.K_LEFT: # - if the left key pressed
            
                player.player_set_speed(-3) # speed set to -3
            
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
            
                player.player_set_speed(3) # speed set to 3

            #end if
        elif event.type == pygame.KEYUP: # - a key released
        
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                player.player_set_speed(0) # speed set to 0

            elif event.key == pygame.K_UP:
                player.fire()   # if up key is released will fire a bullet
            #end if

                
        #end if

                
    #Next event

                
# -- Game logic goes after this comment
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)# collision with player and invaders
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group,invader_group,True,True,collided=None)#group collision with the bullet group and invader group
        
        
  

    for foo in bullet_hit_group:
        player.hit() # will call the hit function and increment the score for each bullet hit
    #next foo    

    
    for foo in player_hit_group: 
        player.lives = player.lives - 1
    #next foo
    all_sprites_group.update() 
# - Screen background is BLACK 
    screen.fill (BLACK) 
# -- Draw here 
    all_sprites_group.draw (screen)
    text_lives = font.render("Lives: " + str(player.lives), False, WHITE)
    text_score = font.render("Score: " + str(player.score_count), False, WHITE)
    text_bullets = font.render("Bullets: " + str(player.bullet_count), False, WHITE)
    screen.blit(text_lives,(50,20))#draws lives
    screen.blit(text_score,(50,60))#draws score
    screen.blit(text_bullets,(50,100))#draws bullets remaining











# -- flip display to reveal new position of objects 
    pygame.display.flip()
# - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()
