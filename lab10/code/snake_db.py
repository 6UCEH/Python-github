import psycopg2
import pygame
import random
import time

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 600
CELL = 30  # Размер одной клетки
FPS = 5    # Начальная скорость игры

# Цвета
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)    
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
colorPURPLE = (128, 0, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Verdana", 60)
game_over_text = font.render("Game Over", True, colorRED)
score_font = pygame.font.SysFont("Verdana", 20)

def get_connection():
  return psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
  )

def create_tables():
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) UNIQUE
    );
  """)
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
      id SERIAL PRIMARY KEY,
      user_id INTEGER REFERENCES users(id),
      score INTEGER,
      level INTEGER,
      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
  """)
  conn.commit()
  cursor.close()
  conn.close()

def get_or_create_user(username):
  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
  user = cursor.fetchone()

  if user:
    user_id = user[0]
    cursor.execute(
      "SELECT score, level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1",
      (user_id,)
    )
    last = cursor.fetchone()
    if last:
      score, level = last
    else:
      score, level = 0, 1
    print(f"Добро пожаловать, {username}! Уровень: {level}, Очки: {score}")
  else:
    cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cursor.fetchone()[0]
    score, level = 0, 1
    print(f"Создан новый пользователь: {username}, уровень: {level}, очки: {score}")

  conn.commit()
  cursor.close()
  conn.close()
  return user_id, level, score

def save_score(user_id, score, level):
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute(
    "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
    (user_id, score, level)
  )
  conn.commit()
  cursor.close()
  conn.close()
  print(f"Сохранено! Очки: {score}, уровень: {level}")

def draw_grid():
  for i in range(HEIGHT // CELL):
    for j in range(WIDTH // CELL):
      pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def increase_level(snake, current_level, current_fps):
  if snake.score >= current_level * 10:
    new_level = current_level + 1
    new_fps = min(current_fps + 1, 15)
    print(f"Повышение уровня! Уровень: {new_level}, Скорость: {new_fps}")
    return new_level, new_fps
  return current_level, current_fps

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Snake:
  def __init__(self):
    self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
    self.dx = 1
    self.dy = 0
    self.growing = False
    self.score = 0

  def move(self):
    new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
    new_head.x = new_head.x % (WIDTH // CELL)
    new_head.y = new_head.y % (HEIGHT // CELL)
    if any(new_head.x == segment.x and new_head.y == segment.y for segment in self.body):
      return False
    self.body.insert(0, new_head)
    if not self.growing:
      self.body.pop()
    else:
      self.growing = False
    return True

  def draw(self):
    pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
    for segment in self.body[1:]:
      pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

  def check_collision(self, food_manager):
    for food in food_manager.foods:
      if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
        self.growing = True
        self.score += food.value
        food_manager.remove_food(food)
        return

class Food:
  def __init__(self):
    self.pos = self.generate_random_pos()
    self.spawn_time = time.time()
    self.lifetime = random.uniform(5, 15)
    self.value = 1

  def generate_random_pos(self):
    return Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

  def draw(self):
    pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

  def is_expired(self):
    return time.time() - self.spawn_time > self.lifetime

class SpecialFood(Food):
  def __init__(self):
    super().__init__()
    self.value = 3
    self.lifetime = random.uniform(3, 7)

  def draw(self):
    pygame.draw.rect(screen, colorPURPLE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class FoodManager:
  def __init__(self):
    self.foods = []
    self.last_spawn_time = time.time()
    self.spawn_interval = 3

  def update(self):
    current_time = time.time()
    self.foods = [food for food in self.foods if not food.is_expired()]
    if current_time - self.last_spawn_time > self.spawn_interval:
      self.spawn_food()
      self.last_spawn_time = current_time

  def spawn_food(self):
    food = SpecialFood() if random.random() < 0.3 else Food()
    self.foods.append(food)

  def remove_food(self, food):
    if food in self.foods:
      self.foods.remove(food)

  def draw(self):
    for food in self.foods:
      food.draw()

# --- MAIN GAME ---
create_tables()
snake = Snake()
food_manager = FoodManager()
clock = pygame.time.Clock()

username = input("Введите ваше имя: ")
user_id, level, score = get_or_create_user(username)
snake.score = score

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT and snake.dx == 0:
        snake.dx, snake.dy = 1, 0
      elif event.key == pygame.K_LEFT and snake.dx == 0:
        snake.dx, snake.dy = -1, 0
      elif event.key == pygame.K_DOWN and snake.dy == 0:
        snake.dx, snake.dy = 0, 1
      elif event.key == pygame.K_UP and snake.dy == 0:
        snake.dx, snake.dy = 0, -1

  screen.fill(colorBLACK)
  draw_grid()
  food_manager.update()

  if not snake.move():
    screen.fill(colorBLACK)
    center_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, center_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    save_score(user_id, snake.score, level)
    running = False

  snake.check_collision(food_manager)
  level, FPS = increase_level(snake, level, FPS)

  snake.draw()
  food_manager.draw()
  score_text = score_font.render(f"Счет: {snake.score}", True, colorWHITE)
  level_text = score_font.render(f"Уровень: {level}", True, colorWHITE)
  screen.blit(score_text, (10, 10))
  screen.blit(level_text, (10, 30))

  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()

import csv

def export_scores_to_csv(filename='top_scores.csv'):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.username, s.score, s.level, s.timestamp
        FROM user_score s
        JOIN users u ON s.user_id = u.id
        ORDER BY s.score DESC, s.timestamp DESC
        LIMIT 10
    """)
    rows = cursor.fetchall()
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Score', 'Level', 'Timestamp'])  # заголовки
        writer.writerows(rows)
    
    cursor.close()
    conn.close()
    print(f"Топ 10 игроков сохранён в файл: {filename}")


export_scores_to_csv()
