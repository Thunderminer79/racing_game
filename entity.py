import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        super().__init__()
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.hitboxes = False
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
    def render(self):
        from main import DISPLAYSERF, RED
        DISPLAYSERF.blit(self.sprite, self.rect)
        if self.hitboxes:
            pygame.draw.rect(DISPLAYSERF, RED, self.rect, 1)
    def collide(self, other):
        pass