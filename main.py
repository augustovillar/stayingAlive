from PySide6.QtWidgets import *
from PySide6.QtCore import *
from interfaceJogo import Ui_MainWindow
import sys
from database import Data_base
import serial
import time
from deteccaoMovimento import detectaMov
from musica import tocaMusica, paraMusica
import random
from morto_vivo import posicionamento_mortoVivo
import logging

nameCOM = 'COM5'


class MainWindow(QMainWindow, Ui_MainWindow):

    id_jogador1Atual = ""
    id_jogador2Atual = ""
    nomeJogador1Atual = ""
    nomeJogador2Atual = ""

    ser = ''

    logger = ''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stayling Alive")
        #self.ser = serial.Serial(nameCOM, baudrate=115200, bytesize=7, stopbits=2, parity='E', timeout=4)
        logging.basicConfig(filename='arquivo_de_log.log',
                            filemode='a',
                            level=logging.DEBUG,
                            format="%(asctime)s:%(levelname)s:%(filename)s:%(message)s")

        self.logger = logging.getLogger('root')

        #appIncos = QIcon()

        ###############################
        #Páginas do Sistema
    
        #modo1
        self.doisJogadores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.cadastroDoisJogares))
        self.historico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.procuraCadastro))
        self.tutorial.clicked.connect(lambda: self.Pages.setCurrentWidget(self.instrucoesTutorial))
        self.voltarHome.clicked.connect(self.close)


        #cadastro
        self.cancelarCadModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        self.voltarPosicionamento.clicked.connect(lambda: self.Pages.setCurrentWidget(self.iniciar_config))

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
        
        # self.comecarJogo.clicked.connect(self.escreveJogo)
        self.comecarJogo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.jogoAndamento))
        self.comecarJogo.clicked.connect(self.jogo_modo1)

        self.cadastrarDoisJogadores.clicked.connect(self.cadastrarUsuarios)
        
        #inicia posicionamento do modo 1
        self.iniciar.clicked.connect(self.posicionamento_modo1)

        self.procurarJogado.clicked.connect(self.procuraHistorico)
        self.procuraOutrJogador.clicked.connect(lambda: self.Pages.setCurrentWidget(self.procuraCadastro))
        self.voltarHistorico_2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

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
            self.logger.warning("Jogadores sem nome no cadastro!")
            return

        if jogador1Nome==jogador2Nome:
            dialog = QMessageBox(parent=self, text="Os nomes dos dois jogadores são iguais.")
            dialog.setWindowTitle("Erro no cadastro")
            dialog.exec()
            self.Pages.setCurrentWidget(self.cadastroDoisJogares)
            self.logger.warning("Jogadores com nomes iguais no cadastro!")
            return

        #verifica se existe para assim cadastrar o usuário
        if len(db.verifica_usuario(jogador1Nome))==0:
            jogador1OK = db.cadastrar_usuario(jogador1Nome)
            
        else:
            jogador1OK = "JA"
            
        
        #retorna OK quando cadastro com sucesso
        if jogador1OK=="OK":
            print(f"O Jogador1, {jogador1Nome}, foi cadastrado com sucesso.")
            self.logger.info(f"Jogador 1, {jogador1Nome}, foi cadastrado com sucesso.")
        elif jogador1OK=="JA":
            print(f"O Jogador1, {jogador1Nome}, já está cadastrado.")
            self.logger.info(f"Jogador 1, {jogador1Nome}, ja esta cadastrado.")
        else:
            print(f"O Jogador1, {jogador1Nome}, não foi cadastrado com sucesso.")
            self.logger.error(f"Jogador 1, {jogador1Nome}, nao foi cadastrado com sucesso.")
            dialog = QMessageBox(parent=self, text="O jogador 1 não foi cadastrado com sucesso!")
            dialog.setWindowTitle("Erro no cadastro")
            dialog.exec()
            self.Pages.setCurrentWidget(self.cadastroDoisJogares)
            return
        
        if len(db.verifica_usuario(jogador2Nome))==0:
            jogador2OK = db.cadastrar_usuario(jogador2Nome)
        else:
            jogador2OK = "JA"

        #retorna OK quando cadastro com sucesso
        if jogador2OK=="OK":
            print(f"O Jogador 2, {jogador2Nome}, foi cadastrado com sucesso.")
            self.logger.info(f"Jogador 2, {jogador2Nome}, foi cadastrado com sucesso.")
        elif jogador2OK=="JA":
            print(f"O Jogador 2, {jogador2Nome}, já está cadastrado.")
            self.logger.info(f"Jogador 2, {jogador2Nome}, ja esta cadastrado.")
        else:
            print(f"O Jogador2, {jogador2Nome}, não foi cadastrado com sucesso.")
            self.logger.error(f"Jogador 2, {jogador2Nome}, nao foi cadastrado com sucesso.")
            dialog = QMessageBox(parent=self, text="O jogador 2 não foi cadastrado com sucesso!")
            dialog.setWindowTitle("Erro no cadastro")
            dialog.exec()
            self.Pages.setCurrentWidget(self.cadastroDoisJogares)
            return

        if ((jogador1OK=="OK" or jogador1OK=="JA") and (jogador2OK=="OK" or jogador2OK=="JA")):
            dialog = QMessageBox(parent=self, text='Usuários cadastrados com sucesso!')
            self.logger.info(f"Cadastro realizado com sucesso")
            dialog.setWindowTitle("Cadastro")
            dialog.exec()
        else:
            dialog = QMessageBox(parent=self, text='Usuários não foram cadastrados!')
            self.logger.error(f"Cadastro nao realizado.")
            dialog.setWindowTitle("Cadastro")
            dialog.exec()
            return

        
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
        
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        #escreve o numero para o sensor ir pra posicao do primeiro jogador
        self.ser.write((str(numJogador)).encode('ascii'))
        self.logger.info(f"Envia caracter {str(numJogador)} para a FPGA.")

        timeStart = time.time()
        timeNow = timeStart
        jogadorPosicionado = 0

        if numJogador == 1:
            tocaMusica("jogador1.mp3")
            self.logger.info(f"Toca jogador1.mp3")
        else:
            tocaMusica("jogador2.mp3")
            self.logger.info(f"Toca jogador2.mp3")

        time.sleep(2)

        while timeNow-timeStart <= timeout:
            recebeDados = self.ser.read_until(expected=('#').encode('ascii')).decode('utf-8')
            print(recebeDados)
            if recebeDados[0]=="0" or recebeDados[0]=="1":
                distancia = int(recebeDados[4:7])
            else:
                distancia = int(recebeDados[5:8])
            self.logger.info(f"Distancia encontrada: {str(distancia)}.")
            print(distancia)

            
            if distancia<=120:
                jogadorPosicionado += 1
                tocaMusica("foi.mp3")
                self.logger.info(f"Toca foi.mp3")
            else:
                tocaMusica("puts.mp3")
                self.logger.info(f"Toca puts.mp3")

            time.sleep(1.5)

            if jogadorPosicionado>=2:
                print('Posicionamento do jogador '+str(numJogador)+' feito com sucesso!')
                tocaMusica("posicionamento_efetuado_com_sucesso.mp3")
                self.logger.info(f"Posicionamento do jogador {str(numJogador)} feito com sucesso acionando musica.")
                time.sleep(3.5)
                return 'OK'

            timeNow = time.time()

        print('Posicionamento do jogador '+str(numJogador)+' não foi feita com sucesso!')
        self.logger.warning(f"Posicionamento do jogador {str(numJogador)} nao foi feita com sucesso.")
        return 'TIMEOUT'

    def posicionamento_modo1(self):


        #self.ser.write(('r').encode('ascii'))

        self.ser.write(('L').encode('ascii')) #liga o vhdl
        time.sleep(0.5)
        self.logger.info(f"Envia caracter L para a FPGA.")

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

        tocaMusica("pode_iniciar_o_jogo.mp3")
        self.logger.info(f"Toca musica para iniciar jogo.")
        self.Pages.setCurrentWidget(self.jogoComecar)

        self.ser.write(('d').encode('ascii'))
        self.logger.info(f"Envia o caracter d para a FPGA.")
        self.logger.info(f"Posicionamento efetuado com sucesso.")

        return "SUCESSO"

    def jogo_modo1(self):
        
        continuaJogo = True
        numeroRodadasDancandoTotais = 0
        numeroRodadasDancando = 0
        numeroRodadasParadoEmPeTotais = 0
        numeroRodadasParadoEmPe = 0
        numeroRodadasAbaixandoTotais = 0
        numeroRodadasAbaixando = 0

        
        #self.ser.write(('L').encode('ascii'))
   

        while continuaJogo:
            #numero de rodadas da danca
            maxRodadasDancando = random.randint(1, 2)
            paraEmQualJogador  = random.randint(1, 2)
            tocaMusica("Bee Gees - StayinAlive.mp3")
            time.sleep(1)

            self.logger.info(f"Inicia parte de dançar.")

            while numeroRodadasDancando < maxRodadasDancando and continuaJogo:
                for i in range(1, 3):
            
                    self.ser.write((str(i)).encode('ascii'))
                    if numeroRodadasDancando == 0 and i==1:
                        time.sleep(1)
                    resposta = detectaMov(tempoDeEspera=3)

                    if resposta == 'NOK':
                        if i == 1:
                            jogador1Campeao = False
                            self.logger.info(f"Jogador 2 é o campeão.")
                        else:
                            jogador1Campeao = True
                            self.logger.info(f"Jogador 1 é o campeão.")
                      
                        continuaJogo = False
                        paraMusica()
                        
                        break

                    #aleatoricamente escolhe em qual jogador parar
                    if (paraEmQualJogador==i and maxRodadasDancando-1==numeroRodadasDancando):
                        paraMusica()
                        break

                numeroRodadasDancando += 1

            #desliga sensor
            self.ser.write(('d').encode('ascii'))
            self.logger.info(f"Envia o caracter d para a FPGA.")

            #guarda info para historico
            numeroRodadasDancandoTotais += numeroRodadasDancando 

            if not continuaJogo:
                break
            
            #zera para proxima
            numeroRodadasDancando = 0

            maxRodadasParadoEmPe = random.randint(1, 2)
            paraEmQualJogador = random.randint(1, 2)
            
            paraMusica()
            
            #liga sensor
            self.ser.write(('L').encode('ascii'))
            self.logger.info(f"Envia o caracter L para a FPGA.")
            self.logger.info(f"Inicia parte parada/vivo.")

            while numeroRodadasParadoEmPe < maxRodadasParadoEmPe and continuaJogo:
                for i in range(1, 3):

                    tocaMusica("xuxa_minha_rainha.mp3")
                    
                    time.sleep(1)

                    self.ser.write((str(i)).encode('ascii'))
                    time.sleep(1)
                    
                    resposta = detectaMov(tempoDeEspera=3, parado=True)
                    estado = posicionamento_mortoVivo(self.ser, eMorto=False)

                    if resposta == 'NOK' or estado == "morto":
                        if i == 1:
                            jogador1Campeao = False
                            self.logger.info(f"Jogador 2 é o campeão.")
                        else:
                            jogador1Campeao = True
                            self.logger.info(f"Jogador 1 é o campeão.")

                        continuaJogo = False

                        break
                
                    #aleatoricamente escolhe em qual jogador parar
                    if (paraEmQualJogador==i and maxRodadasParadoEmPe-1==numeroRodadasParadoEmPe):
                        break
                    
                numeroRodadasParadoEmPe += 1

            #desliga sensor
            #self.ser.write(('d').encode('ascii'))

            #guarda info para historico
            numeroRodadasParadoEmPeTotais += numeroRodadasParadoEmPe

            #quebra o while
            if not continuaJogo:
                break
            
            #zera para proxima
            numeroRodadasParadoEmPe = 0
            print("Parte morto!")
            self.logger.info(f"Inicia parte morto.")

            if continuaJogo:
                tocaMusica('no_ceu_tem_pao.mp3')
                time.sleep(0.5)

                #self.ser.write(('L').encode('ascii'))

                #inicia jogo do morto
                posicaoMorto = random.randint(1, 2)
                print(posicaoMorto)
                self.ser.write((str(posicaoMorto)).encode('ascii'))
                self.logger.info(f"Envia o caracter {posicaoMorto} para a FPGA.")
                time.sleep(1)
                estado = posicionamento_mortoVivo(self.ser, eMorto=True)

                if estado == 'vivo':
                    if posicaoMorto == 1:
                        jogador1Campeao = False
                        self.logger.info(f"Jogador 2 é o campeão.")
                    else:
                        jogador1Campeao = True
                        self.logger.info(f"Jogador 1 é o campeão.")

                    continuaJogo = False

                time.sleep(3)

            #soma com o total
            numeroRodadasAbaixandoTotais += numeroRodadasAbaixando

            #soma de rodadas abaixando
            numeroRodadasAbaixando = 0
            
        #contabiliza os pontos

        print("acabou rodada")
        if continuaJogo == False:
            self.ser.write(('d').encode('ascii'))
            self.logger.info(f"Envia o caracter d para a FPGA.")
        rodadas = [numeroRodadasAbaixandoTotais, numeroRodadasDancandoTotais, numeroRodadasParadoEmPeTotais]
        self.logger.info(f"Escreve informações no banco de dados.")
        self.escreveJogo(rodadas, jogador1Campeao)

        if jogador1Campeao:
            tocaMusica("jogador1_voce_ganhou.mp3")
        else:
            tocaMusica("jogador2_voce_ganhou.mp3")

        return

    def escreveJogo(self, rodadas=[1, 2, 3], jogador1Campeao=True):

        pontosEmComum = sum(rodadas)

        if jogador1Campeao:
            pontosJogador1 = pontosEmComum + 10
            pontosJogador2 = pontosEmComum
        else:
            pontosJogador1 = pontosEmComum
            pontosJogador2 = pontosEmComum + 10

        db = Data_base()
        db.connect()

        self.Pages.setCurrentWidget(self.ganhouJogador)
        
        #escreve  informações na pagina final como tambem no banco de dados
        if jogador1Campeao:
            self.jogadorGanhador.setText(f"""<html><head/><body><p align="center"><span style=" font-size:14pt;">O Jogador 1, {self.nomeJogador1Atual}, ganhou!</span></p></body></html>""")
            self.pontuacaoFim1.setText(f"""<html><head/><body><p align="center"><span style=" font-size:10pt;">Pontuação do jogador 1, {self.nomeJogador1Atual}: {str(pontosJogador1)}.</span></p></body></html>)""")
            self.pontuacaoFim1.setText(f"""<html><head/><body><p align="center"><span style=" font-size:10pt;">Pontuação do jogador 2, {self.nomeJogador2Atual}: {str(pontosJogador2)}.</span></p></body></html>""")
            
            db.criarJogada(self.id_jogador1Atual, self.id_jogador2Atual, self.id_jogador1Atual, pontosJogador1, pontosJogador2, rodadas[0], rodadas[1], rodadas[2])
        else:
            self.jogadorGanhador.setText(f"""<html><head/><body><p align="center"><span style=" font-size:14pt;">O Jogador 2, {self.nomeJogador2Atual}, ganhou!</span></p></body></html>""")
            self.pontuacaoFim1.setText(f"""<html><head/><body><p align="center"><span style=" font-size:10pt;">Pontuação do jogador 1, {self.nomeJogador1Atual}: {str(pontosJogador1)}.</span></p></body></html>)""")
            self.pontuacaoFim1.setText(f"""<html><head/><body><p align="center"><span style=" font-size:10pt;">Pontuação do jogador 2, {self.nomeJogador2Atual}: {str(pontosJogador2)}.</span></p></body></html>""")

            db.criarJogada(self.id_jogador1Atual, self.id_jogador2Atual, self.id_jogador2Atual, pontosJogador1, pontosJogador2, rodadas[0], rodadas[1], rodadas[2])

        db.close_connection()

        return

    def procuraHistorico(self):

        db = Data_base()

        db.connect()

        jogadorNome = self.nomeJogador.text().strip()

        if jogadorNome=="":
            dialog = QMessageBox(parent=self, text="Por favor, insira um nome valido.")
            self.logger.warning(f"Nome invalido para buscar no historio.")
            dialog.setWindowTitle("Erro na busca")
            dialog.exec()
            self.Pages.setCurrentWidget(self.procuraCadastro)
            print("Busca sem nome.")
            return

        #retorna o campo para vazio
        self.nomeJogador.setText("")

        try:
            id_jogador = db.verifica_usuario(jogadorNome)[0][0]
        except:
            dialog = QMessageBox(parent=self, text="Jogador não encontrado")
            self.logger.warning(f"Jogador nao encontrado.")
            dialog.setWindowTitle("Erro na busca")
            dialog.exec()
            self.Pages.setCurrentWidget(self.procuraCadastro)
            print("Busca com usuário não encontrado.")
            return
        
        self.logger.info("Procura informacoes dos jogos do jogador selecionado.")
        informacoesEncontradas = db.procuraJogos(id_jogador)

        db.close_connection()

        jogosVitoriosos = 0
        pontosDancando = 0
        pontosParados = 0
        pontosMorto = 0
        totalPontos = 0

        numJogos = len(informacoesEncontradas)

        for jogo in informacoesEncontradas:
            if jogo[3]==id_jogador:
                jogosVitoriosos += 1
                totalPontos += 10

            pontosMorto += jogo[6]
            pontosDancando += jogo[7]
            pontosParados += jogo[8]
            totalPontos = totalPontos + jogo[6] + jogo[7] + jogo[8]
        
        mediaPontos = totalPontos/numJogos

        self.nomeJogador_2.setText(f"""<html><head/><body><p><span style=" font-size:14pt;">{jogadorNome}</span></p></body></html>""")
        
        self.numJogos.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(numJogos)}</span></p></body></html>""")
        self.numJogosVic.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(jogosVitoriosos)}</span></p></body></html>""")
        self.pontosDancando.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(pontosDancando)}</span></p></body></html>""")
        self.pontosParado.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(pontosParados)}</span></p></body></html>""")
        self.pontosMortos.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(pontosMorto)}</span></p></body></html>""")
        self.totalPontos.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(totalPontos)}</span></p></body></html>""")
        self.mediaPontos.setText(f"""<html><head/><body><p><span style=" font-size:9pt;">{str(mediaPontos)}</span></p></body></html>""")

        self.Pages.setCurrentWidget(self.pagHistorico)
        self.logger.info("Informacoes dos jogos do jogador selecionado dispostas.")
        return 

if __name__=="__main__":
    app = QApplication()
    windows = MainWindow()
    windows.show()
    app.exec()