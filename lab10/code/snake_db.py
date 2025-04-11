import psycopg2
import pygame
import random
import time

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="bisert",
    user="bisert",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Создание таблиц
def create_tables():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_account (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES user_account(id) ON DELETE CASCADE,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        )
    """)
    conn.commit()

# Получить или создать пользователя
def get_or_create_user(username):
    cur.execute("SELECT id FROM user_account WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        cur.execute("INSERT INTO user_account (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        return user_id

# Получение уровня пользователя
def get_user_level(user_id):
    cur.execute("SELECT level FROM user_score WHERE user_id = %s", (user_id,))
    level = cur.fetchone()
    return level[0] if level else 1

# Сохранение прогресса
def save_game(user_id, score, level):
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s",
                (score, level, user_id))
    conn.commit()

# --------------------------------------------
# ИГРА SNAKE (очень базовая версия с паузой)
# --------------------------------------------
pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 20)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

def game_loop(user_id, level):
    snake = [(100, 100), (80, 100)]
    direction = (CELL, 0)
    food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    score = 0
    speed = 5 + level * 2

    running = True
    paused = False

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -CELL)
                elif event.key == pygame.K_DOWN:
                    direction = (0, CELL)
                elif event.key == pygame.K_LEFT:
                    direction = (-CELL, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (CELL, 0)
                elif event.key == pygame.K_p:
                    save_game(user_id, score, level)
                    paused = True
                    print("Game paused and saved.")
                elif event.key == pygame.K_r:
                    paused = False
                    print("Resumed")

        if paused:
            pygame.display.update()
            clock.tick(3)
            continue

        # движение змеи
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake = [head] + snake[:-1]

        # еда
        if head == food:
            snake.append(snake[-1])
            score += 10
            food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
            if score % 50 == 0:
                level += 1
                speed += 1

        # отрисовка
        draw_snake(snake)
        draw_food(food)

        # отображение счёта
        text = font.render(f"Score: {score}  Level: {level}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(speed)

# ----------------------------
# Основная логика запуска
# ----------------------------
if __name__ == "__main__":
    create_tables()
    username = input("Введите имя пользователя: ")
    user_id = get_or_create_user(username)
    level = get_user_level(user_id)

    print(f"Текущий уровень пользователя {username}: {level}")
    game_loop(user_id, level)
