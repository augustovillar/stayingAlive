import cv2
import time

def calculaDiferenca(img1, img2, img3):
    d1 = cv2.absdiff(img3, img2)
    d2 = cv2.absdiff(img2, img1)
    imagem = cv2.bitwise_and(d1,d2)
    s,imagem = cv2.threshold(imagem, 60, 255, cv2.THRESH_BINARY)
    return imagem


def detectaMov(tempoDeEspera=2, parado=False):

    webcam = cv2.VideoCapture(1)
    ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
    penultima = ultima
    antepenultima = ultima

    #guarda tmepo para o cronometro
    timestart = time.time()
    soma = 0 
    i = 0
     
    while (True):
        ret, frame = webcam.read()
        antepenultima = penultima
        penultima = ultima
        ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
        variavel = sum(sum(calculaDiferenca(antepenultima, penultima, ultima)))
        
        if variavel:
            i+=1
            soma = soma + variavel
        print(soma)
        timeafter = time.time()

        if timeafter-timestart >= tempoDeEspera:

            webcam.release()

            if soma>900000 and not parado:
                print("Movimento detectado!")
                return "OK"

            elif soma<200000 and parado:
                print("Pessoa parada!")
                return "OK"
            
            return "NOK"
