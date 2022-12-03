import serial

def posicionamento_mortoVivo(ser, eMorto=False):

    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
    recebeDados = ser.read_until(expected=('#').encode('ascii')).decode('utf-8')
    print(recebeDados)
    if recebeDados[0]=="0" or recebeDados[0]=="1":
        distancia1 = int(recebeDados[4:7])
    elif recebeDados == '':
        ser.write(('d').encode('ascii'))
        ser.write(('L').encode('ascii'))
    else:
        distancia1 = int(recebeDados[5:8])
    print(recebeDados)

    recebeDados = ser.read_until(expected=('#').encode('ascii')).decode('utf-8')
    if recebeDados[0]=="0" or recebeDados[0]=="1":
        distancia2 = int(recebeDados[4:7])
    elif recebeDados == '':
        ser.write(('d').encode('ascii'))
        ser.write(('L').encode('ascii'))
    else:
        distancia2 = int(recebeDados[5:8])
    print(recebeDados)
    distancia2 = int(recebeDados[4:7])

    
    if not eMorto:
        if distancia1 <= 200 or distancia2 <= 200:
            return "vivo"
        else:
            return "morto"
    else:
        if distancia1 >= 100 or distancia2 >= 100:
            return "morto"
        else:
            return "vivo"









