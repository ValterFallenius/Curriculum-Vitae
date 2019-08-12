def main():
    pass

import pygame
import Levels

# Initialize Pygame
pygame.init()

#This is the parentclass for all other classes.
class Blocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.block_type=0
        #Block types:
        # 1: Regular block, a square on which the player can rest
        # 2-5: Bounces the player in a 90 degree angle.
            # 2: Bounces the player in a 90 degree angle from left to up, or from up to left.
            # 3: Bounces the player in a 90 degree angle from up to right, or from right to up.
            # 4: Bounces the player in a 90 degree angle from right to down, or from down to right.
            # 5: Bounces the player in a 90 degree angle from down to left, or from left to down.
        # 6: Goal-block
        # 7: Player-block

# Block-type 1
class Square_Block (Blocks):
    def __init__(self):
        super().__init__()
        self.image.fill (GREY)
        pygame.draw.rect(self.image, DARKGREY, (2, 2, 21, 21))
        # Acceleration which will decide how the block accelerates:
        # acceleration = [accelerationconstant, accepted_x_direction, accepted_y_direction]
        # If accepted x/y direction is 0, all directions are acceptable.
        self.acceleration=[0, 0, 0]
        self.block_type=1

# Block-type 2-5:
class Bounce_Block(Blocks):
    def __init__(self, block_type):
        super().__init__()
        self.block_type=block_type
        # The acceleration is more complex on these triangular blocks; if the
        # player comes from a certain direction the player should bounce in
        # a 90 degree angle, otherwise it shouldn't bounce.
        # We solve this by defining the acceleration with a list of: the accelerationconstant,
        # one accepted x-direction and one accepted y-direction:
        # acceleration = [accelerationconstant, accepted_x_direction, accepted_y_direction]
        if self.block_type==2:
            # Block type 2 should accept x-direction +1 and y-direction +1:
            self.acceleration=[-1, 1, 1]
            self.image.blit (leftup_img, (0, 0))
        elif self.block_type==3:
            self.acceleration=[1, -1, 1]
            self.image.blit (upright_img, (0, 0))
        elif self.block_type==4:
            self.acceleration=[-1, -1, -1]
            self.image.blit (rightdown_img, (0, 0))
        elif self.block_type==5:
            self.acceleration=[1, 1, -1]
            self.image.blit (downleft_img, (0, 0))

# Block-type 6:
class Goal(Blocks):
    def __init__(self):
        super().__init__()
        self.image.blit(goal_img, (0,0))
        self.acceleration=[0, 0, 0]
        self.block_type=6

#Spriteclass which inherits all atributes of the parentclass "Blocks", but instead the  player-class have a method for moving and colliding with other blocks
class Player(Blocks):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.blit(player_img, (0,0))

        #Velosity: [x, y]
        self.velocity = [0, 0]
    def move(self, speed):
        self.rect.x+=self.velocity[0]*speed
        self.rect.y+=self.velocity[1]*speed

    # This method controls how the player will accelerate when it collides with another object.
    def accelerate(self, acceleration):
        v = self.velocity
        u= []
        # Checks if the player has an accepted direction.
        if v[0] == acceleration[1] or v[1] == acceleration[2]:
            u.append(int(v[1]*acceleration[0]))
            u.append(int(v[0]*acceleration[0]))
        else:
            u=[0,0]
        self.velocity=u
    #Makes sure the player isn't inside the other sprite:
def correct_placement(player_reference, block_reference):
    if block_reference.block_type==1:
        if player_reference.velocity[0]>0: player_reference.rect.right = block_reference.rect.left
        elif player_reference.velocity[0]<0: player_reference.rect.left = block_reference.rect.right
        elif player_reference.velocity[1]>0: player_reference.rect.bottom = block_reference.rect.top
        elif player_reference.velocity[1]<0: player_reference.rect.top = block_reference.rect.bottom
    elif block_reference.block_type == 2:
        if player_reference.velocity[0]>0:
            # Following 2 rows of code moves the player from left side of the sprite to the top side:
            player_reference.rect.x=block_reference.rect.x
            player_reference.rect.bottom = block_reference.rect.top
        elif player_reference.velocity[0]<0: player_reference.rect.left = block_reference.rect.right
        elif player_reference.velocity[1]>0:
            # Following 2 rows of code moves the player from top side of the sprite to the left side:
            player_reference.rect.y=block_reference.rect.y
            player_reference.rect.right = block_reference.rect.left
        elif player_reference.velocity[1]<0: player_reference.rect.top = block_reference.rect.bottom
    elif block_reference.block_type==3:
        if player_reference.velocity[0]>0: player_reference.rect.right = block_reference.rect.left
        elif player_reference.velocity[0]<0:
            player_reference.rect.x=block_reference.rect.x
            player_reference.rect.bottom = block_reference.rect.top
        elif player_reference.velocity[1]>0:
            player_reference.rect.y=block_reference.rect.y
            player_reference.rect.left = block_reference.rect.right
        elif player_reference.velocity[1]<0: player_reference.rect.top = block_reference.rect.bottom
    elif block_reference.block_type==4:
        if player_reference.velocity[0]>0: player_reference.rect.right = block_reference.rect.left
        elif player_reference.velocity[0]<0:
            player_reference.rect.x=block_reference.rect.x
            player_reference.rect.top = block_reference.rect.bottom
        elif player_reference.velocity[1]>0: player_reference.rect.bottom = block_reference.rect.top
        elif player_reference.velocity[1]<0:
            player_reference.rect.y=block_reference.rect.y
            player_reference.rect.left = block_reference.rect.right
    elif block_reference.block_type==5:
        if player_reference.velocity[0]>0:
            player_reference.rect.x=block_reference.rect.x
            player_reference.rect.top = block_reference.rect.bottom
        elif player_reference.velocity[0]<0: player_reference.rect.left = block_reference.rect.right
        elif player_reference.velocity[1]>0: player_reference.rect.bottom = block_reference.rect.top
        elif player_reference.velocity[1]<0:
            player_reference.rect.y=block_reference.rect.y
            player_reference.rect.right = block_reference.rect.left
    elif block_reference.block_type==6:
        level_clear=True
        return level_clear
    return player

def background_movement(x_change, y_change):
    new_speed=[]
    if x_change>25:new_speed.append(-1)
    elif x_change<-25:new_speed.append(1)






# Some RGB-colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (160, 0, 0)
DARKGREY = (48, 48, 48)
GREY = (108, 108, 108)
DARKBLUE = (0, 0, 100)


# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of sprites.
block_list = pygame.sprite.Group()

# This is a list of every sprite.
all_sprites_list = pygame.sprite.Group()


# --------------------- Pictures goes here ---------------------------#

background_img = pygame.image.load ("Bakgrund.jpg").convert()

background_img2 = pygame.image.load("JOJO.png").convert()
background_img2.set_colorkey(BLACK)

background_img3 = pygame.image.load("JOJOflippedflipped.png").convert()
background_img3.set_colorkey(BLACK)

background_img4 = pygame.image.load("JOJOflipped.png").convert()
background_img4.set_colorkey(BLACK)

leftup_img = pygame.image.load ("LEFTUP.jpg").convert()
leftup_img.set_colorkey(WHITE)

upright_img = pygame.image.load ("UPRIGHT.jpg").convert()
upright_img.set_colorkey(WHITE)

rightdown_img = pygame.image.load ("RIGHTDOWN.jpg").convert()
rightdown_img.set_colorkey(WHITE)

downleft_img = pygame.image.load ("DOWNLEFT.jpg").convert()
downleft_img.set_colorkey(WHITE)
downleft_img.set_colorkey(BLACK)

goal_img = pygame.image.load ("Goal_img.png").convert()

player_img = pygame.image.load ("Player_img.jpg").convert()
player_img.set_colorkey(BLACK)

# --------------------- Pictures goes here ---------------------------#

pygame.display.set_caption("Orbitz")

# Loop until the user clicks the close button.
done = False
goal_coord=[0,0]
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#This function loads the level and all objekcts from the 28x20 list in "LEVELS".
def load_level(level, player_reference):
    for y in range (20):
        for x in range (28):
            if level[y][x]==0: continue
            elif level[y][x]==1:
                square_block = Square_Block()
                square_block.rect.y=y*25
                square_block.rect.x=x*25
                block_list.add(square_block)
                all_sprites_list.add(square_block)
            elif level[y][x]>=2 and level[y][x]<=5:
                bounce_block = Bounce_Block(level[y][x])
                bounce_block.rect.y=y*25
                bounce_block.rect.x=x*25
                block_list.add(bounce_block)
                all_sprites_list.add(bounce_block)
            elif level[y][x]==6:
                goal = Goal()
                goal.rect.y=y*25
                goal.rect.x=x*25
                block_list.add(goal)
                all_sprites_list.add(goal)
            elif level[y][x]==7:
                player_reference.rect.y=y*25
                player_reference.rect.x=x*25
                all_sprites_list.add(player_reference)


speed=8
speed2=0.2
player=Player()

levelcount=0


# Two lists for making the dots on the screen move differentely, one for [[x_add,y_add], [x_add, y_add], [x_add, y_add]]  and one for [[change_x, change_y], [change_x, change_y], [change_x, change_y]].
# (A total of 3 images that need moving)
location_term_list=[[0, 0], [0, 0], [0, 0]]
change_term_list=[[0.6*speed2, 0.8*speed2], [0.4*speed2, 1.0*speed2], [1.0*speed2, 0.4*speed2]]

print("Your mission is to get the orb to the goal by bouncing off the MEGA-SPACE-BLOCKZ. ")
# -------- Main Program Loop -----------
for LEVEL in Levels.LEVELS:
    if done==True: break
    levelcount+=1
    player_movement=[0,0]
    print ("Level:", levelcount)
    level_clear=False
    load_level(LEVEL, player)
    player_start_position=[player.rect.x,player.rect.y]
    while not done and not level_clear:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and player.velocity == [0,0]:
                if event.key == pygame.K_UP: player.velocity[1]=-1
                elif event.key == pygame.K_DOWN: player.velocity[1]=1
                elif event.key == pygame.K_LEFT: player.velocity[0]=-1
                elif event.key == pygame.K_RIGHT: player.velocity[0]=1

        # --- Game logic should go here
        # Checks if the player is outside the screen:
        if player.rect.x<0 or player.rect.x>700:
            print ("Please dont stray outside the universe...")
            player.velocity=[0,0]
            player.rect.x=player_start_position[0]
            player.rect.y=player_start_position[1]
        elif player.rect.y<0 or player.rect.y>500:
            print ("Please dont stray outside the universe...")
            player.velocity=[0,0]
            player.rect.x=player_start_position[0]
            player.rect.y=player_start_position[1]
        # Moves the player according with it's velocity every frame:
        player.move(speed)

        # Moves the background on the opposite direction of the player:
        if player.velocity!=[0,0]:
            player_movement[0]-=player.velocity[0]*0.3
            player_movement[1]-=player.velocity[1]*0.3

        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
        for block in blocks_hit_list:

            correct_placement(player, block)
            player.accelerate(block.acceleration)
            if block.block_type == 6:
                print ("Good job!")
                level_clear=True
                break


        for i in range(3):
            # Makes the background images move.
            location_term_list[i][0] += change_term_list[i][0]
            location_term_list[i][1] += change_term_list[i][1]
            # Makes the images bounce within a 50x50 square.
            if location_term_list[i][0]<-25:change_term_list[i][0]*=-1
            elif location_term_list[i][0]>25:change_term_list[i][0]*=-1
            if location_term_list[i][1]<-25:change_term_list[i][1]*=-1
            elif location_term_list[i][1]>25:change_term_list[i][1]*=-1

        # --- Screen-clearing code goes here
        # --- Drawing code should go here
        screen.blit (background_img, (0, 0))
        screen.blit (background_img2, (-50 + location_term_list[0][0] + player_movement[0]*0.8, -50 + location_term_list[0][1] + player_movement[1]*0.8))
        screen.blit (background_img3, (-50 + location_term_list[1][0] + player_movement[0], -50 + location_term_list[1][1] + player_movement[1]))
        screen.blit (background_img4, (-50 + location_term_list[2][0] + player_movement[0]*0.6, -50 + location_term_list[2][1] + player_movement[1]*0.6))
        # Draw all the spites
        all_sprites_list.draw(screen)



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    for sprite in all_sprites_list:
        pygame.sprite.Sprite.kill(sprite)

print("GG EZ(...............= Good Game Easy)")

# Close the window and quit.
pygame.quit()
if __name__ == '__main__':
    main()
