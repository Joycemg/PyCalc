from PyQt5.QtWidgets import QMainWindow, QApplication, QUndoStack
from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont
import re
import ast, operator

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("programacion_II/clase4/calculadoranew.ui", self)
        self.expression = ''
        self.botonC.clicked.connect(self.clear_Display)
        self.botonX.clicked.connect(self.delete_Digit)
        self.boton_Punto.clicked.connect(self.comma)
        self.botonPorcen.clicked.connect(lambda:self.set_Display_Text("%"))
        self.botonPIzquierdo.clicked.connect(lambda:self.set_Display_Text("("))
        self.botonPDerecho.clicked.connect(lambda:self.set_Display_Text(")"))
        self.historial.clicked.connect(self.on_Click)
        #Operadores
        self.botonMas.clicked.connect(self.sumar)
        self.botonMenos.clicked.connect(self.restar)
        self.botonMulti.clicked.connect(self.multiplicacion)
        self.botonDivi.clicked.connect(self.division)
        self.botonRaiz.clicked.connect(self.raizCuadrada)
        self.botonPoten.clicked.connect(self.potencia)
        self.botonResultado.clicked.connect(self.result)
        #Numeros
        self.boton_.clicked.connect(lambda:self.set_Display_Text("0"))
        self.boton_1.clicked.connect(lambda:self.set_Display_Text("1"))
        self.boton_2.clicked.connect(lambda:self.set_Display_Text("2"))
        self.boton_3.clicked.connect(lambda:self.set_Display_Text("3"))
        self.boton_4.clicked.connect(lambda:self.set_Display_Text("4"))
        self.boton_5.clicked.connect(lambda:self.set_Display_Text("5"))
        self.boton_6.clicked.connect(lambda:self.set_Display_Text("6"))
        self.boton_7.clicked.connect(lambda:self.set_Display_Text("7"))
        self.boton_8.clicked.connect(lambda:self.set_Display_Text("8"))
        self.boton_9.clicked.connect(lambda:self.set_Display_Text("9"))
        self.digitPSindex = ''
        self.digitPNumber = ''
        self.pow = False
        self.raizC = False
# √
        self.dicSup = {}

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_ParenLeft:self.set_Display_Text("(")
        if event.key() == Qt.Key_ParenRight:self.set_Display_Text(")")
        if event.key() == Qt.Key_Period:
            self.comma()

        if event.key() == Qt.Key_Slash:self.division()
        if event.key() == Qt.Key_Dead_Circumflex:self.potencia()
        if event.key() == Qt.Key_Percent:self.set_Display_Text("%")
        if event.key() == Qt.Key_Asterisk:self.multiplicacion()
        if event.key() == Qt.Key_Minus:self.restar()
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:self.result()
        if event.key() == Qt.Key_Plus:self.sumar()
        if event.key() == Qt.Key_Backspace:self.delete_Digit()
        if event.key() == Qt.Key_R:self.raizCuadrada()
        if event.key() == Qt.Key_0:self.set_Display_Text("0")
        if event.key() == Qt.Key_1:self.set_Display_Text("1")
        if event.key() == Qt.Key_2:self.set_Display_Text("2")
        if event.key() == Qt.Key_3:self.set_Display_Text("3")
        if event.key() == Qt.Key_4:self.set_Display_Text("4")
        if event.key() == Qt.Key_5:self.set_Display_Text("5")
        if event.key() == Qt.Key_6:self.set_Display_Text("6")
        if event.key() == Qt.Key_7:self.set_Display_Text("7")
        if event.key() == Qt.Key_8:self.set_Display_Text("8")
        if event.key() == Qt.Key_9:self.set_Display_Text("9")                
    def arithmetic(self,s):
        
        binOps = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow
        }

        unOps = {
        ast.USub: operator.neg,
        ast.UAdd: operator.pos

        }

        node = ast.parse(s, mode='eval')

        def _eval(node):
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.Str):
                return node.s
            elif isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.BinOp):
                return binOps[type(node.op)](_eval(node.left), _eval(node.right))
            elif isinstance(node, ast.UnaryOp):
                return unOps[type(node.op)](_eval(node.operand))
            else:
                raise Exception('Unsupported type {}'.format(node))
                
        return _eval(node.body)

    def get_Sup(self, x):
        normal = "0123456789"
        sup_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        res = x.maketrans(''.join(normal), ''.join(sup_s))
        return x.translate(res)

    def sumar(self):
        self.offPow()
        self.set_Display_Text(" + ")

    def restar(self):
        self.offPow()
        # self.raizC = False
        self.set_Display_Text(" - ")
    def multiplicacion(self):
        self.offPow()
        # self.raizC = False
        self.set_Display_Text(" × ")
    def division(self):
        self.offPow()
        # self.raizC = False
        if self.display.text() == '':
            self.display.setText("")
        else:
            self.set_Display_Text(" ÷ ")

    def right(self,str):
        str = str[1:] + str[0]
        return str

    def raizCuadrada(self):
        self.offPow()
        self.raizC= True
        self.set_Display_Text('√')

    def potencia(self):
        if self.display.text():
            self.pow = True


    def comma(self):
        if self.display.text() == '':
            self.set_Display_Text("0,")
        else:
            self.set_Display_Text(",")

    def clear_Display(self):
        self.display.clear()
        self.expression = ''
        self.digitPNumber = ''
        self.digitPSindex = ''
        self.pow = False
        self.raizC = False

    def delete_Digit(self):
        if self.pow:
            self.digitPSindex = self.digitPSindex[:-1]
            self.digitPNumber = self.digitPNumber[:-1]
        if self.display.text():
            self.display.backspace()
            self.expression = self.expression[:-1]
            self.label.setText(self.expression)
        else:
            self.clear_Display()
            self.expression = ''

    def offPow(self):
        if self.pow:
            self.dicSup[self.digitPNumber] = self.digitPSindex
            self.digitPSindex = ''
            self.digitPNumber = ''
            self.pow = False

    def offRc(self):
        if self.raizC:
            rc = self.expression.split()
            print(rc)
            for i in range(len(rc)):
                if "√" in rc[i]:
                    rc[i] = self.right(rc[i])
            self.expression = ''.join(rc)
        self.raizC = False


    def result(self):
        self.offPow()
        self.offRc()
        equals = self.expression
        equals = self.replacements(equals)
        equals = self.arithmetic(equals)

 
        try:
            equalStr = f'{equals:15G}'.replace('.', ',').strip()
            if not equalStr == self.display.text():
                self.historial.addItem(f'{self.display.text()}')
                self.historial.addItem(f' {equalStr}')
                self.search(self.display.text())

            self.display.setText(equalStr)


        except:
            self.display.setText("ERROR")

        self.expression = str(equals)

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
            self.expression += self.get_Sup(digito)
            self.digitPSindex += self.get_Sup(digito)
            self.digitPNumber += digito
        else:
            self.expression += digito
            self.display.setText(self.display.text() + digito.strip())
        self.label.setText(self.expression)



    def replacements(self, var):
        operators =(
            ('÷', '/'),('×', '*'),
            (',', '.'),('%', '/100'),
            ('√', '**(0.5)'))

        for op in operators:
            var = re.sub(op[0], op[1], var)

        for i in self.dicSup:
            if self.get_Sup(i) == self.dicSup[i]:
                var = re.sub(self.dicSup[i], f'**{i}', var)
                print(var)
        print(var)
        return var


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()