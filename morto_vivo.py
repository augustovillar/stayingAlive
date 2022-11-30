import serial

def posicionamento_mortoVivo(ser):

    ser.reset_input_buffer()
    ser.reset_output_buffer()
    recebeDados = ser.read_until(expected=('#').encode('ascii')).decode('ascii')

    distancia = int(recebeDados[4:7])

    if distancia <= 220:
        return "vivo"
    else:
        return "morto"









