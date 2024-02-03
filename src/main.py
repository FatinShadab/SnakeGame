import sys
import time
import random
import pygame


class Food:
    def __init__(self, scaledWH = None):
        self.image = pygame.image.load("resources/egg.png").convert_alpha()
        
        if scaledWH:
            self.image = pygame.transform.scale(
                self.image, 
                scaledWH
            )
        
    def get_render_object(self):
        return self.image
    
    def get_random_render_pos(self, xRange, yRange):
        x = random.randint(*xRange)
        y = random.randint(*yRange)
        return self.image.get_rect(topleft=(x, y))


class Snake:
    COLOR = (40, 55, 20)
    
    def __init__(self, cellWH):
        self.w, self.h = self.bodyWH = cellWH
        
        self.body = [
            pygame.math.Vector2(6, 9),
            pygame.math.Vector2(5, 9),
            pygame.math.Vector2(4, 9)
        ]
        
        self.head = self.body[0]

    def get_render_object(self):
        return [(block.x * self.w, block.y * self.h, *self.bodyWH) for block in self.body]


class Game:
    def __init__(self):
        self.cellCount = 20
        self.cellSize = 50
        self.windowWH = (
            self.cellCount * self.cellSize,
            self.cellCount * self.cellSize
        )
        self.width, self.height = self.windowWH
        self.runFlag = True
        self.window = pygame.display.set_mode(self.windowWH)
        self.gameClock = pygame.time.Clock()
        self.maxFPS = 60
        self.backgroundColor = (173, 204, 96)
        self.window.fill(self.backgroundColor)
        pygame.display.set_caption("PySnake") 
        
        
        self.snake = Snake((self.cellSize, self.cellSize))
        
        food = Food((self.cellSize + 20, self.cellSize + 20))
        self.window.blit(
            food.get_render_object(),
            food.get_random_render_pos(
                (0,  (self.cellCount - 1) * self.cellSize),
                (0,  (self.cellCount - 1) * self.cellSize)
                )
            )  

    def render(self):
        for renderObj in self.snake.get_render_object():
            pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 8)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runFlag = False

    def update(self, deltaTime):
        pygame.display.update()

    def cleanup(self):
        pygame.quit()
        sys.exit()

    def gameLoop(self):
        lastTime = time.time()
        
        while self.runFlag:
            deltaTime = time.time() - lastTime
            lastTime = time.time()

            self.input()
            self.update(deltaTime)
            self.render()

            self.gameClock.tick(self.maxFPS)

    def run(self):
        self.gameLoop()


if __name__ == "__main__":
    Game().run()
