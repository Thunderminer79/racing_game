import States.BaseState
import pygame
from pygame.locals import *

class ScoreState(States.BaseState.BaseState):
    def __init__(self):
        pass
    def enter(self, params):
        self.score = params
    def update(self):
        from main import GREEN, BLUE, DISPLAYSERF, WHITE, WINDOW_HEIGHT, WINDOW_WIDTH
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render('You Crashed', True, WHITE)
        text1 = font.render(f"Score: {self.score}", True, WHITE)
        textRect = text.get_rect()
        text1Rect = text1.get_rect()
        textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 150)
        text1Rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 70)
        DISPLAYSERF.blit(text, textRect)
        DISPLAYSERF.blit(text1, text1Rect)

        pressed_keys = pygame.key.get_pressed()

        from main import gStateMachine
        if pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER]:
            gStateMachine.change("Play", None)

    def render(self):
        pass