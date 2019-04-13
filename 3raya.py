# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3raya.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import random
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ventana(object):
    tablero = [0,0,0,0,0,0,0,0,0] #0= vacio 1=jugada persona 2=jugada maquina
    movimientos = 0


    def setupUi(self, ventana):
        ventana.setObjectName(_fromUtf8("ventana"))
        ventana.resize(495, 320)
        ventana.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ventana.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.b0 = QtGui.QPushButton(ventana)
        self.b0.setGeometry(QtCore.QRect(10, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b0.setFont(font)
        self.b0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b0.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b0.setText(_fromUtf8(""))
        self.b0.setObjectName(_fromUtf8("b0"))
        self.b3 = QtGui.QPushButton(ventana)
        self.b3.setGeometry(QtCore.QRect(10, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b3.setText(_fromUtf8(""))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.b6 = QtGui.QPushButton(ventana)
        self.b6.setGeometry(QtCore.QRect(10, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b6.setText(_fromUtf8(""))
        self.b6.setObjectName(_fromUtf8("b6"))
        self.b7 = QtGui.QPushButton(ventana)
        self.b7.setGeometry(QtCore.QRect(110, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b7.setFont(font)
        self.b7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b7.setText(_fromUtf8(""))
        self.b7.setObjectName(_fromUtf8("b7"))
        self.b4 = QtGui.QPushButton(ventana)
        self.b4.setGeometry(QtCore.QRect(110, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b4.setText(_fromUtf8(""))
        self.b4.setObjectName(_fromUtf8("b4"))
        self.b1 = QtGui.QPushButton(ventana)
        self.b1.setGeometry(QtCore.QRect(110, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b1.setText(_fromUtf8(""))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b2 = QtGui.QPushButton(ventana)
        self.b2.setGeometry(QtCore.QRect(210, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b2.setText(_fromUtf8(""))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.b5 = QtGui.QPushButton(ventana)
        self.b5.setGeometry(QtCore.QRect(210, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b5.setText(_fromUtf8(""))
        self.b5.setObjectName(_fromUtf8("b5"))
        self.b8 = QtGui.QPushButton(ventana)
        self.b8.setGeometry(QtCore.QRect(210, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b8.setFont(font)
        self.b8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.b8.setText(_fromUtf8(""))
        self.b8.setObjectName(_fromUtf8("b8"))
        self.ePuntaje = QtGui.QLabel(ventana)
        self.ePuntaje.setGeometry(QtCore.QRect(330, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ePuntaje.setFont(font)
        self.ePuntaje.setObjectName(_fromUtf8("ePuntaje"))
        self.eMaquina = QtGui.QLabel(ventana)
        self.eMaquina.setGeometry(QtCore.QRect(330, 100, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eMaquina.setFont(font)
        self.eMaquina.setStyleSheet(_fromUtf8("color: rgb(226,0,0);"))
        self.eMaquina.setObjectName(_fromUtf8("eMaquina"))
        self.eEmpate = QtGui.QLabel(ventana)
        self.eEmpate.setGeometry(QtCore.QRect(330, 140, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eEmpate.setFont(font)
        self.eEmpate.setStyleSheet(_fromUtf8("color: rgb(226, 0, 0);"))
        self.eEmpate.setObjectName(_fromUtf8("eEmpate"))
        self.eYo = QtGui.QLabel(ventana)
        self.eYo.setGeometry(QtCore.QRect(330, 180, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eYo.setFont(font)
        self.eYo.setStyleSheet(_fromUtf8("color: rgb(226,0,0);"))
        self.eYo.setObjectName(_fromUtf8("eYo"))
        self.lMaquina = QtGui.QLineEdit(ventana)
        self.lMaquina.setEnabled(False)
        self.lMaquina.setGeometry(QtCore.QRect(410, 90, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lMaquina.setFont(font)
        self.lMaquina.setObjectName(_fromUtf8("lMaquina"))
        self.lEmpate = QtGui.QLineEdit(ventana)
        self.lEmpate.setEnabled(False)
        self.lEmpate.setGeometry(QtCore.QRect(410, 130, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lEmpate.setFont(font)
        self.lEmpate.setObjectName(_fromUtf8("lEmpate"))
        self.lYo = QtGui.QLineEdit(ventana)
        self.lYo.setEnabled(False)
        self.lYo.setGeometry(QtCore.QRect(410, 170, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lYo.setFont(font)
        self.lYo.setObjectName(_fromUtf8("lYo"))
        self.bReiniciar = QtGui.QPushButton(ventana)
        self.bReiniciar.setGeometry(QtCore.QRect(350, 240, 95, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bReiniciar.setFont(font)
        self.bReiniciar.setStyleSheet(_fromUtf8("background-color: rgb(85, 192, 0);"))
        self.bReiniciar.setObjectName(_fromUtf8("bReiniciar"))

        QtCore.QObject.connect(self.b0, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_11)
        QtCore.QObject.connect(self.b1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_12)
        QtCore.QObject.connect(self.b2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_13)
        QtCore.QObject.connect(self.b3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_21)
        QtCore.QObject.connect(self.b4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_22)
        QtCore.QObject.connect(self.b5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_23)
        QtCore.QObject.connect(self.b6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_31)
        QtCore.QObject.connect(self.b7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_32)
        QtCore.QObject.connect(self.b8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacer_click_33)
        QtCore.QObject.connect(self.bReiniciar,QtCore.SIGNAL(_fromUtf8("clicked()")),self.reiniciar)


        self.retranslateUi(ventana)
       # QtCore.QMetaObject.connectSlotsByName(ventana)
    def hacer_click_11(self):
            self.jugada(self.b0)
    def hacer_click_12(self):
            self.jugada(self.b1)

    def hacer_click_13(self):
            self.jugada(self.b2)

    def hacer_click_21(self):
            self.jugada(self.b3)

    def hacer_click_22(self):
            self.jugada(self.b4)

    def hacer_click_23(self):
            self.jugada(self.b5)

    def hacer_click_31(self):
            self.jugada(self.b6)

    def hacer_click_32(self):
            self.jugada(self.b7)

    def hacer_click_33(self):
            self.jugada(self.b8)


    def jugada(self,boton):
        boton.setEnabled(False)
        boton.setText('X')

        self.tablero[int(list(boton.objectName())[1])]=1
        self.movimientos+=1
        if self.verificar_jugada(1):
            yo=str(int(self.lYo.displayText())+1)
            self.lYo.setText(yo)
            self.congelar()
            return
        elif self.colocar_ficha_maquina():
            self.movimientos+=1
            if self.verificar_jugada(2):
                maquina=str(int(self.lMaquina.displayText())+1)
                self.lMaquina.setText(maquina)
                self.congelar()
                return
        if self.movimientos == 9:
            empate=str(int(self.lEmpate.displayText())+1)
            self.lEmpate.setText(empate)




    def verificar_jugada(self,valor):

           if self.tablero[0]==self.tablero[1]==self.tablero[2]==valor:
               self.pintar(0,1,2)
               return 1

           if self.tablero[3] == self.tablero[4] == self.tablero[5] == valor:
                   self.pintar(3,4,5)
                   return 1

           if self.tablero[6] == self.tablero[7] == self.tablero[8] == valor:
                   self.pintar(6,7,8)
                   return 1

           if self.tablero[0] == self.tablero[4] == self.tablero[8] == valor:
                   self.pintar(0,4,8)
                   return 1

           if self.tablero[2] == self.tablero[4] == self.tablero[6] == valor:
                    self.pintar(2,4,6)
                    return 1

           if self.tablero[0] == self.tablero[3] == self.tablero[6] == valor:
                   self.pintar(0,3,6)
                   return 1

           if self.tablero[1] == self.tablero[4] == self.tablero[7] == valor:
                    self.pintar(1,4,7)
                    return 1
           if self.tablero[2] == self.tablero[5] == self.tablero[8] == valor:
                    self.pintar(2,5,8)
                    return 1


    def pintar(self,a,b,c):
       self.__dict__['b'+str(a)].setStyleSheet(_fromUtf8("color:rgb(200,0,100);"))
       self.__dict__['b' + str(b)].setStyleSheet(_fromUtf8("color:rgb(200,0,100);"))
       self.__dict__['b' + str(c)].setStyleSheet(_fromUtf8("color:rgb(200,0,100);"))

    def reiniciar(self):
        self.tablero=[0,0,0,0,0,0,0,0,0]
        self.movimientos=0
        i =0
        while i<9:

            self.__dict__['b' + str(i)].setEnabled(True)
            self.__dict__['b' + str(i)].setText('')
            self.__dict__['b' + str(i)].setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
            i+=1

    def congelar(self):
        i = 0
        while i < 9:
            self.__dict__['b' + str(i)].setEnabled(False)
            i += 1

    def colocar_ficha_maquina(self):
        while self.tablero.count(0):
            i=random.randrange(9)
            boton_maquina=self.__dict__['b' + str(i)]
            if not self.tablero[i]:
                self.tablero[i]=2
                boton_maquina.setText('0')
                boton_maquina.setEnabled(False)
                return True


    def retranslateUi(self, ventana):
        ventana.setWindowTitle(_translate("ventana", "3 en Raya", None))
        self.ePuntaje.setText(_translate("ventana", "PUNTUACION", None))
        self.eMaquina.setText(_translate("ventana", "Maquina", None))
        self.eEmpate.setText(_translate("ventana", "Empates", None))
        self.eYo.setText(_translate("ventana", "Yo", None))
        self.lMaquina.setText(_translate("ventana", "0", None))
        self.lEmpate.setText(_translate("ventana", "0", None))
        self.lYo.setText(_translate("ventana", "0", None))
        self.bReiniciar.setText(_translate("ventana", "Reiniciar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ventana = QtGui.QWidget()
    ui = Ui_ventana()
    ui.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())

