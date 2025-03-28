# 2) Snake Game with levels, score, grid and collisions
import pygame
import random
from color_pallete import *  # импорт цветов из отдельного файла

pygame.init()

# Размеры окна и клетки сетки
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Рисуем шахматную сетку
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


# Класс для представления точки (ячейки) на поле
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Класс змейки
class Snake:
    def __init__(self):
        # Инициализация тела змейки из трёх сегментов
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0  # направление движения (вправо)
        self.grow = False        # флаг для роста змейки

    def move(self):
        # Если съела еду — удлиняем
        if self.grow:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.grow = False

        # Двигаем тело змейки от хвоста к голове
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Перемещаем голову по направлению
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        # Рисуем голову (красным), тело (жёлтым)
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        # Проверка столкновения головы с едой
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow = True
            return True
        return False

    def check_self_collision(self):
        # Проверка на столкновение с собственным телом
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

    def check_wall_collision(self):
        # Проверка выхода за пределы экрана
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL


# Класс еды
class Food:
    def __init__(self):
        self.randomize()  # генерируем позицию при создании

    def randomize(self):
        # Случайная позиция еды на игровом поле
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


# Функция для отображения текста на экране
def draw_text(text, x, y, color):
    font = pygame.font.Font(None, 36)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


# Настройки игры
FPS = 5
score = 0
level = 1
clock = pygame.time.Clock()
food = Food()
snake = Snake()
game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, "red")

# Главный игровой цикл
running = True
while running:
    screen.fill(colorBLACK)        # очищаем экран
    draw_grid_chess()              # отрисовываем фон

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Стрелки для управления направлением змейки
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    # Движение змейки
    snake.move()

    # Проверка на проигрыш
    if snake.check_self_collision() or snake.check_wall_collision():
        screen.fill(colorBLACK)
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
        continue

    # Проверка столкновения с едой
    if snake.check_collision(food):
        food.randomize()
        score += 1

        # Увеличение уровня и скорости каждые 4 очка
        if score % 4 == 0:
            level += 1
            FPS += 1

    # Отрисовка объектов
    snake.draw()
    food.draw()
    draw_text(f"Score: {score}", 10, 10, colorBLACK)
    draw_text(f"Level: {level}", 10, 40, colorBLACK)

    pygame.display.flip()
    clock.tick(FPS)  # Ограничение FPS в зависимости от уровня

pygame.quit()
