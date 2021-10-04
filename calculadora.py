from PyQt5.QtWidgets import QMainWindow, QApplication, QUndoStack
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("programacion_II/clase4/calculadoranew.ui", self)
            # self.backup.textChanged.connect(self.agregar_digito)
        self.botonC.clicked.connect(self.limpiarDisplay)
        self.boton_.clicked.connect(lambda:self.setDisplayText("0"))
        self.boton_Punto.clicked.connect(self.puntos)
        self.botonMas.clicked.connect(self.sumar)
        self.botonMenos.clicked.connect(self.restar)
        self.botonMulti.clicked.connect(self.multiplicacion)
        self.botonDivi.clicked.connect(lambda:self.setDisplayText("/"))
        self.botonPorcen.clicked.connect(lambda:self.setDisplayText("%"))
        self.botonPoten.clicked.connect(lambda:self.setDisplayText("**"))
        self.botonPIzquierdo.clicked.connect(lambda:self.setDisplayText("("))
        self.botonPDerecho.clicked.connect(lambda:self.setDisplayText(")"))
        self.boton_1.clicked.connect(lambda:self.setDisplayText("1"))
        self.boton_2.clicked.connect(lambda:self.setDisplayText("2"))
        self.boton_3.clicked.connect(lambda:self.setDisplayText("3"))
        self.boton_4.clicked.connect(lambda:self.setDisplayText("4"))
        self.boton_5.clicked.connect(lambda:self.setDisplayText("5"))
        self.boton_6.clicked.connect(lambda:self.setDisplayText("6"))
        self.boton_7.clicked.connect(lambda:self.setDisplayText("7"))
        self.boton_8.clicked.connect(lambda:self.setDisplayText("8"))
        self.boton_9.clicked.connect(lambda:self.setDisplayText("9"))
        self.botonX.clicked.connect(self.borrarDigito)
        # self.derecha.clicked.connect(self.moverseDerecha)
        # self.izquierda.clicked.connect(self.moverseIzquierda)
        self.botonResultado.clicked.connect(self.resultado)
        # self.botonResu.clicked.connect()
        self.historial.clicked.connect(self.on_click)
        self.expresiones = ''
        self.numA = ''
        # if '+' in self.expresiones:
        #     for dig in self.expresiones:
        #         if dig == "+":
        #             break
        #         self.numA += dig
        #         print(self.numA)

    def sumar(self):

        if "+" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)
        if '-' in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)    
        if "*" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))            
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)

        self.setDisplayText("+")

    def restar(self):
        if "-" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)

        if "+" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)
        if "*" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))            
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)

        self.setDisplayText("-")
    
    def multiplicacion(self):
        if "-" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))            
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)

        if "+" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))            
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)

        if "*" in self.expresiones:
            igual = eval(self.expresiones)
            self.historial.addItem(self.expresiones + ' = ' + str(igual))            
            self.expresiones = str(igual)
            self.display.setText(self.expresiones)

        self.setDisplayText("*")



    def puntos(self):
        if self.expresiones == '' or self.expresiones == '0':
            self.setDisplayText("0.")
        else:
            self.setDisplayText(".")





    def on_click(self):
        print(self.historial.currentItem().text())
        HistoryOP = self.historial.currentItem().text()
        expresion = ''
        for dig in HistoryOP:
            if dig == " ":
                break
            expresion += dig
        self.expresiones = expresion
        self.display.setText(expresion)

    def resultado(self):
        try:
            igual = eval(self.expresiones)
            self.display.setText(str(igual))
            self.historial.addItem(self.expresiones + ' = ' + str(igual))
            # self.expresiones = ''
        except:
            self.display.setText("ERROR")
            # self.expresiones = ''


    def moverseDerecha(self):
        self.display.setSelection(self.display.cursorPosition(), 1)

    def moverseIzquierda(self):
        self.display.setSelection(self.display.cursorPosition(), -1)


        

    def limpiarDisplay(self):
        self.display.clear()
        self.expresiones = ''

    def borrarDigito(self):
        self.display.backspace()
        self.display.setFocus()
        self.expresiones = self.display.text()
        # self.display.setText(self.expresiones)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
        self.expresiones = self.expresiones + self.display.text()

        self.display.setText(self.expresiones)





app = QApplication([])
win = MiVentana()
win.show()
app.exec_()