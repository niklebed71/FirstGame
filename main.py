import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Create a game and a window
pygame.init()  # the command that starts pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))# the program window is created when we set the size in the settings.
pygame.display.set_caption("My first python game")
clock = pygame.time.Clock()

# Add a font and draw the number of points.Account variable,need to draw on the screen.
font_name = pygame.font.match_font('arial')# Searches for the most suitable font in the system.
def draw_text(surf, text, size, x, y):# Сreate a function that draws the number of points
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)#Drawing text on the screen is called "rendering". 
    #True, is responsible for turning anti-aliasing on and off.
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen():# screen display at the start of the game
    draw_text(screen, "FIRST PYGAME GAME", 48, WIDTH / 2, HEIGHT / 4 -50)
    draw_text(screen, "Rules of the game.", 24,WIDTH / 2, HEIGHT / 2 - 50)
    draw_text(screen, " Goal: score the maximum number of points by moving the robot ", 14,WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "with the arrows left - right, collecting coins. ", 14,WIDTH / 2, HEIGHT / 2 +20)
    draw_text(screen, "When a robot collides with a triangle, the player receives a penalty of 10 points. ", 14,WIDTH / 2, HEIGHT / 2 +50)
    draw_text(screen, "When a robot collides with a coin, the player receives 5 points. ", 14,WIDTH / 2, HEIGHT / 2 +80)
    draw_text(screen, "When a robot collides with a monster, the game over. ", 14,WIDTH / 2, HEIGHT / 2 +110)
    #   
    draw_text(screen, "Press any key to begin or X for exit", 18, WIDTH / 2, HEIGHT * 3 / 4 +50)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# Download game graphics
robot = pygame.image.load("robo.png")
ovi = pygame.image.load("ovi.png")
coin = pygame.image.load("kolikko.png")
hirvio = pygame.image.load("hirvio.png")

class Player(pygame.sprite.Sprite): #class tells Python that a new object is being defined, which will be the player's sprite. 
    #Its type is pygame.sprite.Sprite.This means that it will be based on the Sprite class predefined in Pygame.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #runs the initializer of built-in Sprite classes
        self.image = robot # define an image property. Every sprite in Pygame must have two properties: image and rect.
        self.rect = self.image.get_rect() #define the rect of the sprite. It's short for rectangle.
        self.rect.centerx = WIDTH / 2 # determine the location of the sprite by width (center)
        self.rect.bottom = HEIGHT - 10 # determine the location of the sprite by height
        self.speedx = 0 # determine the speed of the sprite
        
    def update(self):# on every game loop, the Player sprite will be updated
        self.speedx = 0# initial speed 0
        keystate = pygame.key.get_pressed()# function returns a dictionary with all keyboard keys and values True or False
        if keystate[pygame.K_LEFT]: # if K_LEFT is pressed
            self.speedx = -8 # x speed -8
        if keystate[pygame.K_RIGHT]:# if K_RIGHT is pressed
            self.speedx = 8 # x speed 8
        self.rect.x += self.speedx # self.rect is the triangle of our sprite, assign it a speed
        if self.rect.right > WIDTH: # sprite stop at the edge of the screen.
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0  

class Mob(pygame.sprite.Sprite):# ovi sprite.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #runs the initializer of built-in Sprite classes
        self.image = ovi #  define an image property.
        self.rect = self.image.get_rect()# define the rect of the sprite.
        self.rect.x = random.randrange(WIDTH - self.rect.width)# limit the random x position of rect to the width
        self.rect.y = random.randrange(-100, -40)# limit a random position in height
        self.speedy = random.randrange(5, 8)# determine the speed of the sprite with a random speed from 5 to 8 by y
       
    def update(self):
        self.rect.y += self.speedy# for the update function, need to set the movement of the sprite at a certain speed
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
       #when the sprite gets to the bottom, move it to a random place at the top        
            self.rect.x = random.randrange(WIDTH - self.rect.width)# limit on a random location on x
            self.rect.y = random.randrange(-100, -40)# limit on a random location on у
            self.speedy = random.randrange(1, 8) # random speed selection  

class Coin(pygame.sprite.Sprite):# kolikko sprite.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #runs the initializer of built-in Sprite classes
        self.image = coin #  define an image property.
        self.rect = self.image.get_rect()# define the rect of the sprite.
        self.rect.x = random.randrange(WIDTH - self.rect.width)# limit the random x position of rect to the width
        self.rect.y = random.randrange(-100, -40)# limit a random position in height
        self.speedy = random.randrange(3, 8)# determine the speed of the sprite with a random speed from 3 to 8 by y
        self.speedx = random.randrange(-3, 3)# and from -3 to 3 x
  
    def update(self):# for the update function, need to set the movement of the sprite at a certain speed
        self.rect.x += self.speedx# take speeds from self.speedx
        self.rect.y += self.speedy# and self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -20 or self.rect.right > WIDTH + 20:
       # when the sprite gets to the bottom, move it to a random place at the top      
            self.rect.x = random.randrange(WIDTH - self.rect.width)# limit on a random location on x
            self.rect.y = random.randrange(-100, -40)# limit on a random location on  у
            self.speedy = random.randrange(1, 5) # random speed selection  

class Hirvio(pygame.sprite.Sprite):# hirvio sprite.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #runs the initializer of built-in Sprite classes
        self.image = hirvio # define an image property.
        self.rect = self.image.get_rect()#define the rect of the sprite.
        self.rect.x = random.randrange(WIDTH - self.rect.width)# limit the random x position of rect to the width
        self.rect.y = random.randrange(-100, -40)# limit a random position in height
        self.speedy = random.randrange(3, 8)# determine the speed of the sprite with a random speed from 3 to 8 by y
        self.speedx = random.randrange(-3, 3)# and from -3 to 3 x
  
    def update(self):# for the update function, need to set the movement of the sprite at a certain speed
        self.rect.x += self.speedx# take speeds from self.speedx
        self.rect.y += self.speedy# and self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
       #  when the sprite gets to the bottom, move it to a random place at the top           
            self.rect.x = random.randrange(WIDTH - self.rect.width)# limit on a random location on x
            self.rect.y = random.randrange(-100, -40)# limit on a random location on  у
            self.speedy = random.randrange(5, 10) # random speed selection  

#Game loop
game_over = True # create a game_over variable at the beginning:
running = True
while running:
    if game_over:
        show_go_screen()# go to this function
        game_over = False
        all_sprites = pygame.sprite.Group()#collect all sprites to update and draw them together
        mobs = pygame.sprite.Group()
        coins = pygame.sprite.Group()
        hirvios = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)# add a sprite to the group all_sprites.
        score = 0

        for i in range(8):# there are a lot of coins,need create a coins group for all of them
            c = Coin()
            all_sprites.add(c)
            coins.add(c)

        for i in range(4):#There are a lot of triangles, need to create a group of mobs for them all
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            
        for i in range(1):#There are many hirvios, need to create a group of hirvios for them all
            h = Hirvio()
            all_sprites.add(h)
            hirvios.add(h)

    # Keeping the cycle at the right speed
    clock.tick(FPS)# tick() asks pygame to determine how long the loop is taking, and to pause so that the loop takes the time it needs.
    # Process input (events)
    for event in pygame.event.get():
        # check to close the window
        if event.type == pygame.QUIT:# event that starts after clicking the cross, passes False to the running variable
            running = False

    # Update
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player,coins,True)# Checking if the robot hit the coin if the True coin disappears
    #If just delete coins,they will run out. You need to loop through hits and create a new one for each missing coin.
    for hit in hits:
        score += 5 #if the event happened +5 points
        c = Coin()
        all_sprites.add(c)
        coins.add(c)

    hits = pygame.sprite.spritecollide(player, hirvios, False)# Checking if robot hit hirvio if True game over
    if hits:  
       running = False
       show_go_screen()# if hit with hirvi go to the beginning
    
    hits = pygame.sprite.spritecollide(player, mobs, True)# checking if the robot hit the mob if the True coin disappears
    #If just delete mob,they will run out. You need to loop through hits and create a new one for each missing mob.
    for hit in hits:
        score -= 10 #if the event happened -19 points
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        
    # Rendering (drawing)
    screen.fill(BLUE)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)# calling the functions for drawing the number of points
    # the screen on which we draw, score, font size, x and y position
    
    pygame.display.flip()# After drawing everything, flip the screen

pygame.quit()

