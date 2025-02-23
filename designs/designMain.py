# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(565, 500))
        MainWindow.setMaximumSize(QtCore.QSize(565, 500))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background {\n"
"    color: RGB(255, 255, 255)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labCod = QtWidgets.QLabel(self.centralwidget)
        self.labCod.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.labCod.setObjectName("labCod")
        self.labQuant = QtWidgets.QLabel(self.centralwidget)
        self.labQuant.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.labQuant.setObjectName("labQuant")
        self.btnMainAdicionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnMainAdicionar.setGeometry(QtCore.QRect(10, 160, 81, 31))
        self.btnMainAdicionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMainAdicionar.setMouseTracking(False)
        self.btnMainAdicionar.setObjectName("btnMainAdicionar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 210, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtMainCod = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMainCod.setGeometry(QtCore.QRect(100, 80, 91, 20))
        self.txtMainCod.setMaxLength(5)
        self.txtMainCod.setObjectName("txtMainCod")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(440, 70, 111, 41))
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.tabCarrinho = QtWidgets.QTableWidget(self.centralwidget)
        self.tabCarrinho.setEnabled(True)
        self.tabCarrinho.setGeometry(QtCore.QRect(10, 230, 541, 261))
        self.tabCarrinho.setDragDropOverwriteMode(False)
        self.tabCarrinho.setShowGrid(True)
        self.tabCarrinho.setGridStyle(QtCore.Qt.SolidLine)
        self.tabCarrinho.setWordWrap(False)
        self.tabCarrinho.setObjectName("tabCarrinho")
        self.tabCarrinho.setColumnCount(0)
        self.tabCarrinho.setRowCount(0)
        self.tabCarrinho.horizontalHeader().setDefaultSectionSize(107)
        self.tabCarrinho.horizontalHeader().setMinimumSectionSize(107)
        self.tabCarrinho.horizontalHeader().setSortIndicatorShown(False)
        self.tabCarrinho.verticalHeader().setVisible(False)
        self.btnMainRemover = QtWidgets.QPushButton(self.centralwidget)
        self.btnMainRemover.setGeometry(QtCore.QRect(440, 160, 111, 31))
        self.btnMainRemover.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMainRemover.setMouseTracking(False)
        self.btnMainRemover.setObjectName("btnMainRemover")
        self.btnMainLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnMainLimpar.setGeometry(QtCore.QRect(440, 120, 111, 31))
        self.btnMainLimpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMainLimpar.setMouseTracking(False)
        self.btnMainLimpar.setObjectName("btnMainLimpar")
        self.btnMainConcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnMainConcluir.setGeometry(QtCore.QRect(100, 160, 91, 31))
        self.btnMainConcluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMainConcluir.setMouseTracking(False)
        self.btnMainConcluir.setDefault(False)
        self.btnMainConcluir.setFlat(False)
        self.btnMainConcluir.setObjectName("btnMainConcluir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 571, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.txtMainMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMainMessage.setEnabled(True)
        self.txtMainMessage.setGeometry(QtCore.QRect(10, 200, 541, 20))
        self.txtMainMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.txtMainMessage.setReadOnly(True)
        self.txtMainMessage.setObjectName("txtMainMessage")
        self.txtMainQuant = QtWidgets.QSpinBox(self.centralwidget)
        self.txtMainQuant.setGeometry(QtCore.QRect(130, 120, 61, 21))
        self.txtMainQuant.setObjectName("txtMainQuant")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Padaria"))
        self.labCod.setText(_translate("MainWindow", "Código:"))
        self.labQuant.setText(_translate("MainWindow", "Quantidade:"))
        self.btnMainAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.commandLinkButton.setText(_translate("MainWindow", "Acessar ADM"))
        self.tabCarrinho.setSortingEnabled(False)
        self.btnMainRemover.setText(_translate("MainWindow", "Remover Produto"))
        self.btnMainLimpar.setText(_translate("MainWindow", "Limpar Carrinho"))
        self.btnMainConcluir.setText(_translate("MainWindow", "Concluir Compra"))
        self.label.setText(_translate("MainWindow", "CAIXA DA PADARIA DO SEU VICTOR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
