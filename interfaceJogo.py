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
        MainWindow.resize(415, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.pageModo1 = QWidget()
        self.pageModo1.setObjectName(u"pageModo1")
        self.frame_14 = QFrame(self.pageModo1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(30, 3, 331, 361))
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
        self.frame.setGeometry(QRect(10, 0, 350, 424))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_18 = QLabel(self.frame_23)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_6.addWidget(self.label_18)

        self.nomeJogador_2 = QLabel(self.frame_23)
        self.nomeJogador_2.setObjectName(u"nomeJogador_2")

        self.horizontalLayout_6.addWidget(self.nomeJogador_2)


        self.verticalLayout.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_24)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_28 = QLabel(self.frame_25)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_7.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_25)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_7.addWidget(self.label_29)


        self.verticalLayout_5.addWidget(self.frame_25)

        self.frame_32 = QFrame(self.frame_24)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_42 = QLabel(self.frame_32)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_14.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_32)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_14.addWidget(self.label_43)


        self.verticalLayout_5.addWidget(self.frame_32)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_30 = QLabel(self.frame_26)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_8.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_26)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_8.addWidget(self.label_31)


        self.verticalLayout_5.addWidget(self.frame_26)

        self.frame_31 = QFrame(self.frame_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_40 = QLabel(self.frame_31)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_13.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_31)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_13.addWidget(self.label_41)


        self.verticalLayout_5.addWidget(self.frame_31)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_32 = QLabel(self.frame_27)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_9.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_27)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_9.addWidget(self.label_33)


        self.verticalLayout_5.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.frame_24)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_36 = QLabel(self.frame_29)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_11.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_29)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_11.addWidget(self.label_37)


        self.verticalLayout_5.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_10.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_10.addWidget(self.label_35)


        self.verticalLayout_5.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.frame_24)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_38 = QLabel(self.frame_30)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_12.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_30)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_12.addWidget(self.label_39)


        self.verticalLayout_5.addWidget(self.frame_30)


        self.verticalLayout.addWidget(self.frame_24)

        self.voltarHistorico = QPushButton(self.frame)
        self.voltarHistorico.setObjectName(u"voltarHistorico")

        self.verticalLayout.addWidget(self.voltarHistorico)

        self.Pages.addWidget(self.pagHistorico)
        self.procuraCadastro = QWidget()
        self.procuraCadastro.setObjectName(u"procuraCadastro")
        self.frame_21 = QFrame(self.procuraCadastro)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(40, 20, 321, 341))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_21)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_25 = QLabel(self.frame_21)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_3.addWidget(self.label_25)

        self.label_27 = QLabel(self.frame_21)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_3.addWidget(self.label_27)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_26 = QLabel(self.frame_22)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_4.addWidget(self.label_26)

        self.nomeJogador = QLineEdit(self.frame_22)
        self.nomeJogador.setObjectName(u"nomeJogador")

        self.horizontalLayout_4.addWidget(self.nomeJogador)


        self.verticalLayout_3.addWidget(self.frame_22)

        self.procurarJogado = QPushButton(self.frame_21)
        self.procurarJogado.setObjectName(u"procurarJogado")

        self.verticalLayout_3.addWidget(self.procurarJogado)

        self.voltarHistorico_2 = QPushButton(self.frame_21)
        self.voltarHistorico_2.setObjectName(u"voltarHistorico_2")

        self.verticalLayout_3.addWidget(self.voltarHistorico_2)

        self.Pages.addWidget(self.procuraCadastro)
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

        self.sair = QPushButton(self.frame_2)
        self.sair.setObjectName(u"sair")

        self.verticalLayout_4.addWidget(self.sair)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.Pages.addWidget(self.pagHome)
        self.iniciar_config = QWidget()
        self.iniciar_config.setObjectName(u"iniciar_config")
        self.frame_15 = QFrame(self.iniciar_config)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 401, 361))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_16.addWidget(self.label_19)

        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_16.addWidget(self.label_20)

        self.iniciar = QPushButton(self.frame_15)
        self.iniciar.setObjectName(u"iniciar")

        self.verticalLayout_16.addWidget(self.iniciar)

        self.Pages.addWidget(self.iniciar_config)
        self.cadastroDoisJogares = QWidget()
        self.cadastroDoisJogares.setObjectName(u"cadastroDoisJogares")
        self.frame_3 = QFrame(self.cadastroDoisJogares)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(29, 11, 341, 351))
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
        self.frame_7.setGeometry(QRect(0, -2, 391, 371))
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
        self.frame_8.setGeometry(QRect(10, 6, 381, 371))
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
        self.frame_9.setGeometry(QRect(0, 13, 391, 361))
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
        self.frame_10.setGeometry(QRect(0, 0, 391, 371))
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
        self.erroConfiguracao = QWidget()
        self.erroConfiguracao.setObjectName(u"erroConfiguracao")
        self.frame_16 = QFrame(self.erroConfiguracao)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(30, 30, 341, 321))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_17.addWidget(self.label_21)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_17.addItem(self.verticalSpacer_8)

        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_17.addWidget(self.label_22)

        self.Pages.addWidget(self.erroConfiguracao)
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
        self.jogoComecar = QWidget()
        self.jogoComecar.setObjectName(u"jogoComecar")
        self.frame_19 = QFrame(self.jogoComecar)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(10, 10, 361, 371))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_19)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_23 = QLabel(self.frame_20)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_21.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_21.addWidget(self.label_24)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_21.addItem(self.verticalSpacer_10)

        self.comecarJogo = QPushButton(self.frame_20)
        self.comecarJogo.setObjectName(u"comecarJogo")

        self.verticalLayout_21.addWidget(self.comecarJogo)

        self.voltarMenu_2 = QPushButton(self.frame_20)
        self.voltarMenu_2.setObjectName(u"voltarMenu_2")

        self.verticalLayout_21.addWidget(self.voltarMenu_2)


        self.verticalLayout_20.addWidget(self.frame_20)

        self.Pages.addWidget(self.jogoComecar)
        self.jogoAndamento = QWidget()
        self.jogoAndamento.setObjectName(u"jogoAndamento")
        self.frame_12 = QFrame(self.jogoAndamento)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(9, -1, 361, 371))
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
        self.ganhouJogador = QWidget()
        self.ganhouJogador.setObjectName(u"ganhouJogador")
        self.frame_17 = QFrame(self.ganhouJogador)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(20, 10, 351, 361))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.jogadorGanhador = QLabel(self.frame_18)
        self.jogadorGanhador.setObjectName(u"jogadorGanhador")

        self.verticalLayout_19.addWidget(self.jogadorGanhador)

        self.pontuacaoFim1 = QLabel(self.frame_18)
        self.pontuacaoFim1.setObjectName(u"pontuacaoFim1")

        self.verticalLayout_19.addWidget(self.pontuacaoFim1)

        self.pontuacaoFim2 = QLabel(self.frame_18)
        self.pontuacaoFim2.setObjectName(u"pontuacaoFim2")

        self.verticalLayout_19.addWidget(self.pontuacaoFim2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_19.addItem(self.verticalSpacer_9)

        self.telaDePreparo = QPushButton(self.frame_18)
        self.telaDePreparo.setObjectName(u"telaDePreparo")

        self.verticalLayout_19.addWidget(self.telaDePreparo)

        self.telaDeCadastrar = QPushButton(self.frame_18)
        self.telaDeCadastrar.setObjectName(u"telaDeCadastrar")

        self.verticalLayout_19.addWidget(self.telaDeCadastrar)

        self.voltarMenu_3 = QPushButton(self.frame_18)
        self.voltarMenu_3.setObjectName(u"voltarMenu_3")

        self.verticalLayout_19.addWidget(self.voltarMenu_3)


        self.verticalLayout_18.addWidget(self.frame_18)

        self.Pages.addWidget(self.ganhouJogador)

        self.horizontalLayout_5.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 415, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Staying Alive</span></p></body></html>", None))
        self.doisJogadores.setText(QCoreApplication.translate("MainWindow", u"2 Jogadores", None))
        self.tutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.voltarHome.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Hist\u00f3rico do jogador: </span></p></body></html>", None))
        self.nomeJogador_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nome_jogador</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.voltarHistorico.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Procura de Hist\u00f3rico</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Procure os status do jogador pelo o seu nome!</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Nome Registrado:", None))
        self.procurarJogado.setText(QCoreApplication.translate("MainWindow", u"Procurar Jogador", None))
        self.voltarHistorico_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Staying Alive</span></p></body></html>", None))
        self.jogoModo1.setText(QCoreApplication.translate("MainWindow", u"Jogar", None))
        self.sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Configura\u00e7\u00e3o do ambiente</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Aperte o bot\u00e3o&quot; iniciar&quot; para configurar </p><p align=\"center\">o ambiente e iniciar o jogo</p></body></html>", None))
        self.iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cadastro dos Jogares</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Jogador 1:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Jogador 2:", None))
        self.cadastrarDoisJogadores.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cancelarCadModo1.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Configurando o ambiente...</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Jogador 1: Fique na frente</p><p align=\"center\">do sensor ultrassonico.</p></body></html>", None))
        self.cancelar_conf1.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Configurando o ambiente...</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Jogador 1: Fique na frente na frente </p><p align=\"center\">do sensor ultrassonico.</p></body></html>", None))
        self.cancelar_conf2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Jogador 1 posicionado</span></p><p align=\"center\"><span style=\" font-size:14pt;\">corretamente!</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Prossiga com o pr\u00f3ximo usu\u00e1rio </p><p align=\"center\">para o seu posicionamento.</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Jogador 2 posicionado</span></p><p align=\"center\"><span style=\" font-size:14pt;\">corretamente!</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Prepare para o as instru\u00e7\u00f5es do jogo.</p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Erro no posicionamento </span></p><p align=\"center\"><span style=\" font-size:14pt;\">dos jogadores!</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Houve um erro no posicionamento dos jogadores. </p><p align=\"center\">Posicionamento ir\u00e1 ser reiniciado.</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Instru\u00e7\u00f5es</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Para iniciar o jogo, cada jogador deve se posicionar </p><p align=\"center\">conforme as instru\u00e7\u00f5es do dispositivo, sempre ficando </p><p align=\"center\">com cerca de 2 metros na dire\u00e7\u00e3o do sensor ultrass\u00f4nico.</p><p align=\"center\">Enquanto a m\u00fasica toca, o dispositivo ficar\u00e1 oscilando </p><p align=\"center\">entre os usu\u00e1rio verificando se eles est\u00e3o dan\u00e7ando. </p><p align=\"center\">Caso negativo, o usu\u00e1rio que n\u00e3o estiver dan\u00e7ando perder\u00e1, </p><p align=\"center\">fazendo com que o oponente ganhe 10 pontos.</p><p align=\"center\">Ap\u00f3s isso, a musica parar\u00e1 repedinamente </p><p align=\"center\">e o sensor ultrass\u00f4nico verificar\u00e1 se o jogador </p><p align=\"center\">est\u00e1 morto (abaixado) ou vivo (levantado).</p></body></html>", None))
        self.voltarModo1.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogo j\u00e1 vai come\u00e7ar!</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Dance enquanto a musica tocar,</p><p align=\"center\">fique parado quando a musica parar.</p><p align=\"center\">Quando o buzzer tocar, abaixe se o </p><p align=\"center\">mestre estiver olhando para voc\u00ea.</p></body></html>", None))
        self.comecarJogo.setText(QCoreApplication.translate("MainWindow", u"Come\u00e7ar o Jogo", None))
        self.voltarMenu_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogo j\u00e1 come\u00e7ou!</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Dance enquanto a musica tocar,</p><p align=\"center\">fique parado quando a musica parar.</p><p align=\"center\">Quando o buzzer tocar, abaixe se o </p><p align=\"center\">mestre estiver olhando para voc\u00ea.</p></body></html>", None))
        self.pausarJogo.setText(QCoreApplication.translate("MainWindow", u"Pausar o Jogo", None))
        self.voltarMenu.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.jogadorGanhador.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogador 1 ganhou!</span></p></body></html>", None))
        self.pontuacaoFim1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Pontua\u00e7\u00e3o do jogador 1, :</p></body></html>", None))
        self.pontuacaoFim2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Pontua\u00e7\u00e3o do jogador2, :</p></body></html>", None))
        self.telaDePreparo.setText(QCoreApplication.translate("MainWindow", u"Recome\u00e7ar com os mesmos participantes", None))
        self.telaDeCadastrar.setText(QCoreApplication.translate("MainWindow", u"Recome\u00e7ar com novos participantes", None))
        self.voltarMenu_3.setText(QCoreApplication.translate("MainWindow", u"Voltar ao Menu", None))
    # retranslateUi

