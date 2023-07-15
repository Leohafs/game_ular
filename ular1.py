import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Lebar dan tinggi layar
screen_width = 800
screen_height = 600

# Ukuran blok ular dan kecepatan pergerakan
block_size = 20
snake_speed = 15

# Font skor
font_style = pygame.font.SysFont(None, 50)
font_replay = pygame.font.SysFont(None, 30)

# Fungsi untuk menampilkan skor
def Your_score(score):
    value = font_style.render("Skor: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Fungsi untuk menampilkan pesan replay
def Replay_message():
    replay_text = font_replay.render("Tekan SPACE untuk Replay atau ESC untuk Keluar", True, WHITE)
    screen.blit(replay_text, [screen_width//2 - replay_text.get_width()//2, screen_height//2])

# Fungsi untuk menggambar ular
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

# Membuat layar game
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game Ular')

game_over = False
game_exit = False

# Koordinat awal ular
x1 = screen_width / 2
y1 = screen_height / 2

# Perubahan koordinat
x1_change = 0
y1_change = 0

# Membuat list untuk menyimpan koordinat ular
snake_List = []
Length_of_snake = 1

# Membuat koordinat makanan
foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0

clock = pygame.time.Clock()

while not game_exit:
    while game_over:
        screen.fill(BLACK)
        Replay_message()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Mengatur ulang variabel game dan ular
                    game_over = False
                    game_exit = False
                    x1 = screen_width / 2
                    y1 = screen_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_List = []
                    Length_of_snake = 1
                    foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
                    foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
                elif event.key == pygame.K_ESCAPE:
                    game_exit = True
                    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = block_size
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -block_size
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = block_size
                x1_change = 0

    # Batasan layar
    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_over = True

    # Perubahan koordinat ular
    x1 += x1_change
    y1 += y1_change

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [foodx, foody, block_size, block_size])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    # Tabrakan dengan tubuh ular
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_over = True

    our_snake(block_size, snake_List)
    Your_score(Length_of_snake - 1)

    pygame.display.update()

    # Makanan dimakan oleh ular
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
        foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
        Length_of_snake += 1

    clock.tick(snake_speed)

# Menutup Pygame
pygame.quit()
