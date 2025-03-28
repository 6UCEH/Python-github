# Paint App — Lab 9
# Расширенная версия: кисть, прямоугольник, круг, квадрат, треугольники, ромб

import pygame
import math

pygame.init()

# Настройки окна
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
LMBpressed = False     # Левая кнопка мыши нажата?
RMBpressed = False     # Правая кнопка мыши нажата?
THICKNESS = 5          # Толщина линий
mode = "brush"         # brush, rect, circle, square, r_triangle, e_triangle, rhombus
curr_color = colorRED  # Цвет по умолчанию
clock = pygame.time.Clock()

# Переменные для рисования
prevX = prevY = 0
startX = startY = 0
rect = pygame.Rect(0, 0, 0, 0)
circle = pygame.Rect(0, 0, 0, 0)
square = pygame.Rect(0, 0, 0, 0)

# Фигуры для хранения истории
rects = []
circles = []
squares = []
r_triangles = []
e_triangles = []
rhombuses = []

# Временные фигуры во время рисования
r_triangle = []
e_triangle = []
rhombus = []

# Поверхность для рисования
drawing_surface = screen.copy()

# Главный цикл
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Клавиши для выбора режима, цвета, очистки
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "brush"
            elif event.key == pygame.K_2:
                mode = "rect"
            elif event.key == pygame.K_3:
                mode = "circle"
            elif event.key == pygame.K_4:
                mode = "square"
            elif event.key == pygame.K_5:
                mode = "r_triangle"
            elif event.key == pygame.K_6:
                mode = "e_triangle"
            elif event.key == pygame.K_7:
                mode = "rhombus"
            elif event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            elif event.key == pygame.K_c:
                # Очистка экрана
                screen.fill(colorBLACK)
                drawing_surface = screen.copy()
                rects.clear()
                circles.clear()
                squares.clear()
                r_triangles.clear()
                e_triangles.clear()
                rhombuses.clear()
            elif event.key == pygame.K_r:
                curr_color = colorRED
            elif event.key == pygame.K_g:
                curr_color = colorGREEN
            elif event.key == pygame.K_b:
                curr_color = colorBLUE

        # Нажатие мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                LMBpressed = True
                prevX, prevY = event.pos
                startX, startY = event.pos

                if mode == "rect":
                    rect = pygame.Rect(startX, startY, 0, 0)
                elif mode == "circle":
                    circle = pygame.Rect(startX, startY, 0, 0)
                elif mode == "square":
                    square = pygame.Rect(startX, startY, 0, 0)
                elif mode == "r_triangle":
                    r_triangle = [(startX, startY), (startX, startY), (startX, startY)]
                elif mode == "e_triangle":
                    e_triangle = [(startX, startY), (startX, startY), (startX, startY)]
                elif mode == "rhombus":
                    rhombus = [(startX, startY)] * 4

            elif event.button == 3:
                RMBpressed = True
                prevX, prevY = event.pos

        # Движение мыши
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

            elif LMBpressed and mode == "square":
                side = abs(currX - startX)
                square.x = min(startX, currX)
                square.y = min(startY, currY)
                square.width = square.height = side

            elif LMBpressed and mode == "r_triangle":
                r_triangle = [
                    (startX, startY),
                    (startX, currY),
                    (currX, currY)
                ]

            elif LMBpressed and mode == "e_triangle":
                side = abs(currX - startX)
                height = (math.sqrt(3) / 2) * side
                e_triangle = [
                    (startX, startY),
                    (startX + side, startY),
                    (startX + side / 2, startY - height)
                ]

            elif LMBpressed and mode == "rhombus":
                centerX = (startX + currX) // 2
                centerY = (startY + currY) // 2
                width = abs(currX - startX)
                height = abs(currY - startY)
                rhombus = [
                    (centerX, centerY - height // 2),  # Верх
                    (centerX + width // 2, centerY),   # Право
                    (centerX, centerY + height // 2),  # Низ
                    (centerX - width // 2, centerY)    # Лево
                ]

            elif RMBpressed:
                pygame.draw.line(drawing_surface, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY

        # Отпускание кнопки мыши — сохраняем фигуру
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                LMBpressed = False
                if mode == "rect":
                    rects.append((rect.copy(), curr_color))
                elif mode == "circle":
                    circles.append((circle.copy(), curr_color))
                elif mode == "square":
                    squares.append((square.copy(), curr_color))
                elif mode == "r_triangle":
                    r_triangles.append((r_triangle.copy(), curr_color))
                elif mode == "e_triangle":
                    e_triangles.append((e_triangle.copy(), curr_color))
                elif mode == "rhombus":
                    rhombuses.append((rhombus.copy(), curr_color))
            elif event.button == 3:
                RMBpressed = False

    # Перерисовка всех фигур
    screen.blit(drawing_surface, (0, 0))
    for r, color in rects:
        pygame.draw.rect(screen, color, r, 2)
    for c, color in circles:
        pygame.draw.ellipse(screen, color, c, 2)
    for s, color in squares:
        pygame.draw.rect(screen, color, s, 2)
    for t, color in r_triangles:
        pygame.draw.polygon(screen, color, t, 2)
    for t, color in e_triangles:
        pygame.draw.polygon(screen, color, t, 2)
    for rh, color in rhombuses:
        pygame.draw.polygon(screen, color, rh, 2)

    # Отображение текущей фигуры при рисовании
    if LMBpressed:
        if mode == "rect":
            pygame.draw.rect(screen, curr_color, rect, 2)
        elif mode == "circle":
            pygame.draw.ellipse(screen, curr_color, circle, 2)
        elif mode == "square":
            pygame.draw.rect(screen, curr_color, square, 2)
        elif mode == "r_triangle":
            pygame.draw.polygon(screen, curr_color, r_triangle, 2)
        elif mode == "e_triangle":
            pygame.draw.polygon(screen, curr_color, e_triangle, 2)
        elif mode == "rhombus":
            pygame.draw.polygon(screen, curr_color, rhombus, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
