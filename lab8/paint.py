# 3)
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Цвета
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)

# Начальные параметры
screen.fill(colorBLACK)
LMBpressed = False
RMBpressed = False
THICKNESS = 5
mode = "brush"  # brush (кисть), rect (прямоугольник), circle (круг)
prevX = prevY = 0
startX = startY = 0
rect = pygame.Rect(0, 0, 0, 0)
circle = pygame.Rect(0, 0, 0, 0)
rects = []  # Храним нарисованные фигуры
circles = []
drawing_surface = screen.copy()
curr_color = colorRED  # Выбранный цвет
clock = pygame.time.Clock()

done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        mode = "brush"
      elif event.key == pygame.K_2:
        mode = "rect"
      elif event.key == pygame.K_3:
        mode = "circle"
      elif event.key == pygame.K_EQUALS:
        THICKNESS += 1
      elif event.key == pygame.K_MINUS:
        THICKNESS = max(1, THICKNESS - 1)
      elif event.key == pygame.K_c:
        screen.fill(colorBLACK)
        rects.clear()
        circles.clear()
        drawing_surface = screen.copy()
      elif event.key == pygame.K_r:
        curr_color = colorRED
      elif event.key == pygame.K_g:
        curr_color = colorGREEN
      elif event.key == pygame.K_b:
        curr_color = colorBLUE
    
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Левая кнопка (рисование)
        LMBpressed = True
        prevX, prevY = event.pos
        if mode == "rect":
          startX, startY = event.pos
          rect = pygame.Rect(startX, startY, 0, 0)
        elif mode == "circle":
          startX, startY = event.pos
          circle = pygame.Rect(startX, startY, 0, 0)
      elif event.button == 3:  # Правая кнопка (ластик)
        RMBpressed = True
        prevX, prevY = event.pos
    
    elif event.type == pygame.MOUSEMOTION:
      currX, currY = event.pos
      if LMBpressed and mode == "brush":
        pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY
      elif LMBpressed and mode == "rect":
        rect.x = min(startX, currX)
        rect.y = min(startY, currY)
        rect.width = abs(currX - startX)
        rect.height = abs(currY - startY)
      elif LMBpressed and mode == "circle":
        radius = max(abs(currX - startX), abs(currY - startY)) // 2
        circle.x = startX - radius
        circle.y = startY - radius
        circle.width = circle.height = radius * 2
      elif RMBpressed:  # Ластик
        pygame.draw.line(drawing_surface, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
        prevX, prevY = currX, currY
    
    elif event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
        LMBpressed = False
        if mode == "rect":
          rects.append((rect.copy(), curr_color))  # Сохраняем прямоугольник
        elif mode == "circle":
          circles.append((circle.copy(), curr_color))  # Сохраняем круг
      elif event.button == 3:
        RMBpressed = False

  # Перерисовываем экран
  screen.blit(drawing_surface, (0, 0))
  for r, color in rects:
    pygame.draw.rect(screen, color, r, 2)
  for c, color in circles:
    pygame.draw.ellipse(screen, color, c, 2)

  # Отображаем текущую фигуру
  if LMBpressed and mode == "rect":
    pygame.draw.rect(screen, curr_color, rect, 2)
  elif LMBpressed and mode == "circle":
    pygame.draw.ellipse(screen, curr_color, circle, 2)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()