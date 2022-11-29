def posicionamento_mortoVivo(ser):

    recebeDados = ser.read_until(expected='#')
    
    distancia = int(recebeDados[-2:-4])

    if distancia <= 220:
        return "vivo"
    else:
        return "morto"









