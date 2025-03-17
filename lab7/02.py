import pygame, sys, datetime
import pygame.locals


WIDTH = 800
HEIGHT = 600
CX = WIDTH // 2
CY = HEIGHT // 2
FPS = 30

pygame.init()
pygame.display.set_caption("Move Circle game")

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
Frame = pygame.time.Clock()

circleImage = pygame.Surface([50, 50])
pygame.draw.circle(circleImage, (255, 0, 0), (25, 25), 25)
circleRect = circleImage.get_rect()

SHIFT_PX = 20
while "Құлдық":
  for event in pygame.event.get():
    if event.type == pygame.locals.QUIT:
      pygame.quit()
      sys.exit()

  frame_keys_map = pygame.key.get_pressed()
  if frame_keys_map[pygame.locals.K_a]:
    if circleRect.x - SHIFT_PX >= 0:
      circleRect.x -= SHIFT_PX
  if frame_keys_map[pygame.locals.K_d]:
    if circleRect.x + SHIFT_PX < WIDTH - circleRect.width:
      circleRect.x += SHIFT_PX
  if frame_keys_map[pygame.locals.K_w]:
    if circleRect.y - SHIFT_PX >= 0:
      circleRect.y -= SHIFT_PX
  if frame_keys_map[pygame.locals.K_s]:
    if circleRect.y + SHIFT_PX < HEIGHT - circleRect.height:
      circleRect.y += SHIFT_PX
          
  DISPLAYSURF.fill((0, 0, 0))
  
  DISPLAYSURF.blit(circleImage, (circleRect.x, circleRect.y))

  pygame.display.update()

  Frame.tick(FPS)