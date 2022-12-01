import serial

def posicionamento_mortoVivo(ser):

    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
    recebeDados = ser.read_until(expected=('#').encode('ascii')).decode('ascii')
    print(recebeDados)
    distancia1 = int(recebeDados[4:7])

    recebeDados = ser.read_until(expected=('#').encode('ascii')).decode('ascii')
    print(recebeDados)
    distancia2 = int(recebeDados[4:7])

    

    if distancia1 <= 100 or distancia2 <= 100:
        return "vivo"
    else:
        return "morto"









