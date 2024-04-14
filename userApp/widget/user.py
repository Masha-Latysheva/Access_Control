# Виджет сотрудников
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtCore, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit, QComboBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt6.QtCore import Qt

from datetime import datetime
from userApp.widget.msg import *

class UserWidget:
    'Окно сотрудники'
    def __init__(self, main, ui, pgcon, client):
        self.main = main
        self.ui = ui
        self.pgcon = pgcon
        self.client = client
        # self.ui.btnTypeUser.clicked.connect(self.userTypes)
        # self.ui.btnJobUser.clicked.connect(self.jobTypes)
        # self.ui.btnStructurUser.clicked.connect(self.structurTypes)
        # self.ui.btnResetUser.clicked.connect(self.Reset)
        # self.ui.btnAddUser.clicked.connect(self.Insert)
        # self.ui.btnSerchUser.clicked.connect(self.Search)
        # self.ui.btnClearsUser.clicked.connect(self.Clear)
        # self.ui.btnDeleteUser.clicked.connect(self.userDelete)
        # self.ui.btnSaveUser.clicked.connect(self.userUpdate)
        # self.ui.tabUser.cellClicked.connect(self.viewInfo)
        # self.ui.tabUidUser.cellClicked.connect(self.btnUidOn)
        # self.ui.tabWorkUser.cellClicked.connect(self.btnWorkOn)
        # self.ui.btUidAddUser.clicked.connect(self.tableUidAdd)
        # self.ui.btUidEditUser.clicked.connect(self.tableUidEdit)
        # self.ui.btUidDelUser.clicked.connect(self.tableUidDel)
        # self.ui.btWorkAddUser.clicked.connect(self.tableWorkAdd)
        # self.ui.btWorkEditUser.clicked.connect(self.tableWorkEdit)
        # self.ui.btWorkDelUser.clicked.connect(self.tableWorkDel)
        # self.ui.textUidUser.textChanged.connect(self.uidCount)
        # self.main.dictWork = {'0':'Добавлен в базу данных', '1':'Прнят на работу', '2':'Уволен', '3':'Дикретный отпуск', '4':'Пенсия'}
