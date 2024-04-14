from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit
from PyQt6 import QtWidgets, QtGui
import os
from sys import argv, executable

def msgInfo(infomsg='Произошла ошибка', title='Внимание'):
    'Окно оповещений (Текст сообщения, имя окна)'
    dlg = QMessageBox()
    dlg.setWindowTitle(title)
    dlg.setFont(QtGui.QFont('Arial', 12))
    dlg.setText(infomsg)
    dlg.setIcon(QMessageBox.Icon.Information)
    dlg.exec()

def msgInfoKey(infomsg='Произошла ошибка', title='Внимание'):
    'Окно оповещений (Текст сообщения, имя окна)'
    dlg = QMessageBox()
    dlg.setWindowTitle(title)
    dlg.setFont(QtGui.QFont('Arial', 12))
    dlg.setText(infomsg)
    dlg.setIcon(QMessageBox.Icon.Information)
    btn_delete = dlg.addButton('  Да  ', QMessageBox.ButtonRole.YesRole)
    btn_cancel = dlg.addButton('  Нет  ', QMessageBox.ButtonRole.NoRole)
    dlg.exec()
    if dlg.clickedButton() == btn_delete:
        dlg.close()
        return True
    else:
        dlg.close()
        return False


def msgInfoError(infomsg='Произошла ошибка', title='Внимание'):
    'Окно оповещений (Текст сообщения, имя окна)'
    dlg = QMessageBox()
    dlg.setWindowTitle(title)
    dlg.setFont(QtGui.QFont('Arial', 12))
    dlg.setText(infomsg)
    dlg.setIcon(QMessageBox.Icon.Information)
    btn_delete = dlg.addButton('  Да  ', QMessageBox.ButtonRole.YesRole)
    btn_cancel = dlg.addButton('  Нет  ', QMessageBox.ButtonRole.NoRole)
    dlg.exec()
    if dlg.clickedButton() == btn_delete:
        dlg.close()
        os.execl(executable, os.path.abspath(__file__), *argv)
    else:
        dlg.close()
        return False

def noneFunc():
    dlg = QMessageBox()
    dlg.setWindowTitle('Внимание')
    dlg.setFont(QtGui.QFont('Arial', 12))
    dlg.setText('Функция находится в разработке')
    dlg.setIcon(QMessageBox.Icon.Information)
    dlg.exec()