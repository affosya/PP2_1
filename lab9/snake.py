import pygame
import sys
import random
import time

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
snake = [(width // 2, height // 2)]
direction = (0, -cell_size)  # Начальное движение вверх
food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
        random.randint(0, (height - cell_size) // cell_size) * cell_size)
food_timer = time.time()  # Время появления первой еды
food_duration = random.randint(5, 10)  # Первая еда исчезает через случайное время
food2 = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
         random.randint(0, (height - cell_size) // cell_size) * cell_size)  # Вторая еда
food2_timer = time.time()  # Время появления второй еды
food2_duration = random.randint(5, 10)  # Вторая еда исчезает через случайное время
score = 0  # Счетчик очков

# Параметр скорости
speed = 6

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

    # Проверка на столкновение с границами
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        running = False

    # Проверка на столкновение с самим собой
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # Проверка на поедание первой еды
    if snake[0] == food:
        score += 10  # Увеличение счета
        food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                random.randint(0, (height - cell_size) // cell_size) * cell_size)
        food_timer = time.time()  # Обновляем время появления новой еды
        food_duration = random.randint(5, 10)  # Новый случайный таймер
    else:
        snake.pop()

    # Проверка на поедание второй еды
    if snake[0] == food2:
        score += 20  # Увеличение счета за вторую еду
        food2 = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                 random.randint(0, (height - cell_size) // cell_size) * cell_size)
        food2_timer = time.time()  # Обновляем время появления новой второй еды
        food2_duration = random.randint(5, 10)  # Новый случайный таймер для второй еды

    # Удаление еды, если прошло слишком много времени
    if time.time() - food_timer > food_duration:
        food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                random.randint(0, (height - cell_size) // cell_size) * cell_size)
        food_timer = time.time()  # Сброс таймера

    if time.time() - food2_timer > food2_duration:
        food2 = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                 random.randint(0, (height - cell_size) // cell_size) * cell_size)
        food2_timer = time.time()  # Сброс таймера для второй еды

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
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(food2[0], food2[1], cell_size, cell_size))  # Вторая еда синяя

    # Отображение счета
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(speed)

# Завершение игры
pygame.quit()
sys.exit()
