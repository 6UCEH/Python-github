# 1) Arcade Game: игрок уклоняется от врагов и собирает монеты

import pygame
import random
import time

# Инициализация всех модулей Pygame и звуков
pygame.init()
pygame.mixer.init()

# Настройка FPS и таймера
clock = pygame.time.Clock()
FPS = 60

# Размер окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка фонового изображения
backgroud = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/AnimatedStreet.png")

# Загрузка изображений игрока, врага и монеты
player_img = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/Player.png")
enemy_img = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/Enemy.png")
coin_img = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/coin.png")

# Устанавливаем начальный размер монеты
coin_img = pygame.transform.scale(coin_img, (55, 55))

# Загрузка музыки и звука столкновения
backgroud_music = pygame.mixer.music.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/background.wav")
crash_sound = pygame.mixer.Sound(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/crash.wav")

# Шрифт и надпись "Game Over"
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "red")

# Шрифт для счётчика монет
coin_count_font = pygame.font.SysFont("Verdana", 20)
coin_count = 0  # Сколько монет собрано

# Воспроизведение фоновой музыки бесконечно
pygame.mixer.music.play(-1)

# Скорость игрока и врага
PLAYER_SPEED = 5
ENEMY_SPEED = 4

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2  # Центрируем по горизонтали
        self.rect.y = HEIGHT - self.rect.h           # Внизу экрана
        
    def move(self):
        # Управление стрелками ← →
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        # Границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)  # Двигается вниз
        if self.rect.top > HEIGHT:         # Если ушёл за нижнюю границу — возрождается
            self.generate_random_rect()
            
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED // 2)  # Монета движется медленнее врага
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
            
    def generate_random_rect(self):
        # При каждом появлении меняем размер монеты случайно
        x = random.randint(45, 70)
        self.image = pygame.transform.scale(self.image, (x, x))
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h  # Появляется над экраном

# Создаём объекты
player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# Добавляем объекты в соответствующие группы
all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображаем фон
    screen.blit(backgroud, (0, 0))

    # Движение объектов
    player.move()
    enemy.move()
    coin.move()

    # Отрисовка объектов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Столкновение игрока с монетой
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_count += 1
        coin.generate_random_rect()

    # Столкновение игрока с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)

        screen.fill("black")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False  # Завершаем игру

    # Отображаем количество собранных монет
    counting = coin_count_font.render(f"Coins: {coin_count}", True, "black")
    screen.blit(counting, (10, 10))

    # Увеличиваем скорость врага при достижении определённого количества монет
    if coin_count == 3:
        ENEMY_SPEED = 6
    elif coin_count == 6:
        ENEMY_SPEED = 7
    elif coin_count == 12:
        ENEMY_SPEED = 8  # Чем больше монет, тем быстрее враг

    pygame.display.flip()
    clock.tick(FPS)

# Выход из игры
pygame.quit()
