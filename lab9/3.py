import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing App")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Начальные настройки инструмента и цвета
current_tool = 'pencil'  # Опции: 'pencil', 'rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'
current_color = BLACK
brush_size = 5  # Размер кисти/ластика

# Настройки инструмента
start_pos = None  # Для рисования прямоугольников и кругов

# Заполняем экран белым фоном
screen.fill(WHITE)

# Функция для рисования палитры цветов
def draw_palette():
    pygame.draw.rect(screen, BLACK, (10, 10, 30, 30))
    pygame.draw.rect(screen, BLUE, (50, 10, 30, 30))
    pygame.draw.rect(screen, GREEN, (90, 10, 30, 30))
    pygame.draw.rect(screen, RED, (130, 10, 30, 30))

# Функция для выбора цвета
def select_color(pos):
    global current_color
    if 10 <= pos[0] <= 40 and 10 <= pos[1] <= 40:
        current_color = BLACK
    elif 50 <= pos[0] <= 80 and 10 <= pos[1] <= 40:
        current_color = BLUE
    elif 90 <= pos[0] <= 120 and 10 <= pos[1] <= 40:
        current_color = GREEN
    elif 130 <= pos[0] <= 160 and 10 <= pos[1] <= 40:
        current_color = RED

# Функции для рисования фигур
def draw_square(start_pos, end_pos):
    side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    rect = pygame.Rect(start_pos[0], start_pos[1], side_length, side_length)
    pygame.draw.rect(screen, current_color, rect, 2)

def draw_right_triangle(start_pos, end_pos):
    point1 = (start_pos[0], end_pos[1])
    point2 = (end_pos[0], end_pos[1])
    point3 = end_pos
    pygame.draw.polygon(screen, current_color, [point1, point2, point3], 2)

def draw_equilateral_triangle(start_pos, end_pos):
    side_length = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
    height = int((3 ** 0.5 / 2) * side_length)
    point1 = (start_pos[0], start_pos[1])
    point2 = (start_pos[0] + side_length, start_pos[1])
    point3 = (start_pos[0] + side_length // 2, start_pos[1] - height)
    pygame.draw.polygon(screen, current_color, [point1, point2, point3], 2)

def draw_rhombus(start_pos, end_pos):
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    point1 = (start_pos[0], start_pos[1] - height // 2)
    point2 = (start_pos[0] + width // 2, start_pos[1])
    point3 = (start_pos[0], start_pos[1] + height // 2)
    point4 = (start_pos[0] - width // 2, start_pos[1])
    pygame.draw.polygon(screen, current_color, [point1, point2, point3, point4], 2)

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            # Выбор инструмента с помощью клавиш
            if event.key == pygame.K_r:
                current_tool = 'rectangle'
            elif event.key == pygame.K_c:
                current_tool = 'circle'
            elif event.key == pygame.K_e:
                current_tool = 'eraser'
            elif event.key == pygame.K_p:
                current_tool = 'pencil'
            elif event.key == pygame.K_s:
                current_tool = 'square'
            elif event.key == pygame.K_t:
                current_tool = 'right_triangle'
            elif event.key == pygame.K_l:
                current_tool = 'equilateral_triangle'
            elif event.key == pygame.K_h:
                current_tool = 'rhombus'
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Выбор цвета из палитры
            if event.button == 1:  # Левый клик
                select_color(event.pos)
                start_pos = event.pos  # Начальная позиция для рисования фигур
            
        elif event.type == pygame.MOUSEBUTTONUP:
            # Рисуем фигуру при отпускании кнопки мыши
            if current_tool == 'rectangle' and start_pos:
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
                start_pos = None
            elif current_tool == 'circle' and start_pos:
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5) // 2
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)
                start_pos = None
            elif current_tool == 'square' and start_pos:
                end_pos = event.pos
                draw_square(start_pos, end_pos)
                start_pos = None
            elif current_tool == 'right_triangle' and start_pos:
                end_pos = event.pos
                draw_right_triangle(start_pos, end_pos)
                start_pos = None
            elif current_tool == 'equilateral_triangle' and start_pos:
                end_pos = event.pos
                draw_equilateral_triangle(start_pos, end_pos)
                start_pos = None
            elif current_tool == 'rhombus' and start_pos:
                end_pos = event.pos
                draw_rhombus(start_pos, end_pos)
                start_pos = None
        
        elif event.type == pygame.MOUSEMOTION:
            # Рисование при движении мыши для карандаша и ластика
            if event.buttons[0]:  # Левый клик удерживается
                if current_tool == 'pencil':
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)
                elif current_tool == 'eraser':
                    pygame.draw.circle(screen, WHITE, event.pos, brush_size)

    # Рисуем палитру цветов
    draw_palette()

    # Обновляем экран
    pygame.display.flip()
