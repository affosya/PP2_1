import pygame

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Настройки экрана
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Music Player')
screen.fill('pink2')

# Функции управления музыкой
def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    load_and_play_music()

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    load_and_play_music()

def stop_music():
    pygame.mixer.music.stop()

def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def load_and_play_music():
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

# Список песен
songs = [
    "C:/Users/Альбина/Downloads/One Direction – Night Changes_(Naijaflavour.com).mp3",
    "C:/Users/Альбина/Downloads/Lady_Gaga_Bruno_Mars_-_Die_With_A_Smile_78217674.mp3",
    "C:/Users/Альбина/Downloads/Ayau & A.Boo - tartady.mp3"
]

# Индекс текущей песни
current_song_index = 0
load_and_play_music()  # Запуск первой песни

# Шрифт по умолчанию
font = pygame.font.SysFont('Arial', 30)
player_surface = font.render("Music Player", True, 'black')
instructions_surface = font.render("Press SPACE to Play/Pause, N for Next, P for Previous, S to Stop", True, 'black')

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пробел для воспроизведения/паузы
                play_pause_music()
            elif event.key == pygame.K_n:  # 'N' для следующей песни
                play_next_song()
            elif event.key == pygame.K_p:  # 'P' для предыдущей песни
                play_previous_song()
            elif event.key == pygame.K_s:  # 'S' для остановки музыки
                stop_music()

    # Отображение текста
    screen.fill('pink2')  # Очищаем экран
    screen.blit(player_surface, (250, 50))
    screen.blit(instructions_surface, (50, 150))

    pygame.display.flip()  # Обновляем экран

pygame.quit()
