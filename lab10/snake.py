import pygame
import random
import datetime
import psycopg2
from pygame.math import Vector2

# Initialize pygame
pygame.init()

# Set up screen
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Snake Game')

# Set up fonts
font = pygame.font.Font(None, 36)

# Database connection
conn = psycopg2.connect("dbname=snake_game user=your_username password=your_password host=localhost")
cur = conn.cursor()

# Snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]  # Head and body of the snake
        self.eated = False  # Flag to check if snake ate the fruit
        self.isDead = False  # Flag to check if snake is dead

    def draw(self):
        for block in self.body:  # Iterate through each block of the snake
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 128, 0), body_rect)  # Drawing the snake body
        snake_head = pygame.Rect(self.body[0].x * cell_size, self.body[0].y * cell_size, cell_size, cell_size)
        headTexture = pygame.image.load('snakehead.png')
        headTexture = pygame.transform.scale(headTexture, (40, 40))
        screen.blit(headTexture, snake_head)

    def move(self, direction):
        if self.eated:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy
            self.eated = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy

# Fruit class
class Fruit:
    def __init__(self):
        self.randomize()

    def draw(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        self.food = pygame.image.load(f'food{self.randomFood}.png').convert_alpha()  # Spawn random fruit
        self.food = pygame.transform.scale(self.food, (35, 35))
        screen.blit(self.food, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)
        self.randomFood = random.randint(1, 3)

# Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.level = 1
        self.score = 0

    def update(self):
        self.snake.move(direction)
        self.checkCollision()

    def draw(self):
        self.snake.draw()
        self.fruit.draw()
        self.drawScore()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.eated = True
            if self.fruit.randomFood == 1:
                self.score += 1
            if self.fruit.randomFood == 2:
                self.score += 2
            if self.fruit.randomFood == 3:
                self.score += 3
            self.fruit.randomize()

    def drawScore(self):
        score_text = "Score: " + str(self.score)
        score_surface = font.render(score_text, True, (56, 74, 12))
        score_rect = score_surface.get_rect(center=(cell_size * cell_number - 150, 40))
        screen.blit(score_surface, score_rect)

    def gameOver(self):
        if self.snake.body[0].x >= 20 or self.snake.body[0].x < 0 or self.snake.body[0].y >= 20 or self.snake.body[0].y < 0:
            return True
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True
        return False

# Main function to start the game
def start_game():
    global direction
    game = Game()
    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_RIGHT:
                    if direction.x != -1:
                        direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if direction.x != 1:
                        direction = Vector2(-1, 0)
                if event.key == pygame.K_UP:
                    if direction.y != 1:
                        direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if direction.y != -1:
                        direction = Vector2(0, 1)

        game.update()
        screen.fill((0, 0, 0))  # Fill the screen with black before drawing
        game.draw()

        if game.gameOver():
            done = True

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

# Set initial direction
direction = Vector2(1, 0)

# Start the game
start_game()
