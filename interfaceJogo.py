# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceJogo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(405, 446)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.pageModo1 = QWidget()
        self.pageModo1.setObjectName(u"pageModo1")
        self.frame_14 = QFrame(self.pageModo1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(30, 3, 331, 381))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_15.addWidget(self.label_2)

        self.doisJogadores = QPushButton(self.frame_14)
        self.doisJogadores.setObjectName(u"doisJogadores")

        self.verticalLayout_15.addWidget(self.doisJogadores)

        self.tutorial = QPushButton(self.frame_14)
        self.tutorial.setObjectName(u"tutorial")

        self.verticalLayout_15.addWidget(self.tutorial)

        self.historico = QPushButton(self.frame_14)
        self.historico.setObjectName(u"historico")

        self.verticalLayout_15.addWidget(self.historico)

        self.voltarHome = QPushButton(self.frame_14)
        self.voltarHome.setObjectName(u"voltarHome")

        self.verticalLayout_15.addWidget(self.voltarHome)

        self.Pages.addWidget(self.pageModo1)
        self.pagHistorico = QWidget()
        self.pagHistorico.setObjectName(u"pagHistorico")
        self.pagHistorico.setEnabled(True)
        self.frame = QFrame(self.pagHistorico)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 10, 321, 341))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.voltarHistorico = QPushButton(self.frame)
        self.voltarHistorico.setObjectName(u"voltarHistorico")

        self.verticalLayout.addWidget(self.voltarHistorico)

        self.Pages.addWidget(self.pagHistorico)
        self.pagHome = QWidget()
        self.pagHome.setObjectName(u"pagHome")
        self.verticalLayout_2 = QVBoxLayout(self.pagHome)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.pagHome)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.jogoModo1 = QPushButton(self.frame_2)
        self.jogoModo1.setObjectName(u"jogoModo1")

        self.verticalLayout_4.addWidget(self.jogoModo1)

        self.jogoModo2 = QPushButton(self.frame_2)
        self.jogoModo2.setObjectName(u"jogoModo2")

        self.verticalLayout_4.addWidget(self.jogoModo2)

        self.sair = QPushButton(self.frame_2)
        self.sair.setObjectName(u"sair")

        self.verticalLayout_4.addWidget(self.sair)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.Pages.addWidget(self.pagHome)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Pages.addWidget(self.page_2)
        self.cadastroDoisJogares = QWidget()
        self.cadastroDoisJogares.setObjectName(u"cadastroDoisJogares")
        self.frame_3 = QFrame(self.cadastroDoisJogares)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(29, 11, 261, 221))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.jogador1 = QLineEdit(self.frame_4)
        self.jogador1.setObjectName(u"jogador1")

        self.horizontalLayout.addWidget(self.jogador1)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.jogador2 = QLineEdit(self.frame_5)
        self.jogador2.setObjectName(u"jogador2")

        self.horizontalLayout_2.addWidget(self.jogador2)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cadastrarDoisJogadores = QPushButton(self.frame_6)
        self.cadastrarDoisJogadores.setObjectName(u"cadastrarDoisJogadores")

        self.horizontalLayout_3.addWidget(self.cadastrarDoisJogadores)

        self.cancelarCadModo1 = QPushButton(self.frame_6)
        self.cancelarCadModo1.setObjectName(u"cancelarCadModo1")

        self.horizontalLayout_3.addWidget(self.cancelarCadModo1)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.Pages.addWidget(self.cadastroDoisJogares)
        self.configuracao1 = QWidget()
        self.configuracao1.setObjectName(u"configuracao1")
        self.frame_7 = QFrame(self.configuracao1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, -2, 321, 231))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.cancelar_conf1 = QPushButton(self.frame_7)
        self.cancelar_conf1.setObjectName(u"cancelar_conf1")

        self.verticalLayout_7.addWidget(self.cancelar_conf1)

        self.Pages.addWidget(self.configuracao1)
        self.configuracao2 = QWidget()
        self.configuracao2.setObjectName(u"configuracao2")
        self.frame_8 = QFrame(self.configuracao2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 6, 311, 221))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.cancelar_conf2 = QPushButton(self.frame_8)
        self.cancelar_conf2.setObjectName(u"cancelar_conf2")

        self.verticalLayout_8.addWidget(self.cancelar_conf2)

        self.Pages.addWidget(self.configuracao2)
        self.sucesso1 = QWidget()
        self.sucesso1.setObjectName(u"sucesso1")
        self.frame_9 = QFrame(self.sucesso1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 13, 321, 221))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)

        self.Pages.addWidget(self.sucesso1)
        self.sucesso2 = QWidget()
        self.sucesso2.setObjectName(u"sucesso2")
        self.frame_10 = QFrame(self.sucesso2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 0, 321, 221))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_10.addWidget(self.label_12)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_10.addWidget(self.label_13)

        self.Pages.addWidget(self.sucesso2)
        self.instrucoesTutorial = QWidget()
        self.instrucoesTutorial.setObjectName(u"instrucoesTutorial")
        self.verticalLayout_12 = QVBoxLayout(self.instrucoesTutorial)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_11 = QFrame(self.instrucoesTutorial)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_11.addWidget(self.label_14)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_11.addWidget(self.label_15)

        self.voltarModo1 = QPushButton(self.frame_11)
        self.voltarModo1.setObjectName(u"voltarModo1")

        self.verticalLayout_11.addWidget(self.voltarModo1)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.Pages.addWidget(self.instrucoesTutorial)
        self.jogoAndamento = QWidget()
        self.jogoAndamento.setObjectName(u"jogoAndamento")
        self.frame_12 = QFrame(self.jogoAndamento)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(9, -1, 371, 381))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_13.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_13.addWidget(self.label_17)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.pausarJogo = QPushButton(self.frame_13)
        self.pausarJogo.setObjectName(u"pausarJogo")

        self.verticalLayout_13.addWidget(self.pausarJogo)

        self.voltarMenu = QPushButton(self.frame_13)
        self.voltarMenu.setObjectName(u"voltarMenu")

        self.verticalLayout_13.addWidget(self.voltarMenu)


        self.verticalLayout_14.addWidget(self.frame_13)

        self.Pages.addWidget(self.jogoAndamento)

        self.verticalLayout_5.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 405, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Staying Alive</span></p></body></html>", None))
        self.doisJogadores.setText(QCoreApplication.translate("MainWindow", u"2 Jogadores", None))
        self.tutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.voltarHome.setText(QCoreApplication.translate("MainWindow", u"Outros", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Hist\u00f3rico</span></p></body></html>", None))
        self.voltarHistorico.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Staying Alive</p></body></html>", None))
        self.jogoModo1.setText(QCoreApplication.translate("MainWindow", u"Modo 1", None))
        self.jogoModo2.setText(QCoreApplication.translate("MainWindow", u"Modo 2", None))
        self.sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastro dos Jogares</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Jogador 1:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Jogador 2:", None))
        self.cadastrarDoisJogadores.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cancelarCadModo1.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Configurando o ambiente...</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Jogador 1: Fique na frente na frente </p><p align=\"center\">do sensor ultrassonico.</p></body></html>", None))
        self.cancelar_conf1.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Configurando o ambiente...</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Jogador 1: Fique na frente na frente </p><p align=\"center\">do sensor ultrassonico.</p></body></html>", None))
        self.cancelar_conf2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Jogador 1 posicionado</span></p><p align=\"center\"><span style=\" font-size:14pt;\">corretamente!</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Prossiga com o pr\u00f3ximo usu\u00e1rio </p><p align=\"center\">para o seu posicionamento.</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Jogador 2 posicionado</span></p><p align=\"center\"><span style=\" font-size:14pt;\">corretamente!</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Prepare para o as instru\u00e7\u00f5es do jogo.</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Instru\u00e7\u00f5es</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Para iniciar o jogo, cada jogador deve se posicionar </p><p align=\"center\">conforme as instru\u00e7\u00f5es do dispositivo, sempre ficando </p><p align=\"center\">com cerca de 2 metros na dire\u00e7\u00e3o do sensor ultrass\u00f4nico.</p><p align=\"center\">Enquanto a m\u00fasica toca, o dispositivo ficar\u00e1 oscilando </p><p align=\"center\">entre os usu\u00e1rio verificando se eles est\u00e3o dan\u00e7ando. </p><p align=\"center\">Caso negativo, o usu\u00e1rio que n\u00e3o estiver dan\u00e7ando perder\u00e1, </p><p align=\"center\">fazendo com que o oponente ganhe 10 pontos.</p><p align=\"center\">Ap\u00f3s isso, a musica parar\u00e1 repedinamente </p><p align=\"center\">e o sensor ultrass\u00f4nico verificar\u00e1 se o jogador </p><p align=\"center\">est\u00e1 morto (abaixado) ou vivo (levantado).</p></body></html>", None))
        self.voltarModo1.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogo j\u00e1 come\u00e7ou!</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Quando a m\u00fasica parar, voc\u00ea deve se </p><p align=\"center\">atentar ao buzzer: quando ele tocar, </p><p align=\"center\">o dispositivo far\u00e1 a verifica\u00e7\u00e3o de se </p><p align=\"center\">os jogadores estar\u00e3o mortos ou vivos.</p></body></html>", None))
        self.pausarJogo.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
        self.voltarMenu.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

