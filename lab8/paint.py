# 3) Paint App: простая рисовалка с кистью, прямоугольником и кругом
import pygame

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")  # Заголовок окна

# Цвета RGB
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)

# Начальные параметры
screen.fill(colorBLACK)  # Заливка фона чёрным
LMBpressed = False       # ЛКМ нажата?
RMBpressed = False       # ПКМ нажата?
THICKNESS = 5            # Толщина кисти/ластика
mode = "brush"           # brush / rect / circle — режим рисования
prevX = prevY = 0        # Предыдущая позиция мыши (для кисти)
startX = startY = 0      # Начальная точка фигуры
rect = pygame.Rect(0, 0, 0, 0)     # Прямоугольник
circle = pygame.Rect(0, 0, 0, 0)   # Круг

# Списки для хранения нарисованных фигур
rects = []
circles = []

drawing_surface = screen.copy()   # Поверхность для рисования (сохраняет всё)
curr_color = colorRED             # Цвет по умолчанию
clock = pygame.time.Clock()       # Таймер для FPS

# Главный игровой цикл
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

    # Обработка клавиш
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        mode = "brush"     # Режим кисти
      elif event.key == pygame.K_2:
        mode = "rect"      # Режим прямоугольника
      elif event.key == pygame.K_3:
        mode = "circle"    # Режим круга
      elif event.key == pygame.K_EQUALS:
        THICKNESS += 1     # Увеличить толщину
      elif event.key == pygame.K_MINUS:
        THICKNESS = max(1, THICKNESS - 1)  # Уменьшить, но не меньше 1
      elif event.key == pygame.K_c:
        # Очистка экрана
        screen.fill(colorBLACK)
        rects.clear()
        circles.clear()
        drawing_surface = screen.copy()
      # Смена цвета по клавишам
      elif event.key == pygame.K_r:
        curr_color = colorRED
      elif event.key == pygame.K_g:
        curr_color = colorGREEN
      elif event.key == pygame.K_b:
        curr_color = colorBLUE

    # Нажатие кнопки мыши
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Левая кнопка — рисуем
        LMBpressed = True
        prevX, prevY = event.pos
        if mode == "rect":
          startX, startY = event.pos
          rect = pygame.Rect(startX, startY, 0, 0)
        elif mode == "circle":
          startX, startY = event.pos
          circle = pygame.Rect(startX, startY, 0, 0)
      elif event.button == 3:  # Правая кнопка — ластик
        RMBpressed = True
        prevX, prevY = event.pos

    # Движение мыши
    elif event.type == pygame.MOUSEMOTION:
      currX, currY = event.pos
      if LMBpressed and mode == "brush":
        # Рисуем линию между предыдущей и текущей точкой
        pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY
      elif LMBpressed and mode == "rect":
        # Обновляем параметры прямоугольника в реальном времени
        rect.x = min(startX, currX)
        rect.y = min(startY, currY)
        rect.width = abs(currX - startX)
        rect.height = abs(currY - startY)
      elif LMBpressed and mode == "circle":
        # Вычисляем радиус и центр круга
        radius = max(abs(currX - startX), abs(currY - startY)) // 2
        circle.x = startX - radius
        circle.y = startY - radius
        circle.width = circle.height = radius * 2
      elif RMBpressed:
        # Ластик работает как кисть, но с цветом фона
        pygame.draw.line(drawing_surface, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY

    # Отпускание мыши
    elif event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
        LMBpressed = False
        # Сохраняем нарисованную фигуру
        if mode == "rect":
          rects.append((rect.copy(), curr_color))
        elif mode == "circle":
          circles.append((circle.copy(), curr_color))
      elif event.button == 3:
        RMBpressed = False

  # Отображение холста
  screen.blit(drawing_surface, (0, 0))

  # Перерисовываем все сохранённые фигуры
  for r, color in rects:
    pygame.draw.rect(screen, color, r, 2)
  for c, color in circles:
    pygame.draw.ellipse(screen, color, c, 2)

  # Отображаем текущую фигуру (в процессе рисования)
  if LMBpressed and mode == "rect":
    pygame.draw.rect(screen, curr_color, rect, 2)
  elif LMBpressed and mode == "circle":
    pygame.draw.ellipse(screen, curr_color, circle, 2)

  # Обновление экрана
  pygame.display.flip()
  clock.tick(60)

# Завершение программы
pygame.quit()
