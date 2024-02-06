# PygameBasics
---
তোমরা এখানে! আরে আরে কোথায় যাও! এসে যখন পড়েছো, Game development এবং Pygame সম্পর্কে কিছু শিখে যাও। 

#### # Pygame আবার কোন গেম? (◔_◔)
---
ধুরো! Pygame কোনো game না। ইহা Python এর একটি library যা দিয়ে আমরা গেম বানাতে পারি। আমি ধরে নিচ্ছি যে তোমরা সবাই Python এবং Python এর basic জানো। আমরা আজকে python এবং programming এর basic নিয়ে তেমন কিছু আলোচনা করবো না। 

শিখার যাত্রাটা Pygame install করার মাধ্যমে শুরু করলে খারাপ হয় না। Pygame install এর জন্য আমাদের কম্পিউটারে Python থাকতে হবে। যদি Python না থাকে তাহলে [python.org](https://www.python.org/downloads) থেকে stable version ডাউনলোড করে নিতে পারো। 

এখন আমরা Pygame install করার জন্য প্রস্তুত । যদি তুমি এখন Windows কম্পিউটার ব্যবহার করে থাকো তাহলে তুমি CMD(Command prompt) এ গিয়ে নিচের লাইনটা execute করো। 
```
pip install pygame
```
যদি Windows না হয়ে Linux, Mac ব্যবহার করে থাকো তাহলে এইটা Terminal এ execute করো।
```
pip3 install pygame
```

Pygame শিখার জন্য এখন আমরা প্রস্তুত, কিন্তু গেম ডেভেলপমেন্ট নিয়ে আলোচনা করার আগে কম্পিউটার গেমসকে একটু নতুন ভাবে চিনে আসা যাক, 

#### # গেম কি আলিবাবার বাক্স? ¯\\(°_o)/¯
---
প্রচলিত ধারণা থেকে খুব সহজে আমরা বলতে পারি গেম বিনোদনের একটা মাধ্যম ছাড়া আর কিছুই না। যে গেম গুলো আমরা কম্পিউটার এ খেলে থাকি সেগুলোকে আমরা কম্পিউটার গেম বলে আখ্যায়িত করি, তাই না? কিন্তু এই সংজ্ঞা আমাদের কম্পিউটার গেম বানাতে কোনো কাজে আসবে না! তাহলে গেম এর সংজ্ঞা কি হতে পারে?

একবিংশ শতাব্দীতে এসে আমরা কে-ই বা মুভি না দেখি! এখন একটু চিন্তা করা যাক একটা মুভি আসলে কি? একটা মুভি হলো অনেক ক্ষুদ্র সময়ে ছবির ক্রমাগত পরিবর্তন। এটা আবার কি বলে ফেললাম! ঠিকই শুনেছো। একটা মুভি, অনেক গুলো ছবির সমন্বয়ে বানানো হয়। যেখানে ছবি গুলিকে এতো যলদি পরিবর্তন করে দেখানো হয় যে আমাদের মস্তিষ্ক মনে করে এটা একটা চলমান দৃশ্য। এই প্রসেসটাকে বলে অ্যানিমেশন এবং এই ধারার মুভি গুলোকে বলে এনিমেটেড মুভি। এই অ্যানিমেশন অথবা ছবি পরিবর্তন হওয়ার ক্রম মুভির কাহিনীর উপর ভিত্তি করে ঠিক করা হয়। অর্থাৎ, ছবি পরিবর্তনের ক্রম ঠিক করার মাধ্যমে, মুভির ঘটনা ক্রম আমরা চাইলেই নিজের মত সাজিয়ে নিতে পারি। এখন কথা হলো আমি এটা নিয়ে কেন এতো কিছু বললাম?

তোমরা নিজেই চিন্তা করো, যদি এই রকম একটা এনিমেটেড মুভিতে অ্যানিমেশন/ছবি পরিবর্তনের ক্রম তুমি মুভি দেখার সময় পরিবর্তন করতে পারো তাহলে ব্যাপার টা কি দাঁড়াবে? এটা কি আর মুভি থাকবে? না, তখন আমরা এটা কে গেম বলতে পারি, তাই না!

##### তাহলে এবার আমরা বলতে পারি যে গেম, একটা Interacive Animated মুভি ছাড়া আর এর কিছুই না।

#### # GameLoop কি আলাদিনের জ্বীন না গেমের জিন?  ԅ(≖‿≖ԅ)
---
এখন আমরা জানি যে গেম আসলে কি। চলো আমরা একটা diagram দেখে আসি যেটা আমাদের গেম এর সংজ্ঞা কে সমর্থন করে -
<br>
<div style="text-align: center;">
    <img src="images/gameLoop.jpg" height="60%" width="60%">
</div>
<br>

আমরা এখন পর্যন্ত যা আলোচনা করলাম তা এখানে অনেক সহজে দেখানো হয়েছে। এখন এই diagram নিয়ে আরো কিছু আলোচনা করা যাক। কেননা যেকোনো গেম বানাতে আমাদের এই diagram টা implement করতে হবে, তারপর আমরা আমাদের গেম এর প্রয়োজন অনুযায়ী আরো অনেক features develop করে থাকি।

##### Diagram এ আমরা তিনটা core functionality দেখতে পারছি - Render, Input এবং Update। এই functionality গুলিকে একত্রে বলা হয় "GameLoop"।

কেন loop বলছি? কারণ এই functionality গুলো গেম শুরু থেকে বন্ধ করার আগ পর্যন্ত চক্রাকারে চলতে থাকে। আজকে আমাদের মূল লক্ষ্য হলো Pygame দিয়ে এই 'GameLoop' implement করার মাধ্যমে একটা simple snake গেম develop করা।

#### # GameLoop এর ময়নাতদন্ত ! (ง •̀_•́)ง
---
এবার দেখা যাক GameLoop এর ভিতর কি কি কাজ করা হয়,

* Render : মনে আছে সেই অ্যানিমেশন/ছবি পরিবর্তন করার কথা? সাধারণত render component এ আমরা অ্যানিমেশন রিলেটেড কোড করে থাকি। আমরা আরো সহজে বলতে পারি এখানে আমরা গ্রাফিক্স এর কাজ করে থাকি।

* Input : এখানে আমরা user থেকে নেওয়া নির্দেশনা(input) গ্রহণ এবং input processing এর কোড করে থাকি। এই নির্দেশনা গুলো হতে পারে keyboard key press/release, mouse motion/click, touch ইত্যাদি ।

* Update : user input event, time ইত্যাদির উপর ভিত্তি করে গেম এর কাহিনী, গ্রাফিক্স এবং গেমের  সাথে জড়িত আরো কিছু কাজ যেমন, NPC's(Non-Player Character) movement, player movement, game score, game state ইত্যাদি পরিবর্তন করতে হয় যার কোড GameLoop এর এই component এ করা হয়। 

> Clock/FPS : Frames per Second ইহা আবার কি? এটা নতুন কিছু না, ঐযে ক্ষুদ্র সময়ে ছবি পরিবর্তনের হারই FPS। GameLoop যত দ্রুত চলবে FPS তত বেশি হবে। সুতরাং, আমরা বলতে পারি GameLoop এবং FPS এর মধ্যে একটা সম্পর্ক রয়েছে। কিন্তু তা নিয়ে অন্যকোনো দিন কথা বলা যাবে।

#### # চলো এবার সাপ বানাই। 	ᕙ(`▽´)ᕗ
---
শুরুতেই বলে নেই এখানে গেমটার কোড OOP Approach এ করা হবে। কেননা, এখন গেম ডেভেলপমেন্টে OOP Approach ব্যবহার করতে উৎসাহিত করা হয় এবং আমি নিজেও OOP Approach ব্যবহার করে থাকি।

এখন, কোড দেখার আগে আমরা দুইটা system সম্পর্কে একটু জেনে আসি। 

##### Rectangle Collision System
যেকোনো গেমে আমাদের collision system লাগবেই। আমাদের snake গেমের কথাই ধরা যাক, গেমে snake যে একটা food খেতে পারবে এবং গেমে score কখন বাড়াবো তা বুঝবো কিভাবে? এইতো বুঝেগেছো, যখন snake এবং food এর object এর সংঘর্ষ (collision) হবে।

Rectangle collision system হলো সবচেয়ে সহজ collision system বলে আমার মনে হয়।
এখানে করতে কি হয়? আমরা আমাদের প্রতিটি ছবি অথবা গেমে object কে একটা করে Rectangle দিয়ে রাখি, যেটা গেমে খেলার সময় দেখা যায় না। 

এই Rectangle গুলি ছবিগুলোর সাথে move করে। তবে প্রশ্ন থেকেই যাই যে এমনটা কেন? 

কারণ দুইটা ছবির মধ্যে collision হয়েছে কিনা তা বের করা যত কঠিন, দুইটা Rectangle এর ভিতর তা বের করা তোতো সোজা। অংকের ভিতর আমি এখন যাবো না। কেননা, Pygame এটা আমাদের জন্য আগে থেকেই করে রেখেছে, আমরা শুধু তা ব্যবহার করবো, তবে তোমরা চাইলে দেখে নিতে পারো যে, দুটি Rectangle এর collision কিভাবে বের করা যায়।

<br>
<div style="text-align: center;">
    <img src="images/yAxis.png" height="60%" width="60%">
</div>
<br>

##### Computer Graphics System
বলাই বাহুল্য যে কম্পিউটার গ্রাফিক্সে (x, y) এর মান একটু ভিন্নভাবে কাজ করে। সাধারণত (0, 0) বিন্দুর অবস্থান মাঝখানে থাকার কথা।  তবে কম্পিউটার গ্রাফিক্সে (0, 0) বিন্দু top-left corner এ থাকে। ঠিক আছে বুঝলাম! আরে দাড়াও, এখনো শেষ হয় নি! মজার কথাতো বাকি আছে এখনও। কম্পিউটার গ্রাফিক্সে y এর মান উল্টাভাবে কাজ করে।

উল্টাভাবে কাজ করে! মানে কি? এর মানে হলো যদি y এর মান বাড়ানো হয় তাহলে object নিচে নামে এবং y এর মান যদি কমানো হয় তাহলে object উপরে উঠে। মজার না ব্যাপারটা?
<br>
<div style="text-align: center;">
    <img src="images/yAxis.png" height="60%" width="60%">
</div>
<br>

##### Self Explanatory Source Code
```
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

            self.gameClock.tick(self.maxFPS)
            pygame.display.flip()
            pygame.display.update()

    def run(self) -> None:
        """
        Start the game.
        """
        self.gameLoop()


if __name__ == "__main__":
    # Run the game when the script is executed
    Game().run()

```
ভয় পেলে নাকি ? আরেহ ভয়ের কিছু নেই, আসো, কিছু ধাপে বিশ্লেষণ করা যাক -
