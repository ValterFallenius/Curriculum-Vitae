import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 700
screen_height = 500

class ParentClass(pygame.sprite.Sprite):
    def __init__(self,  x_pos=0, y_pos=0, color=BLACK, size=25):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=pygame.Surface([size,size])
        self.image.fill(color)
        self.velocity=[0, 0, 0, 0]#[UP, DOWN, LEFT, RIGHT]
        self.rect = self.image.get_rect()

    # Moves the sprite (called every frame).
    def move(self):
        self.rect.x+=self.velocity[3]*self.speed - self.velocity[2]*self.speed
        self.rect.y+=self.velocity[1]*self.speed - self.velocity[0]*self.speed

    def stayInside(self):
        if self.rect.y<0:
            self.stop("UP")
        if self.rect.y>screen_height-self.size:
            self.stop("DOWN")
        if self.rect.x<0:
            self.stop("LEFT")
        if self.rect.x>screen_width-self.size:
            self.stop("RIGHT")

    def stop(self, direction):
        if direction=="UP":
            self.rect.y=0
        elif direction=="DOWN":
            self.rect.y=screen_height-self.size
        elif direction=="LEFT":
            self.rect.x=1
        elif direction=="RIGHT":
            self.rect.x=screen_width-self.size

        if self.blockType==2:
            self.accelerate()
        else:
            if direction=="UP":
                self.velocity[0]=0
            elif direction=="DOWN":
                self.velocity[1]=0
            elif direction=="LEFT":
                self.velocity[2]=0
            elif direction=="RIGHT":
                self.velocity[3]=0

#Player-class
class Player(ParentClass):
    def __init__(self,  x_pos=0, y_pos=0,color=BLACK, size=25):
        super(Player, self).__init__(x_pos, y_pos, color, size)
        pygame.draw.rect(self.image, WHITE, (0, 0, 25, 25), 4)
        self.score=0
        self.blockType=0
        self.speed=4



class Target(ParentClass):
    def __init__(self, x_pos=300, y_pos=300, color=GREEN, size=25):
        super(Target, self).__init__(x_pos, y_pos, color, size)
        self.blockType=1
    def regenerate(self, new_x, new_y):
        self.rect.x=new_x
        self.rect.y=new_y

class BounceBall(ParentClass):
    def __init__(self, x_pos=0, y_pos=0,color=RED, size=25):
        super(BounceBall, self).__init__(x_pos, y_pos, color, size)
        self.blockType=2
        randomindex=random.randrange(4)
        self.velocity[randomindex]=1
        self.speed=3
    #Makes the BounceBall-object bounce when this function is called.
    def accelerate(self):

        temp=self.velocity
        newVelocity=[temp[1], temp[0], temp[3], temp[2]]
        self.velocity=newVelocity


        '''
class movingBackgrounds(pygame.sprite.Sprite):
    def __init__(self, screensize_x, screensize_y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([screensize_x*2,screensize_y]*2)
        self.image.blit (image, (0, 0))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=-1*(screensize_x/2)
        self.rect.y=-1*(screensize_y/2)'''


def randomizeCoordinate(screen_width, screen_height):
    x_value=random.randrange(screen_width)
    y_value=random.randrange(screen_height)
    return [x_value, y_value]

def generateEnemy(screen_width, screen_height, objectGroup, allSpritesGroup):
    coords = randomizeCoordinate(screen_width, screen_height)
    bounceBall = BounceBall()
    bounceBall.rect.x=coords[0]
    bounceBall.rect.y=coords[1]
    objectGroup.add(bounceBall)
    allSpritesGroup.add(bounceBall)
    return (objectGroup, allSpritesGroup)

def regenerateNewTarget(targetreference, screen_width, screen_height):
    newTargetCoords=randomizeCoordinate(screen_width, screen_height)
    targetreference.regenerate(newTargetCoords[0], newTargetCoords[1])
