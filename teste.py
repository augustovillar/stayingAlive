import cv2
from tkinter import *
import serial
import time

def calculaDiferenca(img1, img2, img3):
    """
    Captura o movimento pela subtração de pixel dos frames.
    """
    d1 = cv2.absdiff(img3, img2)
    d2 = cv2.absdiff(img2, img1)
    imagem = cv2.bitwise_and(d1,d2)
    s,imagem = cv2.threshold(imagem, 60, 255, cv2.THRESH_BINARY)
    return imagem


def liga(event):
    """
    Inicia a detecção de movimento utlizando a webcam conectada. Salva as capturas de movimentos em 'C:\Imagens Deteccao/.
    """
    janela = "Tela de Captura"
    janela2 = "Tela Normal"
    i=1
    cv2.namedWindow(janela, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(janela2, cv2.WINDOW_AUTOSIZE)
    webcam = cv2.VideoCapture(0)
    ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
    penultima = ultima
    antepenultima = ultima

    ser = serial.Serial('COM6', baudrate=9600, bytesize=7, stopbits=2, parity='E')

    while (True):
        ret, frame = webcam.read()
        antepenultima = penultima
        penultima = ultima
        ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
        cv2.imshow(janela, calculaDiferenca(antepenultima, penultima, ultima))
        cv2.imshow(janela2, frame)
        variavel = sum(sum(calculaDiferenca(antepenultima, penultima, ultima)))
        if variavel:
            print(variavel)
            nome = 'image'+str(i)
            i+=1
            if variavel>15000:
                ser.write(('1').encode("ascii"))
                # cv2.imwrite('C:\Imagens Projeto T4/'+nome+'.jpg', frame)

        k=cv2.waitKey(30) & 0xFF
        if k == 27:
            webcam.release()
            cv2.destroyWindow(janela)
            cv2.destroyWindow(janela2)
            break

Janela = Tk()
botao = Button(Janela, text="Ligar Detector de Movimento", fg="Black", font="Arial,9")
label = Label(Janela, text = "Para Desligar a Detecção de Movimento Pressione 'Esc'.")
label.place(x=90, y=10, width=300, height=50)
botao.bind("<Button-1>", liga)
botao.place(x=120, y=150, width=230, height=50)
Janela.geometry('450x450')
Janela.title("Detector de Movimento")
Janela.mainloop()