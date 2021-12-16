import pygame
import States.PlayState
import States.ScoreState
import States.StartState
import StateMachine

FPS = 30
clock = pygame.time.Clock()

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

GROUND_SCROLL_SPEED = 15
BACKGROUND_SCROLL_SPEED = 3
LOOPING_POINT = 1280

WHITE = (255, 255, 255)

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

DISPLAYSERF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

states = {"Start": States.StartState.StartState(), "Play": States.PlayState.PlayState(), "Score": States.ScoreState.ScoreState()}
gStateMachine = StateMachine.StateMachine(states)