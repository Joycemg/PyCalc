from PyQt5.QtWidgets import QMainWindow, QApplication, QUndoStack
from PyQt5 import uic
import re
import time



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
        self.botonRaiz.clicked.connect(lambda:self.setDisplayText("√"))
        self.botonDivi.clicked.connect(self.division)
        self.botonPorcen.clicked.connect(lambda:self.setDisplayText("%"))
        self.botonPoten.clicked.connect(lambda:self.setDisplayText("²"))
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
        self.botonResultado.clicked.connect(self.resultado)
        self.historial.clicked.connect(self.on_click)
    
        
    def sumar(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()

        self.setDisplayText("+")

    def restar(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()

        self.setDisplayText("-")
    
    def multiplicacion(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()

        self.setDisplayText("×")

    def division(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()
        if self.display.text() == '' or self.display.text() == '0':
            self.display.setText("")
        else:
            self.setDisplayText("÷")


    def puntos(self):
        if self.display.text() == '':
            self.setDisplayText("0,")
        else:
            self.setDisplayText(",")





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
            aux = self.display.text()
            aux = re.sub(r'÷', r'/', aux)
            aux = re.sub(r',', r'.', aux)
            aux = re.sub(r'×', r'*', aux)
            aux = re.sub(r'²', r'**2', aux)
            igual = eval(aux)
            igualStr = str(igual).replace('.', ',')
            self.historial.addItem(self.display.text() + ' = ' + igualStr)
            # if "," in igualStr:
            #     self.display.setText(f'{igual:.2f}'.replace(".", ","))
            # else:
            if type(igual) == float:
                self.display.setText(f'{igual:.3f}'.replace(".", ","))
            else:
                self.display.setText(str(igual))



        except:
            self.display.setText("ERROR")




    def limpiarDisplay(self):
        self.display.clear()
        self.expresiones = ''

    def borrarDigito(self):
        self.display.backspace()
        self.display.setFocus()
        self.expresiones = self.display.text()
        # self.display.setText(self.expresiones)

    def setDisplayText(self, tex):
        if self.display.text() == "ERROR":
            time.sleep(0.2)
            self.display.setText("")
        digito=tex
        self.display.setText(self.display.text()+ digito)
        self.display.setFocus()

        # display = self.display.text()
        # retornar = f'{display:10}'
        # self.display.setText(retornar)

        # self.display.setText(digito+text) 
        # self.display.setFocus()
        # self.expresiones = self.display.text()
#         self.expresiones = self.expresiones + self.display.text()

# 
        # if '+' == digito:
        #     # self.display.setText(self.display.text() + digito) 
        #     self.display.setFocus()
        # else:
        #     display = self.display.text()
        #     retonar = '{:,}'.format(int(display))
        #     # .replace(',','.')
        #     self.display.setText(str(retonar))






app = QApplication([])
win = MiVentana()
win.show()
app.exec_()