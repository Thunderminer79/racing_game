#import pygame

class BaseState():
    def enter(self, params):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def render(self):
        pass