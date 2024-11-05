import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #clock
    ticker = pygame.time.Clock()
    dt = 0
    
    #Group based on drawable and udpateable
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shot,drawable,updateable)
    
    #player
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for asteroid in asteroids:
            if(asteroid.collision(player)):
                print("Game over!")
                return
        for draw in drawable:
            draw.draw(screen)
        for update in updateable:
            update.update(dt)
        pygame.display.flip()
        dt = ticker.tick(60)/1000
        
        
if __name__ == '__main__':
    main()