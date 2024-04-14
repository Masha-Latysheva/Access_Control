# Виджет отчетов
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from userApp.widget.msg import *

class OrganizationWidget:
    'Окно сотрудники'
    def __init__(self, main, ui, pgcon):
        self.main = main
        self.ui = ui
        self.pgcon = pgcon