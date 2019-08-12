import pygame
import classesEskiv

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Eskiv Interstellar")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background_img = pygame.image.load ("space-4.jpg").convert()

# This is a list of sprites.
objects = pygame.sprite.Group()

# This is a list of every sprite.
all_sprites_list = pygame.sprite.Group()

#Generates the player in the middle of the plane.
player = classesEskiv.Player(screen_width//2-12, screen_height//2-12)
all_sprites_list.add(player)

target=classesEskiv.Target()
objects.add(target)
all_sprites_list.add(target)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.velocity[0]=1
            elif event.key == pygame.K_DOWN:
                player.velocity[1]=1
            elif event.key == pygame.K_LEFT:
                player.velocity[2]=1
            elif event.key == pygame.K_RIGHT:
                player.velocity[3]=1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.velocity[0]=0
            elif event.key == pygame.K_DOWN:
                player.velocity[1]=0
            elif event.key == pygame.K_LEFT:
                player.velocity[2]=0
            elif event.key == pygame.K_RIGHT:
                player.velocity[3]=0

    # --- Game logic should go here

    # Makes sure no objects move outside the screen.
    for sprite in all_sprites_list:
        sprite.stayInside()

    # Moves the player
    player.move()

    #Moves all other objects
    for sprite in objects:
        if sprite.blockType==2:
            sprite.move()

    # --------------- This section checks if the player has collided with anything and decides what to do: ----------------------- #

    sprites_hit_list = pygame.sprite.spritecollide(player, objects, False)

    for sprite in sprites_hit_list:
        if sprite.blockType == 1:
            player.score+=1
            print("Your current score is: " + str(player.score))

            #moves the target to a different position:
            newTargetCoords=classesEskiv.regenerateNewTarget(sprite, screen_width, screen_height)

            #Generates a new bounceball enemy-object
            temp=classesEskiv.generateEnemy(screen_width, screen_height, objects, all_sprites_list)
            #Refreshes the content of the sprite groups.
            objects=temp[0]
            all_sprites_list=temp[1]
        # Checks if the player hit an enemy bounceball.
        elif sprite.blockType == 2:

            done = True
            print("You got " + str(player.score) + " points.")
            break

    # --------------- This section checks if the player has collided with anything and decides what to do: ----------------------- #

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    screen.blit (background_img, (0, 0))
    # Draw all the spites
    all_sprites_list.draw(screen)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
