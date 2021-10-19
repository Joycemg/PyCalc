from PyQt5.QtWidgets import QMainWindow, QApplication, QUndoStack
from PyQt5 import uic
from PyQt5.QtGui import QFont
import re
import ast

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("programacion_II/clase4/calculadoranew.ui", self)
        self.botonC.clicked.connect(self.clear_Display)
        self.botonX.clicked.connect(self.delete_Digit)
        self.botonResultado.clicked.connect(self.result)
        self.boton_Punto.clicked.connect(self.comma)
        self.botonMas.clicked.connect(self.sumar)
        self.botonMenos.clicked.connect(self.restar)
        self.botonMulti.clicked.connect(self.multiplicacion)
        self.botonDivi.clicked.connect(self.division)
        self.botonRaiz.clicked.connect(self.raizCuadrada)
        self.botonPoten.clicked.connect(self.potencia)
        self.boton_.clicked.connect(lambda:self.set_Display_Text("0"))
        self.botonPorcen.clicked.connect(lambda:self.set_Display_Text("%"))
        self.botonPIzquierdo.clicked.connect(lambda:self.set_Display_Text("("))
        self.botonPDerecho.clicked.connect(lambda:self.set_Display_Text(")"))
        self.boton_1.clicked.connect(lambda:self.set_Display_Text("1"))
        self.boton_2.clicked.connect(lambda:self.set_Display_Text("2"))
        self.boton_3.clicked.connect(lambda:self.set_Display_Text("3"))
        self.boton_4.clicked.connect(lambda:self.set_Display_Text("4"))
        self.boton_5.clicked.connect(lambda:self.set_Display_Text("5"))
        self.boton_6.clicked.connect(lambda:self.set_Display_Text("6"))
        self.boton_7.clicked.connect(lambda:self.set_Display_Text("7"))
        self.boton_8.clicked.connect(lambda:self.set_Display_Text("8"))
        self.boton_9.clicked.connect(lambda:self.set_Display_Text("9"))
        self.historial.clicked.connect(self.on_Click)
        self.digitPSindex = ''
        self.digitPNumber = ''
        self.pow = False
        self.raizC = False
# √
        
        self.dicSup = {}
    def get_Sup(self, x):
        normal = "0123456789"
        sup_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        res = x.maketrans(''.join(normal), ''.join(sup_s))
        return x.translate(res)
    def sumar(self):
        self.pow = False
        self.raizC = False
        self.set_Display_Text("+")
    def restar(self):
        self.pow = False
        self.raizC = False
        self.set_Display_Text("-")
    def multiplicacion(self):
        self.pow = False
        self.raizC = False
        self.set_Display_Text("×")
    def division(self):
        self.pow = False
        self.raizC = False
        if self.display.text() == '':
            self.display.setText("")
        else:
            self.set_Display_Text("÷")
   
    def raizCuadrada(self):
        self.pow = False
        self.raizC= True
        self.set_Display_Text('√')

    def potencia(self):
        self.raizC = False
        if self.display.text():
            self.pow = True

    def comma(self):
        if self.display.text() == '':
            self.set_Display_Text("0,")
        else:
            self.set_Display_Text(",")

    def clear_Display(self):
        self.lower_Flag()
        self.display.clear()
        self.digitPNumber = ''
        self.digitPSindex = ''

    def delete_Digit(self):
        if self.pow:
            self.digitPSindex = self.digitPSindex[:-1]
            self.digitPNumber = self.digitPNumber[:-1]
        if self.display.text():
            self.display.backspace()
        else:
            self.clear_Display()


    def super_Script(self, var):
        for i in self.dicPotencia:
            if i == var:
                var = re.sub( i,self.dicPotencia[i], var)
        return var

    def result(self):
        expression = self.display.text()
        equal = self.replacements(expression)
        print(equal)
        if self.raizC:
            equal = f'{equal}**(0.5)'
            self.raizC = False

        try:
            equal = ast.literal_eval(equal)
            equalStr = f'{equal:15G}'.replace('.', ',').strip()
            if not equalStr == expression:
                self.historial.addItem(f'{expression}')
                self.historial.addItem(f' {equalStr}')
                self.search(expression)

            self.display.setText(equalStr)

        except:
            self.display.setText("ERROR")

        self.digitPNumber = ''
        self.digitPSindex = ''
        self.lower_Flag()

    def search(self, equal):
        for i  in range(0, self.historial.count()):
            if self.historial.item(i).text() == equal:
                self.historial.item(i).setFont (QFont ("Courier", 9, italic = True))
    def on_Click(self):
        opHistory = self.historial.currentItem().text().strip()
        expression = ''
        for dig in opHistory:
            expression += dig
        self.display.setText(expression)
    
    def lower_Flag(self):
        self.pow = False
        self.raizC = False
    def set_Display_Text(self, text):
        if self.display.text() == "ERROR":
            self.display.setText("")
        digito=text

        if self.pow:
            self.display.setText(self.display.text()+ self.get_Sup(digito))
            self.digitPSindex += self.get_Sup(digito)
            self.digitPNumber += digito
            self.dicSup[self.digitPNumber] = self.digitPSindex
        else:
            self.display.setText(self.display.text() + digito)

        print(self.display.text())
        equal = self.replacements(self.display.text())
        try:
            print(ast.literal_eval(equal))
            print(equal)
            if ast.literal_eval(equal):
                if self.raizC:
                    equal = f'{equal} **(0.5)'
                equal = ast.literal_eval(equal)
                self.label.setText(f'{equal:15G}'.replace('.', ','))
        except:
            self.label.setText(".....")
    
    def replacements(self, var):
        operators =(
            ('÷', '/'),('×', '*'), 
            (',', '.'),('%', '/100'),
            ('√', ''))
        
        for op in operators:
            var = re.sub(op[0], op[1], var)
        
        for i in self.dicSup:
            if self.dicSup[i] == self.digitPSindex:
                var = re.sub(self.dicSup[i], f'**{i}', var)
        return var

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