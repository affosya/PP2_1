import pygame
import sys
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Размеры окна и цвета
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Загрузка изображений
bg_image = pygame.image.load(r"C:\Users\Альбина\OneDrive\Рабочий стол\main.png")  # Лицо часов с Микки Маусом
hour_hand_image = pygame.image.load(r"C:\Users\Альбина\OneDrive\Рабочий стол\right-hand.png").convert_alpha()  # Правая рука для часов
minute_hand_image = pygame.image.load(r"C:\Users\Альбина\OneDrive\Рабочий стол\left-hand.png").convert_alpha()  # Левая рука для минут

# Центр экрана (центр часов)
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Функция для поворота изображения вокруг центра
def blit_rotate_center(surf, image, center, angle):
    """Поворачивает изображение вокруг центра и выводит на экран."""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect.topleft)

# Основной цикл программы
clock = pygame.time.Clock()
running = True

while running:
    # Получаем текущее время
    current_time = datetime.now()
    hours = current_time.hour % 12  # 12-часовой формат
    minutes = current_time.minute
    seconds = current_time.second

    # Углы для стрелок: 360 градусов за полный круг
    hour_angle = -(360 / 12) * hours - (30 / 60) * minutes  # Движение часов на минутные доли
    minute_angle = -(360 / 60) * minutes - (6 / 60) * seconds  # Движение минут на секундные доли

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона и отображение часов
    screen.fill(WHITE)
    screen.blit(bg_image, (center_x - bg_image.get_width() // 2, center_y - bg_image.get_height() // 2))

    # Отображение часовой стрелки (правая рука)
    blit_rotate_center(screen, hour_hand_image, (center_x, center_y), hour_angle)

    # Отображение минутной стрелки (левая рука)
    blit_rotate_center(screen, minute_hand_image, (center_x, center_y), minute_angle)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
