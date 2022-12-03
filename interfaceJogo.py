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
        MainWindow.resize(414, 488)
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
        self.frame_14.setGeometry(QRect(0, 3, 391, 421))
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
        self.frame.setGeometry(QRect(-1, 3, 391, 421))
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

        self.numJogos = QLabel(self.frame_25)
        self.numJogos.setObjectName(u"numJogos")

        self.horizontalLayout_7.addWidget(self.numJogos)


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

        self.numJogosVic = QLabel(self.frame_32)
        self.numJogosVic.setObjectName(u"numJogosVic")

        self.horizontalLayout_14.addWidget(self.numJogosVic)


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

        self.pontosDancando = QLabel(self.frame_26)
        self.pontosDancando.setObjectName(u"pontosDancando")

        self.horizontalLayout_8.addWidget(self.pontosDancando)


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

        self.pontosParado = QLabel(self.frame_31)
        self.pontosParado.setObjectName(u"pontosParado")

        self.horizontalLayout_13.addWidget(self.pontosParado)


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

        self.pontosMortos = QLabel(self.frame_27)
        self.pontosMortos.setObjectName(u"pontosMortos")

        self.horizontalLayout_9.addWidget(self.pontosMortos)


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

        self.totalPontos = QLabel(self.frame_29)
        self.totalPontos.setObjectName(u"totalPontos")

        self.horizontalLayout_11.addWidget(self.totalPontos)


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

        self.mediaPontos = QLabel(self.frame_28)
        self.mediaPontos.setObjectName(u"mediaPontos")

        self.horizontalLayout_10.addWidget(self.mediaPontos)


        self.verticalLayout_5.addWidget(self.frame_28)


        self.verticalLayout.addWidget(self.frame_24)

        self.procuraOutrJogador = QPushButton(self.frame)
        self.procuraOutrJogador.setObjectName(u"procuraOutrJogador")

        self.verticalLayout.addWidget(self.procuraOutrJogador)

        self.voltarHistorico = QPushButton(self.frame)
        self.voltarHistorico.setObjectName(u"voltarHistorico")

        self.verticalLayout.addWidget(self.voltarHistorico)

        self.Pages.addWidget(self.pagHistorico)
        self.procuraCadastro = QWidget()
        self.procuraCadastro.setObjectName(u"procuraCadastro")
        self.frame_21 = QFrame(self.procuraCadastro)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(0, 0, 391, 421))
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
        self.iniciar_config = QWidget()
        self.iniciar_config.setObjectName(u"iniciar_config")
        self.frame_15 = QFrame(self.iniciar_config)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 391, 421))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_16.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_16.addWidget(self.label_20, 0, Qt.AlignTop)

        self.iniciar = QPushButton(self.frame_15)
        self.iniciar.setObjectName(u"iniciar")

        self.verticalLayout_16.addWidget(self.iniciar)

        self.Pages.addWidget(self.iniciar_config)
        self.cadastroDoisJogares = QWidget()
        self.cadastroDoisJogares.setObjectName(u"cadastroDoisJogares")
        self.frame_3 = QFrame(self.cadastroDoisJogares)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-1, 1, 391, 421))
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
        self.erroConfiguracao = QWidget()
        self.erroConfiguracao.setObjectName(u"erroConfiguracao")
        self.frame_16 = QFrame(self.erroConfiguracao)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 391, 421))
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

        self.voltarPosicionamento = QPushButton(self.frame_16)
        self.voltarPosicionamento.setObjectName(u"voltarPosicionamento")

        self.verticalLayout_17.addWidget(self.voltarPosicionamento)

        self.Pages.addWidget(self.erroConfiguracao)
        self.instrucoesTutorial = QWidget()
        self.instrucoesTutorial.setObjectName(u"instrucoesTutorial")
        self.frame_11 = QFrame(self.instrucoesTutorial)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(-1, -1, 391, 421))
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

        self.Pages.addWidget(self.instrucoesTutorial)
        self.jogoComecar = QWidget()
        self.jogoComecar.setObjectName(u"jogoComecar")
        self.frame_19 = QFrame(self.jogoComecar)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(0, 0, 391, 421))
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
        self.frame_12.setGeometry(QRect(-1, -1, 391, 421))
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
        self.frame_17.setGeometry(QRect(0, 0, 391, 421))
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
        self.menubar.setGeometry(QRect(0, 0, 414, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Staying Alive</span></p></body></html>", None))
        self.doisJogadores.setText(QCoreApplication.translate("MainWindow", u"Jogar", None))
        self.tutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.historico.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.voltarHome.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Hist\u00f3rico do jogador: </span></p></body></html>", None))
        self.nomeJogador_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nome_jogador</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">N\u00famero de Jogos:</span></p></body></html>", None))
        self.numJogos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">N\u00famero de Jogos Vitoriosos:</span></p></body></html>", None))
        self.numJogosVic.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">Pontos Dan\u00e7ando:</span></p></body></html>", None))
        self.pontosDancando.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">Pontos Parados:</span></p></body></html>", None))
        self.pontosParado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">Pontos Mortos:</span></p></body></html>", None))
        self.pontosMortos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">Total de Pontos:</span></p></body></html>", None))
        self.totalPontos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">M\u00e9dia de Pontos:</span></p></body></html>", None))
        self.mediaPontos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">TextLabel</span></p></body></html>", None))
        self.procuraOutrJogador.setText(QCoreApplication.translate("MainWindow", u"Procurar outro jogador", None))
        self.voltarHistorico.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Procura de Hist\u00f3rico</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Procure os status do jogador pelo o seu nome!</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome Registrado:</span></p></body></html>", None))
        self.procurarJogado.setText(QCoreApplication.translate("MainWindow", u"Procurar Jogador", None))
        self.voltarHistorico_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Posicionamento dos jogadores</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">1 - Aperte o bot\u00e3o abaixo para iniciar a confgura\u00e7\u00e3o </span></p><p align=\"center\"><span style=\" font-size:9pt;\">do posicionamento dos jogadores.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">2 - Ao ser chamado, fique na posi\u00e7\u00e3o indicada pelo mestre.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">3 - Espere o comando de voz avisar</span></p><p align=\"center\"><span style=\" font-size:9pt;\">que voc\u00ea est\u00e1 posicionado corretamente.</span></p></body></html>", None))
        self.iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cadastro dos Jogadores</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Jogador 1:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Jogador 2:</span></p></body></html>", None))
        self.cadastrarDoisJogadores.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cancelarCadModo1.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Erro no posicionamento </span></p><p align=\"center\"><span style=\" font-size:14pt;\">dos jogadores!</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Houve um erro no posicionamento dos jogadores. </span></p><p align=\"center\"><span style=\" font-size:9pt;\">Posicionamento ir\u00e1 ser reiniciado.</span></p></body></html>", None))
        self.voltarPosicionamento.setText(QCoreApplication.translate("MainWindow", u"Voltar para Posicionamento", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Instru\u00e7\u00f5es</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Para iniciar o jogo, cada jogador deve se posicionar </p><p align=\"center\">conforme as instru\u00e7\u00f5es do dispositivo, sempre ficando </p><p align=\"center\">com cerca de 1 metro na dire\u00e7\u00e3o do sensor ultrass\u00f4nico.</p><p align=\"center\">Enquanto a m\u00fasica toca, o dispositivo ficar\u00e1 oscilando </p><p align=\"center\">entre os usu\u00e1rio verificando se eles est\u00e3o dan\u00e7ando. </p><p align=\"center\">Caso negativo, o usu\u00e1rio que n\u00e3o estiver dan\u00e7ando perder\u00e1, </p><p align=\"center\">fazendo com que o oponente ganhe 10 pontos,</p><p align=\"center\">al\u00e9m dos pontos das rodadas. Ap\u00f3s isso, a m\u00fasica</p><p align=\"center\">parar\u00e1 repedinamente e o sensor ultrass\u00f4nico verificar\u00e1</p><p align=\"center\">se o jogador est\u00e1 morto (abaixado) ou vivo (levantado).</p></body></html>", None))
        self.voltarModo1.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogo j\u00e1 vai come\u00e7ar!</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">1 - Dance enquanto a musica estiver tocando!</span></p><p align=\"center\"><span style=\" font-size:9pt;\">2 - Fique parado ao ouvir &quot;est\u00e1tua&quot; de nossa rainha.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">3 - Abaixe-se quando ouvir &quot;morreu&quot;, se o mestre</span></p><p align=\"center\"><span style=\" font-size:9pt;\">estiver olhando para voc\u00ea. Clique em &quot;come\u00e7ar </span></p><p align=\"center\"><span style=\" font-size:9pt;\">o jogo&quot; para iniciar a divers\u00e3o!</span></p></body></html>", None))
        self.comecarJogo.setText(QCoreApplication.translate("MainWindow", u"Come\u00e7ar o Jogo", None))
        self.voltarMenu_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogo j\u00e1 come\u00e7ou!</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">1 - Dance enquanto a musica tocar</span></p><p align=\"center\"><span style=\" font-size:9pt;\">2 - Fique parado ao ouvir &quot;est\u00e1tua&quot; de nossa rainha</span></p><p align=\"center\"><span style=\" font-size:9pt;\">3 - Abaixe-se quando ouvir &quot;morreu&quot;, se o mestre olhar</span></p><p align=\"center\"><span style=\" font-size:9pt;\"> para voc\u00ea. </span></p><p align=\"center\"><span style=\" font-size:9pt;\">Preste aten\u00e7\u00e3o e se diverta!</span></p></body></html>", None))
        self.pausarJogo.setText(QCoreApplication.translate("MainWindow", u"Pausar o Jogo", None))
        self.voltarMenu.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.jogadorGanhador.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">O Jogador X ganhou!</span></p></body></html>", None))
        self.pontuacaoFim1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Pontua\u00e7\u00e3o do jogador 1, :</p></body></html>", None))
        self.pontuacaoFim2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Pontua\u00e7\u00e3o do jogador2, :</p></body></html>", None))
        self.telaDePreparo.setText(QCoreApplication.translate("MainWindow", u"Recome\u00e7ar com os mesmos participantes", None))
        self.telaDeCadastrar.setText(QCoreApplication.translate("MainWindow", u"Recome\u00e7ar com novos participantes", None))
        self.voltarMenu_3.setText(QCoreApplication.translate("MainWindow", u"Voltar ao Menu", None))
    # retranslateUi

