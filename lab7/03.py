import pygame, sys, datetime
import pygame.locals


WIDTH = 800
HEIGHT = 600
CX = WIDTH // 2
CY = HEIGHT // 2
FPS = 30

pygame.init()
pygame.display.set_caption("MP3 Player")

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
Frame = pygame.time.Clock()

is_paused = True
cur_index = 0
cur_music_path = ""
music_paths = [
  "lab7/mp1.mp3",
  "lab7/mp2.mp3",
]

def get_music_name(music_path):
  return music_path.split("/")[-1].split(".")[0]
 
def play(music_path):
  global cur_music_path
  if music_path == cur_music_path:
    pygame.mixer.music.unpause()
  else:
    cur_music_path = music_path
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play(-1)


def stop_music():
  pygame.mixer.music.pause()

prevHintFont = pygame.font.Font(None, 30)
prevHintImg = prevHintFont.render("Press LEFT ARROW to switch back", True, (255, 255, 255))

curMusicFont = pygame.font.Font(None, 30)

nextHintFont = pygame.font.Font(None, 30)
nextHintImg = nextHintFont.render("Press RIGHT ARROW to switch forward", True, (255, 255, 255))

while "Кайфовать":
  for event in pygame.event.get():
    if event.type == pygame.locals.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.locals.KEYDOWN:
      if event.key == pygame.locals.K_RIGHT:
        cur_index += 1
        cur_index = min(cur_index, len(music_paths) - 1)
        if not is_paused:
          play(music_paths[cur_index])
      elif event.key == pygame.locals.K_LEFT:
        cur_index -= 1
        cur_index = max(0, cur_index)
        if not is_paused:
          play(music_paths[cur_index])
      elif event.key == pygame.locals.K_SPACE:
        if is_paused:
          is_paused = False
          play(music_paths[cur_index])
        else:
          is_paused = True
          stop_music()
          
  
  curMusicFontImg1 = curMusicFont.render(
    f"Currently playing \"{get_music_name(music_paths[cur_index])}\"",
    True, (255, 255, 255)
  );
  curMusicFontImg2 = curMusicFont.render(
    "Paused" if is_paused else "",
    True, (255, 255, 255)
  );

  DISPLAYSURF.fill((0, 0, 0))
  DISPLAYSURF.blit(prevHintImg, (CX - prevHintImg.get_width() // 2 - 100, CY + 100))
  DISPLAYSURF.blit(curMusicFontImg1, (CX - curMusicFontImg1.get_width() // 2, CY - 100))
  DISPLAYSURF.blit(curMusicFontImg2, (CX - curMusicFontImg2.get_width() // 2, CY - 80))
  DISPLAYSURF.blit(nextHintImg, (CX - nextHintImg.get_width() // 2 + 100, CY + 140))

  pygame.display.update()

  Frame.tick(FPS)