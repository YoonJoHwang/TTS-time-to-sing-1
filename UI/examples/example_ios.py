#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #
import sys
import yaml
sys.path.append("../pyqt5Custom")
sys.path.append("../bridge")
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase, QIcon
from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast

import Make_new_song, Model_training
from config_data_input import *
from config_parser import Config
from progressbar import Progressbar

class MainWindow(QDialog):
    def __init__(self):
        # widget = QtWidgets.QStackedWidget()
        super(MainWindow, self).__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")
        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.conlyt = QVBoxLayout()
        self.conlyt.setSpacing(0)
        self.conlyt.setContentsMargins(70, 15, 70, 0)
        self.layout.addLayout(self.conlyt)
        self.ibtnlyt = ImageBox(source="data/tts.png")
        self.layout.addWidget(self.ibtnlyt, alignment=Qt.AlignHCenter | Qt.AlignCenter)

        h = QLabel("<span style='font-size:60px; font-family:SF Pro Display; color:rgb(28,28,30);'>\U0001F5A5 Time To Sing </span>")

        ah = QLabel(
            "<span style='font-size:25px; font-family:SF Pro Display; color:rgb(89,89,92);'>노래하는 TTS program</span>")


        h.setContentsMargins(140, 0, 0, 0)
        ah.setContentsMargins(240, 0, 0, 0)
        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)
        self.conlyt.addSpacing(90)

        """
        self.ibtnlyt = ImageBox(source="data/tts.png")
        self.layout.addWidget(self.ibtnlyt, alignment=Qt.AlignTop | Qt.AlignTop)
        """

        self.btnslyt = QHBoxLayout()
        self.conlyt.addLayout(self.btnslyt)

        self.btnlyt = QHBoxLayout()
        self.btnlyt.setSpacing(110)

        self.btnslyt.addLayout(self.btnlyt)

        self.btnlyt2 = QVBoxLayout()
        self.btnslyt.addLayout(self.btnlyt2)

        self.btn2 = StyledButton("Model Training")
        self.btn2.setFixedSize(170, 54)
        self.btn2.anim_press.speed = 7.3

        self.btn2.setStyleDict({
            "background-color": (0, 0, 0),
            "border-color": (0, 0, 0),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21,
        })
        self.btn2.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 0, 0),
            "color": (0, 0, 0),
        }, "hover")
        self.btn2.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 0, 0),
            "color": (0, 0, 0),
        }, "press")
        self.btn2.clicked.connect(lambda: switchWidget(1)) #
        self.btnlyt.addWidget(self.btn2, alignment=Qt.AlignBottom | Qt.AlignHCenter)

        self.btn1 = StyledButton("Generate Song")
        self.btn1.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn1.setStyleDict({
            "background-color": (0, 0, 0),
            "border-color": (0, 0, 0),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21,
        })
        self.btn1.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 0, 0),
            "color": (0, 0, 0),
        }, "hover")
        self.btn1.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 0, 0),
            "color": (0, 0, 0),
        }, "press")

        self.btn1.clicked.connect(lambda: switchWidget(2))
        self.btnlyt.addWidget(self.btn1, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

def switchWidget(num):
    global wg
    wg.setCurrentIndex(num)

if __name__ == "__main__":

    sys.path.append('../pyqt5Custom')
    app = QApplication(sys.argv)
    wg = QtWidgets.QStackedWidget()
    wg.setWindowTitle("Sogang and SmileGate")
    wg.setWindowIcon(QIcon('TTS.png'))
    wg.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

    mw = MainWindow() # index [0]
    wg.addWidget(mw)

    pb1 = Progressbar(switchWidget) # index [3]

    ml = Model_training.Model_training(switchWidget, pb1) # index [1]
    wg.addWidget(ml)

    ns = Make_new_song.Make_new_song(switchWidget, pb1) # index [2]
    wg.addWidget(ns)

    wg.addWidget(pb1)

    wg.setFixedHeight(800)
    wg.setFixedWidth(1200)

    switchWidget(0)
    wg.show()

    sys.exit(app.exec_())
