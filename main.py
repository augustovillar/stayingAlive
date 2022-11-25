from PySide6.QtWidgets import *
from interfaceJogo import Ui_MainWindow
import sys
from database import Data_base
import serial
import time


class MainWindow(QMainWindow, Ui_MainWindow):

    id_jogador1Atual = ""
    id_jogador2Atual = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stayling Alive")
        ser = serial.Serial('COM5', baudrate=115200, bytesize=7, stopbits=2, parity='E')
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

        #Aguardando comando iniciar
        self.iniciar.clicked.connect(self.iniciar_uc)

        #configurando player 1
        self.cancelar_conf1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        
        #configurando player 2
        self.cancelarCadModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #tutorial
        self.voltarModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #historico
        self.voltarHistorico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        ########################################################################################

        self.cadastrarDoisJogadores.clicked.connect(self.cadastrarUsuarios)


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

        self.jogador1.setText('')
        self.jogador2.setText('')

        self.Pages.setCurrentWidget(self.iniciar_config)

    def iniciar_uc(self):

    def posicionamento_pessoa1(self):
        #    '120,200#'
        return




if __name__=="__main__":
    app = QApplication()
    windows = MainWindow()
    windows.show()
    app.exec()