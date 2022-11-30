def posicionamento_mortoVivo(ser):

    recebeDados = self.ser.read_until(expected=('#').encode('ascii')).decode('ascii')

    
    distancia = int(recebeDados[4:7])

    if distancia <= 220:
        return "vivo"
    else:
        return "morto"









