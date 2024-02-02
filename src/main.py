import sys
import time
import pygame


class Game:
    def __init__(self):
        self.runFlag = True
        self.window = pygame.display.set_mode((1280, 720))
        self.gameClock = pygame.time.Clock()
        self.maxFPS = 60
        self.backgroundColor = (173, 204, 96)
        self.window.fill(self.backgroundColor)
        pygame.display.set_caption("PySnake")   

    def render(self):    
        pygame.display.update()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runFlag = False

    def update(self, deltaTime):
        pass

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
