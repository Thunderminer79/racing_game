import States.BaseState
import pygame
from enemy import Enemy
import random

class PlayState(States.BaseState.BaseState):
    def enter(self, params):
        from main import player
        self.enemyList = []
        self.updateTimer = 0
        self.spawnSpeed = 90
        self.score = 0
        player.x, player.y = 600, 600

    def update(self):
        self.updateTimer += 1
        if self.updateTimer % 5 == 0 and self.spawnSpeed > 60:
            self.spawnSpeed -= 1
        
        if self.updateTimer % self.spawnSpeed == 0:
            randomType = random.randint(1, 4)
            if randomType == 1 or randomType == 2:
                enemyType = 1
            elif randomType == 3:
                enemyType = 2
            elif randomType == 4:
                enemyType = 3

            from main import Background, WINDOW_HEIGHT, WINDOW_WIDTH
            if enemyType != 2:
                enemyY = random.randint(Background.rect.height, WINDOW_HEIGHT - 90)
            else:
                enemyY = random.randint(Background.rect.height + 90, WINDOW_HEIGHT - 180)

            self.enemyList.append(Enemy(WINDOW_WIDTH, enemyY, "enemy.png", random.randint(10, 20), enemyType))
        
        from main import gStateMachine, collidCheck, player
        for enemy in self.enemyList:
            enemy.update()
            if collidCheck(player, enemy):
                gStateMachine.change("Score", self.score)
            if enemy.x < -enemy.width:
                self.enemyList.remove(enemy)
                self.score += 1

        from main import player
        player.update()

    def render(self):
        from main import player

        for enemy in self.enemyList:
            enemy.render()

        player.render()
        
        from main import WHITE, DISPLAYSERF
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(f"Score: {self.score}", True, WHITE)
        textRect = text.get_rect()
        textRect.center = (50, 15)
        DISPLAYSERF.blit(text, textRect)

    