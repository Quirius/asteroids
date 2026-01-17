from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_SHOOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position.x, position.y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt