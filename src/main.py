import sys
import random
from typing import Optional, List, Tuple
import pygame


class Direction:
    """
    Used for representing different directions.
    """
    RIGHT: pygame.math.Vector2 = pygame.math.Vector2(1, 0)
    LEFT: pygame.math.Vector2 = pygame.math.Vector2(-1, 0)
    UP: pygame.math.Vector2 = pygame.math.Vector2(0, -1)
    DOWN: pygame.math.Vector2 = pygame.math.Vector2(0, 1)


class Food:
    """
    Represents the food object in the game.
    """
    def __init__(self, scaledWH: Optional[Tuple[int, int]] = None) -> None:
        """
        Initialize the Food object.

        Parameters:
            scaledWH (tuple): Tuple specifying the scaled width and height of the food image.
        """
        self.image: pygame.Surface = pygame.image.load("resources/egg.png").convert_alpha()

        if scaledWH:
            self.image = pygame.transform.scale(
                self.image,
                scaledWH
            )

    def get_render_object(self) -> pygame.Surface:
        """
        Get the render object (image) of the food.

        Returns:
            pygame.Surface: The rendered image of the food.
        """
        return self.image

    def get_random_render_pos(self, xRange: Tuple[int, int], yRange: Tuple[int, int]) -> pygame.Rect:
        """
        Get a random position for rendering the food.

        Parameters:
            xRange (tuple): Tuple specifying the range of x-coordinate for the random position.
            yRange (tuple): Tuple specifying the range of y-coordinate for the random position.

        Returns:
            pygame.Rect: Rectangle representing the random position for rendering the food.
        """
        x: int = random.randint(*xRange)
        y: int = random.randint(*yRange)

        return self.image.get_rect(topleft=(x, y))


class Snake:
    """
    Represents the snake object in the game.
    """
    COLOR: Tuple[int, int, int] = (40, 55, 20)

    def __init__(self, cellWH: Tuple[int, int]) -> None:
        """
        Initialize the Snake object.

        Parameters:
            cellWH (tuple): Tuple specifying the width and height of each cell in the snake.
        """
        self.defaultDirection: pygame.math.Vector2 = Direction.RIGHT
        self.w, self.h = self.bodyWH = cellWH
        self.direction: pygame.math.Vector2 = self.defaultDirection

        # Initial body parts of the snake
        self.body: List[pygame.math.Vector2] = [
            pygame.math.Vector2(6, 9),
            pygame.math.Vector2(5, 9),
            pygame.math.Vector2(4, 9)
        ]

        self.head: pygame.math.Vector2 = self.body[0]

    def update(self) -> None:
        """
        Update the position of the snake based on its direction.
        """
        self.body.pop()
        self.body.insert(0, self.head + self.direction)
        self.head = self.body[0]

    def get_render_object(self) -> List[Tuple[int, int, int, int]]:
        """
        Get the render objects (rectangles) for each body part of the snake.

        Returns:
            list: List of tuples, where each tuple represents the (x, y, width, height) of a body part.
        """
        return [(block.x * self.w, block.y * self.h, *self.bodyWH) for block in self.body]

    def get_snake_head(self) -> pygame.Rect:
        """
        Get the rectangle representing the head of the snake.

        Returns:
            pygame.Rect: Rectangle representing the head of the snake.
        """
        return pygame.Rect(self.head.x * self.w, self.head.y * self.h, *self.bodyWH)

    def grow(self) -> None:
        """
        Increase the length of the snake by adding a body part.
        """
        self.body.append(self.body[-1] + self.direction)

    def reset(self) -> None:
        """
        Reset the snake to its default state.
        """
        self.direction = self.defaultDirection

        # Initial body parts of the snake
        self.body = [
            pygame.math.Vector2(6, 9),
            pygame.math.Vector2(5, 9),
            pygame.math.Vector2(4, 9)
        ]

        self.head = self.body[0]


class Game:
    """
    Represents the main game class.
    """
    Menu: int = 0
    Play: int = 2
    Pause: int = 3

    AUTO_SNAKE_MOVEMENT: int = pygame.event.custom_type()
    AUTO_HISS_SOUND: int = pygame.event.custom_type()

    def __init__(self) -> None:
        """
        Initialize the Game object.
        """
        pygame.init()

        # Game state and properties
        self.state: int = Game.Menu
        self.scoreValue: int = 0
        self.highScoreValue: int = 0
        self.cellCount: int = 16
        self.cellSize: int = 50
        self.windowWH: Tuple[int, int] = (
            self.cellCount * self.cellSize,
            self.cellCount * self.cellSize
        )
        self.width, self.height = self.windowWH
        self.runFlag: bool = True
        self.window: pygame.Surface = pygame.display.set_mode(self.windowWH)
        self.gameClock: pygame.time.Clock = pygame.time.Clock()
        self.font: pygame.font.Font = pygame.font.Font("resources/Pixeltype.ttf", 50)
        self.font.bold: bool = True
        self.maxFPS: int = 60
        self.backgroundColor: Tuple[int, int, int] = (173, 204, 96)
        pygame.display.set_caption("PySnake")

        # Snake and Food objects
        self.snake: Snake = Snake((self.cellSize + 10, self.cellSize + 10))
        self.food: Food = Food((2 * self.cellSize, 2 * self.cellSize))
        self.foodPos: Optional[pygame.Rect] = None

        # Play area rectangle
        self.playArea: pygame.Rect = pygame.Rect(5, 40, self.width - 10, self.height - 45)

        # Timer events for automatic snake movement and hiss sound
        pygame.time.set_timer(Game.AUTO_SNAKE_MOVEMENT, 200)
        pygame.time.set_timer(Game.AUTO_HISS_SOUND, 5000)

        # Configure audio
        self.config_audio()

    def config_audio(self) -> None:
        """
        Load and configure game sounds.
        """
        self.eatSE: pygame.mixer.Sound = pygame.mixer.Sound("resources/hiss3-103123.mp3")
        self.hitSE: pygame.mixer.Sound = pygame.mixer.Sound("resources/loss.mp3")
        self.hissSE: pygame.mixer.Sound = pygame.mixer.Sound("resources/hiss.mp3")

        # Set volume for each sound
        self.eatSE.set_volume(0.5)
        self.hitSE.set_volume(0.5)
        self.hissSE.set_volume(0.5)

    def update_high_sore(self) -> None:
        """
        Update the high score based on the current score.
        """
        self.highScoreValue: int = max(self.highScoreValue, self.scoreValue)

    def handle_food_snake_collision(self) -> None:
        """
        Handle collisions between snake and food, update score, and play sound.
        """
        food_solid_area: pygame.Rect = self.foodPos.copy()
        food_solid_area.width = 40
        food_solid_area.height = 40
        food_solid_area.x += 35
        food_solid_area.y += 25

        if self.snake.get_snake_head().colliderect(food_solid_area):
            # Generate new food position
            self.foodPos: Optional[pygame.Rect] = self.food.get_random_render_pos(
                (50, (self.cellCount - 2) * self.cellSize),
                (50, (self.cellCount - 2) * self.cellSize)
            )
            # Grow the snake, update score, and play eat sound
            self.snake.grow()
            self.scoreValue += 1
            self.eatSE.play()

    def termination_event_ocurred(self) -> bool:
        """
        Check for game termination conditions.

        Returns:
            bool: True if the termination conditions are met, False otherwise.
        """
        snakeHead: pygame.Rect = self.snake.get_snake_head()
        for bodyPart in self.snake.get_render_object()[1:]:
            if snakeHead.contains(bodyPart):
                return True
        return not self.playArea.contains(snakeHead)

    def render_menu(self) -> None:
        """
        Render the menu screen.
        """
        pygame.draw.circle(self.window, "Black", (self.width // 2, self.height // 2), self.width // 2.4)
        pygame.draw.circle(self.window, (30, 60, 30), (self.width // 2, self.height // 2), self.width // 2.5)

        if self.termination_event_ocurred():
            # If game over, display score and high score
            self.window.blit(self.font.render(f"Score : {self.scoreValue}", False, (6, 2, 26)),
                             ((self.width // 4) + 120, self.height // 2.6))
            self.window.blit(self.font.render(f"High Score : {self.highScoreValue}", False, (6, 2, 26)),
                             ((self.width // 4) + 100, self.height // 2.2))
            self.window.blit(self.font.render(f"Press Enter To Play !", False, (6, 2, 26)),
                             ((self.width // 4) + 50, self.height // 1.8))
        else:
            # If not game over, display instructions
            self.window.blit(self.font.render(f"Use Arrow keys to Move !", False, (6, 2, 26)),
                             ((self.width // 5) + 70, self.height // 2.6))
            self.window.blit(self.font.render(f"Space key to Pause !", False, (6, 2, 26)),
                             ((self.width // 4) + 60, self.height // 2.2))
            self.window.blit(self.font.render(f"Press Enter To Play !", False, (6, 2, 26)),
                             ((self.width // 4) + 55, self.height // 1.8))

    def render(self) -> None:
        """
        Render the game.
        """
        self.window.fill(self.backgroundColor)

        # Draw play area rectangle
        pygame.draw.rect(self.window, (6, 2, 26), self.playArea, 15)

        # Display scores
        self.window.blit(self.font.render(f"Score {self.scoreValue}", False, (6, 2, 26)), (10, 5))
        self.window.blit(self.font.render(f"High Score : {self.highScoreValue}", False, (6, 2, 26)),
                         ((self.width - 400) + 100, 5))

        if self.foodPos:
            # Display food at its position
            self.window.blit(
                self.food.get_render_object(),
                self.foodPos
            )

        for idx, renderObj in enumerate(self.snake.get_render_object()):
            if idx == 0:
                # Draw head of the snake with larger border
                pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 26)
            else:
                # Draw body parts of the snake with smaller border
                pygame.draw.rect(self.window, Snake.COLOR, renderObj, 0, 16)

        if self.state == Game.Menu:
            # Render menu screen if the game is in menu state
            self.render_menu()

        if self.state == Game.Pause:
            # Draw pause indicator if the game is in pause state
            pygame.draw.rect(self.window, Snake.COLOR, pygame.Rect(200, 5, 10, 20))
            pygame.draw.rect(self.window, Snake.COLOR, pygame.Rect(215, 5, 10, 20))

    def input(self) -> None:
        """
        Handle user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runFlag = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.state == Game.Menu:
                    # Start the game when Enter is pressed in the menu state
                    self.scoreValue = 0
                    self.snake.reset()
                    self.foodPos: Optional[pygame.Rect] = self.food.get_random_render_pos(
                        (50, (self.cellCount - 2) * self.cellSize),
                        (50, (self.cellCount - 2) * self.cellSize)
                    )
                    self.state = Game.Play

                if event.key == pygame.K_SPACE:
                    # Toggle pause state with Space key
                    if self.state == Game.Play:
                        self.state = Game.Pause
                    elif self.state == Game.Pause:
                        self.state = Game.Play
                elif event.key == pygame.K_UP:
                    # Change snake direction based on arrow keys
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = Direction.RIGHT
                elif event.key == pygame.K_LEFT:
                    self.snake.direction = Direction.LEFT

            elif event.type == Game.AUTO_SNAKE_MOVEMENT:
                # Automatically update snake position at regular intervals
                if self.state == Game.Play:
                    self.snake.update()

            elif event.type == Game.AUTO_HISS_SOUND:
                # Play hiss sound at regular intervals
                if self.state == Game.Play:
                    self.hissSE.play()

    def update(self) -> None:
        """
        Update the game state.
        """
        self.update_high_sore()
        self.handle_food_snake_collision()

        if self.termination_event_ocurred():
            # Play hit sound and reset to menu state if termination conditions are met
            self.hitSE.play()
            self.state = Game.Menu

    def cleanup(self) -> None:
        """
        Clean up resources and exit the game.
        """
        pygame.quit()
        sys.exit()

    def gameLoop(self) -> None:
        """
        Main game loop.
        """
        while self.runFlag:
            self.input()

            if self.state == Game.Play:
                self.update()

            self.render()

            pygame.display.flip()
            pygame.display.update()
            
            self.gameClock.tick(self.maxFPS)

    def run(self) -> None:
        """
        Start the game.
        """
        self.gameLoop()


if __name__ == "__main__":
    # Run the game when the script is executed
    Game().run()
