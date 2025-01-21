# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.display.set_caption("Pygame2 Asteroid")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    main_player = Player(x, y)
    field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))

        for up in updatable:
            up.update(dt)
        
        for obj in asteroids:
            if obj.has_collided(main_player):
                print("Game over!")
                return
        
        for dr in drawable:
            dr.draw(screen)
        
        for ast in asteroids:
            for bullet in shots:
                if bullet.has_collided(ast):
                    bullet.kill()
                    ast.kill()
        
        pygame.display.flip()

        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()