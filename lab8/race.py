# Импортируем библиотеки: pygame для игры, random для случайных позиций, time для паузы
import pygame
import random
import time

# Инициализация Pygame и звуковой системы
pygame.init()
pygame.mixer.init()

# Настройка частоты обновления кадров (FPS)
clock = pygame.time.Clock()
FPS = 60

# Размеры окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка фонового изображения
backgroud = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/AnimatedStreet.png")

# Загрузка изображений игрока, врага и монетки
player_img = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/Player.png")
enemy_img = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/Enemy.png")
coin_img = pygame.image.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/coin.png")

# Изменяем размер изображения монеты
coin_img = pygame.transform.scale(coin_img, (55, 55))

# Загрузка фоновой музыки и звука столкновения
backgroud_music = pygame.mixer.music.load(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/background.wav")
crash_sound = pygame.mixer.Sound(r"/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-8/lab8/crash.wav")

# Настройка шрифта и текста "Game Over"
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "red")

# Шрифт и счётчик монет
coin_count_font = pygame.font.SysFont("Verdana", 20)
coin_count = 0

# Воспроизведение фоновой музыки в бесконечном цикле
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
        self.rect.x = WIDTH // 2 - self.rect.w // 2  # Центр по горизонтали
        self.rect.y = HEIGHT - self.rect.h           # Внизу экрана
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)  # Движение влево
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)   # Движение вправо
        # Ограничения, чтобы не выйти за границы экрана
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
        self.generate_random_rect()  # Генерация позиции при старте
        
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)  # Движение вниз
        if self.rect.top > HEIGHT:         # Если вышел за экран — появится сверху
            self.generate_random_rect()
            
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0  # Появляется вверху экрана

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED // 2)  # Монета двигается медленнее врага
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
            
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h  # Появляется чуть выше экрана

# Создание объектов игры
player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# Добавление объектов в группы
all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение фона
    screen.blit(backgroud, (0, 0))

    # Движение объектов
    player.move()
    enemy.move()
    coin.move()

    # Отрисовка всех объектов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Столкновение с монетой
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_count += 1  # Увеличиваем счётчик
        coin.generate_random_rect()  # Перемещаем монету вверх

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()  # Звук аварии
        time.sleep(1)       # Пауза

        # Показ надписи "Game Over"
        screen.fill("black")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)       # Пауза перед завершением
        running = False

    # Отображение количества собранных монет
    counting = coin_count_font.render(f"Coins: {coin_count}", True, "black")
    screen.blit(counting, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение игры
pygame.quit()
