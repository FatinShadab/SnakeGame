import sys
import random
import pygame


class Direction:
    RIGHT = pygame.math.Vector2(1, 0)
    LEFT = pygame.math.Vector2(-1, 0)
    UP = pygame.math.Vector2(0, -1)
    DOWN = pygame.math.Vector2(0, 1)


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
        self.defaultDirection = Direction.RIGHT
        self.w, self.h = self.bodyWH = cellWH
        self.direction = self.defaultDirection
        
        self.body = [
            pygame.math.Vector2(6, 9),
            pygame.math.Vector2(5, 9),
            pygame.math.Vector2(4, 9)
        ]
        
        self.head = self.body[0]
        
    def update(self):
        self.body.pop()
        self.body.insert(0, self.head + self.direction)
        self.head = self.body[0]
        
    def get_render_object(self):
        return [(block.x * self.w, block.y * self.h, *self.bodyWH) for block in self.body]
    
    def get_snake_head(self):
        return pygame.Rect(self.head.x * self.w, self.head.y * self.h, *self.bodyWH)

    def grow(self):
        self.body.append(self.body[-1] + self.direction)

class Game:
    AUTO_SNAKE_MOVEMENT = pygame.event.custom_type()
    AUTO_FOOD_GENERATION = pygame.event.custom_type()
    
    def __init__(self):
        pygame.init()
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
        pygame.display.set_caption("PySnake")
        
        self.snake = Snake((self.cellSize, self.cellSize))
        
        self.food = Food((self.cellSize + 10, self.cellSize + 10))
        self.foodPos = self.foodPos = self.food.get_random_render_pos(
            (50,  (self.cellCount - 2) * self.cellSize),
            (50,  (self.cellCount - 2) * self.cellSize)
        )
        
        self.recordedUserEvent = None
        
        pygame.time.set_timer(Game.AUTO_SNAKE_MOVEMENT, 200)
        pygame.time.set_timer(Game.AUTO_FOOD_GENERATION, 4000)

    def handle_food_snake_collision(self):
        if self.snake.get_snake_head().colliderect(self.foodPos):
            self.foodPos = self.foodPos = self.food.get_random_render_pos(
                (50,  (self.cellCount - 2) * self.cellSize),
                (50,  (self.cellCount - 2) * self.cellSize)
            )
            self.snake.grow()
        
        pass

    def render(self):
        self.window.fill(self.backgroundColor)
        
        self.window.blit(
            self.food.get_render_object(),
            self.foodPos
        )
        
        for idx, renderObj in enumerate(self.snake.get_render_object()):
            if idx == 0:
                pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 20)
            else:
                pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 16)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runFlag = False
                
            self.recordedUserEvent = event

    def update(self):
        if self.recordedUserEvent:
            if self.recordedUserEvent.type == Game.AUTO_SNAKE_MOVEMENT:
                self.snake.update()
            
            if self.recordedUserEvent.type == Game.AUTO_FOOD_GENERATION:
                self.foodPos = self.food.get_random_render_pos(
                    (50,  (self.cellCount - 2) * self.cellSize),
                    (50,  (self.cellCount - 2) * self.cellSize)
                )
                
            if self.recordedUserEvent.type == pygame.KEYDOWN:
                if self.recordedUserEvent.key == pygame.K_UP:
                    self.snake.direction = Direction.UP
                if self.recordedUserEvent.key == pygame.K_DOWN:
                    self.snake.direction = Direction.DOWN
                if self.recordedUserEvent.key == pygame.K_RIGHT:
                    self.snake.direction = Direction.RIGHT
                if self.recordedUserEvent.key == pygame.K_LEFT:
                    self.snake.direction = Direction.LEFT
            
            self.recordedUserEvent = None
            
        self.handle_food_snake_collision()

        pygame.display.flip()
        pygame.display.update()

    def cleanup(self):
        pygame.quit()
        sys.exit()

    def gameLoop(self):
        while self.runFlag:
            
            self.input()
            self.update()
            self.render()

            self.gameClock.tick(self.maxFPS)

    def run(self):
        self.gameLoop()


if __name__ == "__main__":
    Game().run()
