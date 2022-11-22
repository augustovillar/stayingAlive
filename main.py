from PySide6.QtWidgets import *
from interfaceJogo import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stayling Alive")
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
        self.cadastrarDoisJogadores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.configuracao1))
        self.cancelarCadModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #configurando player 1
        self.cancelar_conf1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))
        
        #configurando player 2
        self.cancelarCadModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #tutorial
        self.voltarModo1.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))

        #historico
        self.voltarHistorico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pageModo1))


        

        
        


if __name__=="__main__":
    app = QApplication()
    windows = MainWindow()
    windows.show()
    app.exec()