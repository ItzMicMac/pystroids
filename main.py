import pygame
from sys import exit
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    # Sprite groups for shared functionality
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Main Game loop
    while True:
        # Logging
        log_state()
        # Process Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Process Input
        updatable.update(dt)
        for roid in asteroids:
            if player.collides_with(roid):
                log_event("player_hit")
                print("Game over!")
                exit()
        for roid in asteroids:
            for shot in shots:
                if shot.collides_with(roid):
                    log_event("asteroid_shot")
                    shot.kill()
                    roid.split()

        screen.fill("black") # Resets screen
        # Player and object drawing starts here
        for item in drawable:
            item.draw(screen)

        # Player and object drawing ends here
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
