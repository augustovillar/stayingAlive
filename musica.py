import pygame

def tocaMusica(nome):
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(nome)
    pygame.mixer.music.play()
    pygame.event.wait()

def pauseMusica():
    pygame.mixer.music.pause()

def unpauseMusica():
    pygame.mixer.music.unpause()

tocaMusica('audio_teste.mp3')