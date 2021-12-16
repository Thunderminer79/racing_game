import pygame
import sys
import States.PlayState
import States.ScoreState
import States.StartState
import StateMachine
import car
from pygame.locals import *

#initalize pygame
pygame.init()

player = car.Car(600, 600, "car1.png")

FPS = 30
clock = pygame.time.Clock()

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

GROUND_SCROLL_SPEED = 15
BACKGROUND_SCROLL_SPEED = 3
LOOPING_POINT = 1280

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

Road = pygame.sprite.Sprite()
Road.image = pygame.image.load("road.png")
Road.rect = Road.image.get_rect()
Road.rect.topleft = (0, 0)

Background = pygame.sprite.Sprite()
Background.image = pygame.image.load("background.png")
Background.rect = Background.image.get_rect()
Background.rect.topleft = (0, 0)

groundScroll = 0
backgroundScroll = 0

#Setup a 300x300 Pixel Display
DISPLAYSERF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAYSERF.fill(WHITE)
pygame.display.set_caption("Racing Game")

# Music
mixer = pygame.mixer

mixer.init()
mixer.music.load("gameMusic.ogg")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

#statemachine
states = {"Start": States.StartState.StartState(), "Play": States.PlayState.PlayState(), "Score": States.ScoreState.ScoreState()}
gStateMachine = StateMachine.StateMachine(states)
gStateMachine.change("Start", None)

def collidCheck(entity1, entity2):
    if not (entity1.x > entity2.x + entity2.width) and not (entity1.x + entity1.width < entity2.x) and not (entity1.y > entity2.y + entity2.height) and not (entity1.y + entity1.height < entity2.y):
        return True
    else:
        return False 

def update():
    global groundScroll
    global backgroundScroll
    gStateMachine.update()
    groundScroll = (groundScroll - GROUND_SCROLL_SPEED) % LOOPING_POINT
    Road.rect.topleft = (groundScroll - WINDOW_WIDTH, WINDOW_HEIGHT - Road.rect.height)

    backgroundScroll = (backgroundScroll - BACKGROUND_SCROLL_SPEED) % LOOPING_POINT
    Background.rect.topleft = (backgroundScroll - WINDOW_WIDTH, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def render():
    pygame.display.update()
    DISPLAYSERF.fill(WHITE)
    
    DISPLAYSERF.blit(Road.image, Road.rect)
    DISPLAYSERF.blit(Background.image, Background.rect)

    gStateMachine.render()


#game loop
while True:
    update()
    render()

    clock.tick(FPS)