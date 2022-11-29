import multiprocessing
from playsound import playsound

p = ''

def tocaMusica(musicaNome):
    global p
    p = multiprocessing.Process(target=playsound, args=(musicaNome,))
    p.start()

def paraMusica():
    global p
    p.terminate()
