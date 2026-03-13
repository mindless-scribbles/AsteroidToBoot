import pygame
import logger
import random
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return None
        else:
            logger.log_event("asteroid_split")
            random_angle = random.randrange(20, 50)
            asteroid_vector_one = self.velocity.rotate(random_angle)
            asteroid_vector_two = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_one.velocity = asteroid_vector_one * 1.2
            asteroid_two.velocity = asteroid_vector_two
