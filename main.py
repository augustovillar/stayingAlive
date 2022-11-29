from PySide6.QtWidgets import *
from interfaceJogo import Ui_MainWindow
import sys
from database import Data_base
import serial
import time
from deteccaoMovimento import detectaMov
from musica import tocaMusica, paraMusica
import random
from morto_vivo import posicionamento_mortoVivo

nameCOM = 'COM8'


class MainWindow(QMainWindow, Ui_MainWindow):

    id_jogador1Atual = ""
    id_jogador2Atual = ""
    nomeJogador1Atual = ""
    nomeJogador2Atual = ""

    ser = ''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stayling Alive")
        self.ser = serial.Serial(nameCOM, baudrate=115200, bytesize=7, stopbits=2, parity='E', timeout=None)

        #appIncos = QIcon()

        ###############################
        #Páginas do Sistema

        #home
        self.jogoModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        # self.jogoModo2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo2))
        # self.sair.clicked encerra a execução

        #modo1
        self.doisJogadores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.cadastroDoisJogares))
        self.historico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pagHistorico))
        self.tutorial.clicked.connect(lambda: self.Pages.setCurrentWidget(self.instrucoesTutorial))
        self.voltarHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pagHome))

        #cadastro
        #self.cadastrarDoisJogadores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.configuracao1))
        self.cancelarCadModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.iniciar_config))

        #configurando player 1
        self.cancelar_conf1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        
        #configurando player 2
        self.cancelarCadModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #tutorial
        self.voltarModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #historico
        self.voltarHistorico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #ganhador
        self.telaDeCadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.cadastroDoisJogares))
        self.telaDePreparo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.iniciar_config))
        self.voltarMenu_3.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        self.voltarMenu_2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        self.voltarMenu.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        self.comecarJogo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.jogoAndamento))
        self.comecarJogo.clicked.connect(self.jogo_modo1)

        ########################################################################################
        #cadastra usuarios
        self.cadastrarDoisJogadores.clicked.connect(self.cadastrarUsuarios)
        
        #inicia posicionamento do modo 1
        self.iniciar.clicked.connect(self.posicionamento_modo1)

    def cadastrarUsuarios(self):
        db = Data_base()

        db.connect()

        jogador1Nome = self.jogador1.text().strip()
        jogador2Nome = self.jogador2.text().strip()

        if jogador1Nome=="" or jogador2Nome=="":
            dialog = QMessageBox(parent=self, text="Não foi adicionado os nomes corretamentes!")
            dialog.setWindowTitle("Erro no cadastro")
            dialog.exec()
            self.Pages.setCurrentWidget(self.cadastroDoisJogares)
            return

        #verifica se existe para assim cadastrar o usuário
        if len(db.verifica_usuario(jogador1Nome))==0:
            jogador1OK = db.cadastrar_usuario(jogador1Nome)
        else:
            jogador1OK = "JA"
        
        #retorna OK quando cadastro com sucesso
        if jogador1OK=="OK":
            print(f"O Jogador1, {jogador1Nome}, foi cadastrado com sucesso.")
        elif jogador1OK=="JA":
            print(f"O Jogador1, {jogador1Nome}, já está cadastrado.")
        else:
            print(f"O Jogador1, {jogador1Nome}, não foi cadastrado com sucesso.")
            print(jogador1OK)
        
        if len(db.verifica_usuario(jogador2Nome))==0:
            jogador2OK = db.cadastrar_usuario(jogador2Nome)
        else:
            jogador2OK = "JA"

        #retorna OK quando cadastro com sucesso
        if jogador2OK=="OK":
            print(f"O Jogador2, {jogador2Nome}, foi cadastrado com sucesso.")
        elif jogador2OK=="JA":
            print(f"O Jogador2, {jogador2Nome}, já está cadastrado.")
        else:
            print(f"O Jogador2, {jogador2Nome}, não foi cadastrado com sucesso.")

        if ((jogador1OK=="OK" or jogador1OK=="JA") and (jogador2OK=="OK" or jogador2OK=="JA")):
            dialog = QMessageBox(parent=self, text='Usuários cadastrados com sucesso!')
        else:
            dialog = QMessageBox(parent=self, text='Usuários cadastrados com sucesso!')

        dialog.setWindowTitle("Cadastro")
        dialog.exec()

        self.id_jogador1Atual = db.verifica_usuario(jogador1Nome)[0][0]
        self.id_jogador2Atual = db.verifica_usuario(jogador2Nome)[0][0]
        self.nomeJogador1Atual = jogador1Nome
        self.nomeJogador2Atual = jogador2Nome

        self.jogador1.setText('')
        self.jogador2.setText('')

        self.Pages.setCurrentWidget(self.iniciar_config)

        db.close_connection()

    def posicionamento_pessoa(self, numJogador):

        timeout = 20

        self.ser.write(('l').encode('ascii'))
        #escreve o numero para o sensor ir pra posicao do primeiro jogador
        self.ser.write((str(numJogador)).encode('ascii'))

        timeStart = time.time()
        timeNow = timeStart
        jogadorPosicionado = 0

        while timeNow-timeStart <= timeout:
            recebeDados = self.ser.read_until(expected=('#').encode('ascii')).decode('ascii')

            distancia = int(recebeDados[4:7])
            
            if distancia<=220:
                jogadorPosicionado += 1

            if jogadorPosicionado>=3:
                print('Posicionamento do jogador '+str(numJogador)+' feito com sucesso!')
                return 'OK'

            timeNow = time.time()

        print('Posicionamento do jogador '+str(numJogador)+' não foi feita com sucesso!')

        self.ser.write(('d').encode('ascii'))

        return 'TIMEOUT'

    def posicionamento_modo1(self):

        self.ser.write(('d').encode('ascii'))

        status = self.posicionamento_pessoa(1)

        if status!="OK":
            self.Pages.setCurrentWidget(self.erroConfiguracao)
            print("Posicionamento do jogador 1 não foi concluído corretamente.")
            return "ERRO1"

        status = self.posicionamento_pessoa(2)

        if status!="OK":
            self.Pages.setCurrentWidget(self.erroConfiguracao)
            print("Posicionamento do jogador 2 não foi concluído corretamente.")
            return "ERRO2"

        self.Pages.setCurrentWidget(self.jogoComecar)

        self.ser.write(('d').encode('ascii'))

        return "SUCESSO"

    def jogo_modo1(self):

        continuaJogo = True
        numeroRodadasDancandoTotais = 0
        numeroRodadasDancando = 0
        numeroRodadasParadoEmPeTotais = 0
        numeroRodadasParadoEmPe = 0
        numeroRodadasAbaixandoTotais = 0
        numeroRodadasAbaixando = 0
        

        while continuaJogo:
            #numero de rodadas da danca
            maxRodadasDancando = 4 #random.randint(1,4)
            tocaMusica("stayingalive.mp3")
            while numeroRodadasDancando <= maxRodadasDancando and continuaJogo:
                for i in range(1, 3):

                    self.ser.write((str(i)).encode('ascii'))

                    resposta = detectaMov(nameCOM, mensagem='d', tempoDeEspera=3)

                    if resposta == 'NOK':
                        if i == 1:
                            jogador1Campeao = False
                        else:
                            jogador1Campeao = True

                        continuaJogo = False

                        break
                    
                numeroRodadasDancando += 1

            #guarda info para historico
            numeroRodadasDancandoTotais += numeroRodadasDancando
            
            #zera para proxima
            numeroRodadasDancando = 0

            maxRodadasParadoEmPe = 4 #random.randint(1,4)
            paraMusica()
            tocaMusica("xuxa_minha_rainha.mp3")

            while numeroRodadasParadoEmPe <= maxRodadasParadoEmPe and continuaJogo:
                for i in range(1, 3):

                    self.ser.write((str(i)).encode('ascii'))

                    resposta = detectaMov(mensagem='d', tempoDeEspera=3)
                    estado = posicionamento_mortoVivo(i, self.ser)

                    if resposta == 'OK' and estado == "morto":
                        if i == 1:
                            jogador1Campeao = False
                        else:
                            jogador1Campeao = True

                        continuaJogo = False

                        break
                    
                numeroRodadasParadoEmPe += 1

             #guarda info para historico
            numeroRodadasParadoEmPeTotais += numeroRodadasParadoEmPe
            
            #zera para proxima
            numeroRodadasParadoEmPe = 0
            
            paraMusica()
            tocaMusica('no_ceu_tem_pao.mp3')
            maxRodadasAbaixando = 4 #random.randint(1,4) 
            while numeroRodadasAbaixando <= maxRodadasAbaixando and continuaJogo:
                for i in range(1, 3):                     

                    self.ser.write((str(i)).encode('ascii'))
                    estado = posicionamento_mortoVivo(i, self.ser)

                    if estado == 'vivo':
                        if i == 1:
                            jogador1Campeao = False
                        else:
                            jogador1Campeao = True

                        continuaJogo = False

                        break
                    
                numeroRodadasAbaixando += 1

            #soma com o total
            numeroRodadasAbaixandoTotais += numeroRodadasAbaixando

            #soma de rodadas abaixando
            numeroRodadasAbaixando = 0
            paraMusica()

        #contabiliza os pontos

        
        rodadas = [numeroRodadasAbaixandoTotais, numeroRodadasDancandoTotais, numeroRodadasParadoEmPeTotais]
        self.escreveJogo(rodadas, jogador1Campeao)

    def escreveJogo(self, rodadas, jogador1Campeao):

        #testando
        self.id_jogador1Atual  = 5
        self.id_jogador2Atual  = 6
        self.nomeJogador1Atual = 'augusto'
        self.nomeJogador2Atual = 'emilly'

        pontosEmComum = sum(rodadas)

        if jogador1Campeao:
            pontosJogador1 = pontosEmComum + 10
            pontosJogador2 = pontosEmComum
        else:
            pontosJogador1 = pontosEmComum
            pontosJogador2 = pontosEmComum + 10

        db = Data_base()

        self.Pages.setCurrentWidget(self.ganhouJogador)

        if jogador1Campeao:
            self.jogadorGanhador.setText(f"O jogador 1, {self.nomeJogador1Atual}, ganhou o jogo!")
            self.pontuacaoFim.setText(f"""Pontuação do jogador 1, {self.nomeJogador1Atual}: {str(pontosJogador1)}
                                        Pontuação do jogador 2, {self.nomeJogador2Atual}: {str(pontosJogador2)}
                                        """)
            db.criarJogada(self.id_jogador1Atual, self.id_jogador2Atual, self.id_jogador1Atual, pontosJogador1, pontosJogador2, rodadas[0], rodadas[1], rodadas[2])
            
        else:
            self.jogadorGanhador.setText(f"O jogador 2, {self.nomeJogador1Atual}, ganhou o jogo!")
            self.pontuacaoFim.setText(f"""Pontuação do jogador 1, {self.nomeJogador1Atual}: {str(pontosJogador1)}
                                        Pontuação do jogador 2, {self.nomeJogador2Atual}: {str(pontosJogador2)}
                                        """)

            db.criarJogada(self.id_jogador1Atual, self.id_jogador2Atual, self.id_jogador2Atual, pontosJogador1, pontosJogador2, rodadas[0], rodadas[1], rodadas[2])

        db.close_connection()

        
            



if __name__=="__main__":
    app = QApplication()
    windows = MainWindow()
    windows.show()
    app.exec()