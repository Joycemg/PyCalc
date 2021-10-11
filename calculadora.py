from PyQt5.QtWidgets import QMainWindow, QApplication, QUndoStack
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QFont
import re
import time

#### BUG EN POTENCIA AL USAR BACK AL DIGITO DE LA CALCULADORA
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
        self.digitoP = ''
        self.digitoP2 = ''
        self.poten = False
        self.raizC = False
# √
        self.dicPotencia = {'0' : chr(0x2070), '1' : chr(0xB9), '2' : chr(0x0B2),'3' : chr(0x0b3), '4' : chr(0x2074), '5':chr(0x2075),'6':chr(0x2076), '7' : chr(0x2077), '8':chr(0x2078), '9':chr(0x2079)}
        
        self.dicPotencia2 = {}
    
    def raizCuadrada(self):
        self.poten = False
        self.raizC= True
        self.setDisplayText('√')

    def potencia(self):
        self.raizC = False
        self.poten = True

    def remplazarNum(self, var):
        for i in self.dicPotencia:
            if i == var:
                var = re.sub( i,self.dicPotencia[i], var)
                # break
        return var

    def convertirPotencia(self, var):
        pass
    def sumar(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()
        self.poten = False
        self.raizC = False
        self.setDisplayText("+")

    def restar(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()
        self.poten = False
        self.raizC = False
        self.setDisplayText("-")
    
    def multiplicacion(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()
        self.poten = False
        self.raizC = False
        self.setDisplayText("×")

    def division(self):
        # if "+" or "-" or "*" or "/" in self.expresiones:
        #     self.resultado()
        self.poten = False
        self.raizC = False
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
        aux = self.display.text()
        igual = self.replacements(aux, self.digitoP)
        if self.raizC:
            igual = f'{igual}**(0.5)'
            self.raizC = False
        try:
            igual = eval(igual)
            igualStr = str(igual).replace('.', ',')
            if not igualStr == self.display.text():
                self.historial.addItem(f'{self.display.text():<0}')
                self.historial.addItem(f' {igualStr}')
                self.search(self.display.text())

            if type(igual) == float:
                self.display.setText(f'{igual:.2f}'.replace(".", ","))
            else:
                self.display.setText(str(igual))

            self.digitoP = ''
            self.digitoP2 = ''
            self.poten = False
            self.dicPotencia2.clear()


        except:
            self.display.setText("ERROR")

    def limpiarDisplay(self):
        self.poten = False
        self.raizC = False
        self.display.clear()
        self.digitoP = ''
        self.digitoP2 = ''
        self.dicPotencia2.clear()

    def borrarDigito(self):
        if self.display.text():
            self.display.backspace()
        else:
            self.limpiarDisplay()
    def setDisplayText(self, tex):
        if self.display.text() == "ERROR":
            time.sleep(0.1)
            self.display.setText("")
        digito=tex
        
        if self.poten:
            self.digitoP2 = self.digitoP2 + digito
            digito2 = self.remplazarNum(digito)
            self.digitoP = self.digitoP + digito2
            self.display.setText(self.display.text()+ digito2)
            self.dicPotencia2[self.digitoP2] = self.digitoP
        

        elif self.raizC:
            digito3 = digito
            self.display.setText(self.display.text()+ digito3)
        else:
            self.display.setText(self.display.text()+ digito)

        self.display.setFocus()
        aux = self.display.text()
        igual = self.replacements(aux, self.digitoP)
        print(igual)
        try:
            if eval(igual):
                if self.raizC:
                    igual = f'{igual} **(0.5)'
                    print(igual)

                print(igual)
                igual = eval(igual)
                print(igual)
                self.label.setText(str(igual).replace(".", ","))
        except:
            self.label.setText(".....")

        # if self.potencia:
        #     self.dicPotencia2 = dict.fromkeys(secuencia, 0.1)
        #     pass

        
        
    def replacements(self, var, var2):
        operadores =(
            ('÷', '/'),('×', '*'), 
            (',', '.'),('%', '/100'),
            ('√', ''))
        
        for op in operadores:
            var = re.sub(op[0], op[1], var)
        
        for i in self.dicPotencia2:
            if self.dicPotencia2[i] == var2:
                var = re.sub(self.dicPotencia2[i], f'**{i}', var)
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