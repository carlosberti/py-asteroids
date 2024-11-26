import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
           return
            
       for obj in updatable: 
         obj.update(dt)
        
      
       for asteroid in asteroids:
         if asteroid.collides_with(player):
           print("Game over!")
           sys.exit()
            
       screen.fill("black")
       
       for obj in drawable:
         obj.draw(screen)

       pygame.display.flip()
       time_since_last_time = clock.tick(60)
       dt = time_since_last_time / 1000

if __name__ == "__main__":
    main()