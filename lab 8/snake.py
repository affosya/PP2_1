import pygame
import sys
import random

pygame.init()

# Основные параметры экрана
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Загрузка фонового изображения
background = pygame.image.load(r"C:\Users\Альбина\OneDrive\Рабочий стол\field.png")
background = pygame.transform.scale(background, (width, height))  # Масштабирование по размеру экрана

# Цвета и шрифт
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)  # Цвет сетки
font = pygame.font.Font(None, 36)  # Использование стандартного шрифта

# Параметры змейки и еды
cell_size = 20
# Определение размера ячейки игрового поля.
snake = [(width // 2, height // 2)]
direction = (0, -cell_size)  # Начальное движение вверх
food = (random.randint(0, (width-cell_size)//cell_size) * cell_size,
        random.randint(0, (height-cell_size)//cell_size) * cell_size)
score = 0  # Счетчик очков

# Параметр скорости
speed = 10

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, cell_size):
                direction = (0, -cell_size)
            elif event.key == pygame.K_DOWN and direction != (0, -cell_size):
                direction = (0, cell_size)
            elif event.key == pygame.K_LEFT and direction != (cell_size, 0):
                direction = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-cell_size, 0):
                direction = (cell_size, 0)

    # Тороидальное перемещение змейки
    new_head = ((snake[0][0] + direction[0]), (snake[0][1] + direction[1]))

    if (snake[0][0] < 0 or snake[0][0] >= width or
         snake[0][1] < 0 or snake[0][1] >= height):
         running = False

    # Проверка на столкновение с самим собой
    if new_head in snake:
        running = False

    snake.insert(0, new_head)
    
    # Еда и рост змейки
    if snake[0] == food:
        score += 10  # Увеличение счета
        food = (random.randint(0, (width-cell_size)//cell_size) * cell_size,
                random.randint(0, (height-cell_size)//cell_size) * cell_size)
    else:
        snake.pop()

    # Отрисовка фона, змейки и еды
    screen.blit(background, (0, 0))

    # Отрисовка сетки
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, gray, (x, 0), (x, height), 1)
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, gray, (0, y), (width, y), 1)

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, green, pygame.Rect(segment[0], segment[1], cell_size, cell_size))
    
    # Отрисовка еды
    pygame.draw.rect(screen, red, pygame.Rect(food[0], food[1], cell_size, cell_size))

    # Отображение счета
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(speed)

# Завершение игры
pygame.quit()
sys.exit()
