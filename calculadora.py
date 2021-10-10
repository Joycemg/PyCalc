from PyQt5.QtWidgets import QMainWindow, QApplication, QUndoStack
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QFont
import re
import time


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("programacion_II/clase4/calculadoranew.ui", self)
        self.botonC.clicked.connect(self.limpiarDisplay)
        self.boton_.clicked.connect(lambda:self.setDisplayText("0"))
        self.boton_Punto.clicked.connect(self.puntos)
        self.botonMas.clicked.connect(self.sumar)
        self.botonMenos.clicked.connect(self.restar)
        self.botonMulti.clicked.connect(self.multiplicacion)
        self.botonRaiz.clicked.connect(self.raizCuadrada)
        self.botonDivi.clicked.connect(self.division)
        self.botonPorcen.clicked.connect(lambda:self.setDisplayText("%"))
        self.botonPoten.clicked.connect(self.potencia)
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
        self.potencia = False
        self.raizC = False
# √
        self.dicPotencia = {'0' : chr(0x2070), '1' : chr(0xB9), '2' : chr(0x0B2),'3' : chr(0x0b3), '4' : chr(0x2074), '5':chr(0x2075),'6':chr(0x2076), '7' : chr(0x2077), '8':chr(0x2078), '9':chr(0x2079)}
        self.dicPotencia2 = {}
    
    def raizCuadrada(self):
        self.raizC= True
        self.setDisplayText('√')

    def potencia(self):
        self.potencia = True

    def remplazarNum(self, var):
        for i in self.dicPotencia:
            if i == var:
                var = re.sub( i,self.dicPotencia[i], var)
                break
        return var
        
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
        HistoryOP = self.historial.currentItem().text().strip()
        expresion = ''
        for dig in HistoryOP:
            expresion += dig
        self.display.setText(expresion)


    def search(self, igualx):
        for i  in range(0, self.historial.count()):
            if self.historial.item(i).text() == igualx:
                self.historial.item(i).setFont (QFont ("Courier", 9, italic = True))


    def resultado(self):
        try:
            aux = self.display.text()
            aux = self.replacements(aux)
            if self.raizC:
                igual = f'{aux} **(0.5)'
                self.raizC = False
            else:
                igual = self.replacements(aux)

            igual = eval(igual)
            igualStr = str(igual).replace('.', ',')
            print(igualStr)
            if not igualStr == self.display.text():
                self.historial.addItem(f'{self.display.text():<0}')
                self.historial.addItem(f' {igualStr}')
                self.search(self.display.text())

            self.display.setText(str(igual).replace(".", ","))



        except:
            self.display.setText("ERROR")

    def limpiarDisplay(self):
        self.display.clear()

    def borrarDigito(self):
        self.display.backspace()
        self.display.setFocus()
        self.expresiones = self.display.text()

    def setDisplayText(self, tex):
        if self.display.text() == "ERROR":
            time.sleep(0.1)
            self.display.setText("")
        digito=tex
        
        if self.potencia:
            digito2 = self.remplazarNum(digito)
            self.display.setText(self.display.text()+ digito2)
            # self.dicPotencia2 = dict.fromkeys(digito, digito2)
            self.potencia = False

        elif self.raizC:
            digito3 = digito
            self.display.setText(self.display.text()+ digito3)
            print(digito3)
        else:
            self.display.setText(self.display.text()+ digito)

        self.display.setFocus()
        aux = self.display.text()
        try:
            self.label.setText(aux)
            aux = self.replacements(aux)
            if eval(aux):
                if self.raizC:
                    igual = f'{aux} **(0.5)'
                else:
                    igual = self.replacements(aux)

                igual = eval(igual)
                self.label.setText(str(igual).replace(".", ","))

        except:
            self.label.setText(".....")
        # if self.potencia:
        #     self.dicPotencia2 = dict.fromkeys(secuencia, 0.1)
        #     pass
        
        
    def replacements(self, var):
        operadores =(
            ('÷', '/'),('×', '*'), 
            (',', '.'),('%', '/100'),
            ('√', ''))
        
        for op in operadores:
            var = re.sub(op[0], op[1], var)
        
        for i in self.dicPotencia:
            if self.dicPotencia[i] in var:
                var = re.sub(self.dicPotencia[i], f'**{i}', var)
                print(var)
        return var    


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