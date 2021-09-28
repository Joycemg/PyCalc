from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
            # self.backup.textChanged.connect(self.agregar_digito)
        self.botonC.clicked.connect(self.limpiarDisplay)
        self.boton0.clicked.connect(lambda:self.setDisplayText("0"))
        self.boton00.clicked.connect(lambda:self.setDisplayText("00"))
        self.botonPunto.clicked.connect(lambda:self.setDisplayText("."))
        self.botonSuma.clicked.connect(lambda:self.setDisplayText("+"))
        self.botonMenos.clicked.connect(lambda:self.setDisplayText("-"))
        self.botonMulti.clicked.connect(lambda:self.setDisplayText("×"))
        self.botonDivision.clicked.connect(lambda:self.setDisplayText("÷"))
        self.boton1.clicked.connect(lambda:self.setDisplayText("-"))
        self.boton1.clicked.connect(lambda:self.setDisplayText("1"))
        self.boton2.clicked.connect(lambda:self.setDisplayText("2"))
        self.boton3.clicked.connect(lambda:self.setDisplayText("3"))
        self.boton4.clicked.connect(lambda:self.setDisplayText("4"))
        self.boton5.clicked.connect(lambda:self.setDisplayText("5"))
        self.boton6.clicked.connect(lambda:self.setDisplayText("6"))
        self.boton7.clicked.connect(lambda:self.setDisplayText("7"))
        self.boton8.clicked.connect(lambda:self.setDisplayText("8"))
        self.boton9.clicked.connect(lambda:self.setDisplayText("9"))

    def limpiarDisplay(self):
        self.display.setText('')
        self.display.setFocus()

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def agregar_digito(self):
        self.Calculo.setText(self.Calculo.text() + self.backup.text())



app = QApplication([])
win = MiVentana()
win.show()
app.exec_()