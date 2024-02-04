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

    def reset(self):
        self.direction = self.defaultDirection
        
        self.body = [
            pygame.math.Vector2(6, 9),
            pygame.math.Vector2(5, 9),
            pygame.math.Vector2(4, 9)
        ]
        
        self.head = self.body[0]
        

class Game:
    Menu = 0
    Play = 2
    Pause = 3
    
    AUTO_SNAKE_MOVEMENT = pygame.event.custom_type()
    AUTO_HISS_SOUND = pygame.event.custom_type()
    
    def __init__(self):
        pygame.init()
        self.state = Game.Menu
        self.scoreValue = 0
        self.highScoreValue = 0
        self.cellCount = 16
        self.cellSize = 50
        self.windowWH = (
            self.cellCount * self.cellSize,
            self.cellCount * self.cellSize
        )
        self.width, self.height = self.windowWH
        self.runFlag = True
        self.window = pygame.display.set_mode(self.windowWH)
        self.gameClock = pygame.time.Clock()
        self.font = pygame.font.Font("resources/Pixeltype.ttf", 50)
        self.font.bold = True
        self.maxFPS = 60
        self.backgroundColor = (173, 204, 96)
        pygame.display.set_caption("PySnake")
        
        self.snake = Snake((self.cellSize + 10, self.cellSize + 10))
        
        self.food = Food((2*self.cellSize, 2*self.cellSize))
        self.foodPos = None
        
        self.playArea = pygame.Rect(5, 40, self.width - 10, self.height - 45)
        
        pygame.time.set_timer(Game.AUTO_SNAKE_MOVEMENT, 200)
        pygame.time.set_timer(Game.AUTO_HISS_SOUND, 5000)
        
        self.config_audio()
        
    def config_audio(self):
        self.eatSE = pygame.mixer.Sound("resources/hiss3-103123.mp3")
        self.hitSE = pygame.mixer.Sound("resources/loss.mp3")
        self.hissSE = pygame.mixer.Sound("resources/hiss.mp3")
        
        self.eatSE.set_volume(0.5)
        self.hitSE.set_volume(0.5)
        self.hissSE.set_volume(0.5)

    def update_high_sore(self):
        self.highScoreValue = max(self.highScoreValue, self.scoreValue)

    def handle_food_snake_collision(self):
        food_solid_area = self.foodPos.copy()
        food_solid_area.width = 40
        food_solid_area.height = 40
        food_solid_area.x += 35
        food_solid_area.y += 25

        #pygame.draw.rect(self.window, "Blue", food_solid_area)

        if self.snake.get_snake_head().colliderect(food_solid_area):
            self.foodPos = self.foodPos = self.food.get_random_render_pos(
                (50,  (self.cellCount - 2) * self.cellSize),
                (50,  (self.cellCount - 2) * self.cellSize)
            )
            self.snake.grow()
            self.scoreValue += 1
            self.eatSE.play()

    def termination_event_ocurred(self):
        snakeHead = self.snake.get_snake_head()
        for bodyPart in self.snake.get_render_object()[1:]:
            if snakeHead.contains(bodyPart):
                return True
        return not self.playArea.contains(snakeHead)

    def render_menu(self):
        pygame.draw.circle(self.window, "Black", (self.width/2, self.height/2), self.width / 2.4)
        pygame.draw.circle(self.window, (30, 60, 30), (self.width/2, self.height/2), self.width / 2.5)
        
        if self.termination_event_ocurred():
            self.window.blit(self.font.render(f"Score : {self.scoreValue}",False, (6, 2, 26)), ((self.width / 4) + 120, self.height / 2.6))
            self.window.blit(self.font.render(f"High Score : {self.highScoreValue}",False, (6, 2, 26)), ((self.width / 4) + 100, self.height / 2.2))
            self.window.blit(self.font.render(f"Press Enter To Play !", False, (6, 2, 26)), ((self.width / 4) + 50, self.height / 1.8))
        else:
            self.window.blit(self.font.render(f"Use Arrow keys to Move !", False, (6, 2, 26)), ((self.width / 5) + 70, self.height / 2.6))
            self.window.blit(self.font.render(f"Space key to Pause !", False, (6, 2, 26)), ((self.width / 4) + 60, self.height / 2.2))
            self.window.blit(self.font.render(f"Press Enter To Play !", False, (6, 2, 26)), ((self.width / 4) + 55, self.height / 1.8))        

    def render(self):
        self.window.fill(self.backgroundColor)
        
        pygame.draw.rect(self.window, (6, 2, 26), self.playArea, 15)
        
        self.window.blit(self.font.render(f"Score {self.scoreValue}", False, (6, 2, 26)), (10, 5))
        self.window.blit(self.font.render(f"High Score : {self.highScoreValue}",False, (6, 2, 26)), ((self.width - 400) + 100, 5))
        
        if self.foodPos:
            self.window.blit(
                self.food.get_render_object(),
                self.foodPos
            )
        
        for idx, renderObj in enumerate(self.snake.get_render_object()):
            if idx == 0:
                pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 26)
            else:
                pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 16)

        if self.state == Game.Menu:
            self.render_menu()
            
        if self.state == Game.Pause:
            pygame.draw.rect(self.window, Snake.COLOR, pygame.Rect(200, 5, 10, 20))
            pygame.draw.rect(self.window, Snake.COLOR, pygame.Rect(215, 5, 10, 20))

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runFlag = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.state == Game.Menu:
                    self.scoreValue = 0
                    self.snake.reset()
                    self.foodPos = self.food.get_random_render_pos(
                            (50,  (self.cellCount - 2) * self.cellSize),
                            (50,  (self.cellCount - 2) * self.cellSize)
                    )
                    self.state = Game.Play
                    
                if event.key == pygame.K_SPACE:
                    if self.state == Game.Play:
                        self.state = Game.Pause
                    elif self.state == Game.Pause:
                        self.state = Game.Play
                elif event.key == pygame.K_UP:
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = Direction.RIGHT
                elif event.key == pygame.K_LEFT:
                    self.snake.direction = Direction.LEFT
                    
            elif event.type == Game.AUTO_SNAKE_MOVEMENT:
                if self.state == Game.Play:
                    self.snake.update()
            
            elif event.type == Game.AUTO_HISS_SOUND:
                if self.state == Game.Play:
                    self.hissSE.play()
                    

    def update(self):
        self.update_high_sore()
        self.handle_food_snake_collision()
        
        if self.termination_event_ocurred():
            self.hitSE.play()
            self.state = Game.Menu

    def cleanup(self):
        pygame.quit()
        sys.exit()

    def gameLoop(self):
        while self.runFlag:
            
            self.input()
            
            if self.state == Game.Play:
                self.update()
            
            self.render()

            self.gameClock.tick(self.maxFPS)
            pygame.display.flip()
            pygame.display.update()

    def run(self):
        self.gameLoop()


if __name__ == "__main__":
    Game().run()
