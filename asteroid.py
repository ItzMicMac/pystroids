import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Adds the velocity vector based on delta time
        self.position += self.velocity * dt

    def split(self):
        self.kill() # Kill original asteroid
        # Break if the radius is less than the minimum
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = uniform(20, 50)
        roid1_vector = self.velocity.rotate(rand_angle)
        roid2_vector = self.velocity.rotate(-rand_angle)
        roid_radius = self.radius - ASTEROID_MIN_RADIUS
        roid1 = Asteroid(self.position.x, self.position.y, roid_radius)
        roid2 = Asteroid(self.position.x, self.position.y, roid_radius)
        roid1.velocity = roid1_vector * 1.2
        roid2.velocity = roid2_vector * 1.2
