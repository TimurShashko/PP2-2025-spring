import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

clock = pygame.time.Clock()

_sound_library = dict()
def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_sound("Miyagi_JEndshpil_Mav-d_-_Aphrodisiac_78725692.mp3")
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
        
    screen.fill("white")

    pygame.display.flip()
    clock.tick(60)