import sys
from sys import argv, executable
import os
from PyQt6 import QtWidgets, QtCore, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit, QComboBox
from PyQt6.QtGui import QPixmap

from PyQt6.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

import psycopg2
# from datetime import datetime
import configparser
from gui.mainui import *
from gui.icon_test import *

from widget.config import *
from widget.user import *
from widget.home import *
from widget.directory import *
from widget.organization import *
from widget.reports import *
from widget.start import *
from widget.info import *
from widget.setconnect import *
from userApp.widget.msg import *
from cryptography.fernet import Fernet


# конфиг прасер
startConfig()

config = configparser.ConfigParser()
config.read("settings.ini")

conStatus = False
errorStatus = ''
# #Настройки SQL
# try:
#     enableMqtt = bool(config["MQTT"]["enable"])
# except:
#     enableMqtt = False
try:
    pg_user = config["SQL"]["user"]
    pg_password = config["SQL"]["password"]
    pg_host = config["SQL"]["host"]
    pg_port = config["SQL"]["port"]
except:
    pg_user, pg_password, pg_host, pg_port = '', '', '', ''
    errorStatus = 'SetSQL,'
# try:
#     mqtt_broker = config["MQTT"]["broker"]
#     mqtt_port = config["MQTT"]["port"]
#     mqtt_username = config["MQTT"]["username"]
#     mqtt_password = config["MQTT"]["password"]
#     mqtt_topic_info = config["MQTT"]["topic_info"]
#     mqtt_mes_info = config["MQTT"]["mes_info"]
#     mqtt_client_id = config["MQTT"]["client_id"]
#     mqtt_version = config["MQTT"]["version"]
#     mqtt_tcp = config["MQTT"]["tcp"]
#     mqtt_add = config["MQTT"]["add"]
# except:
#     mqtt_broker, mqtt_port, mqtt_username, mqtt_password, mqtt_client_id = '', '', '', '', ''
#     if enableMqtt:
#         errorStatus += 'SetMqtt,'
try:
    pg_database = config["SQL"]["database"]
    pg_DBstructsub = config["DB"]["Structsub"]
    pg_DBjob = config["DB"]["Job"]
    pg_DBtype = config["DB"]["Type"]
    pg_DBrecords = config["DB"]["records"]
    pg_DBuid = config["DB"]["UID"]
    pg_DBuser = config["DB"]["User"]
    pg_DBtopic = config["DB"]["Topic"]
    pg_DBapprole = config["DB"]["AppRole"]
    pg_DBuserapp = config["DB"]["UserApp"]
    pg_DBsetuserapp = config["DB"]["SetUserApp"]
    pg_DBwork = config["DB"]["Work"]
    pg_DBorganization = config["DB"]["Organization"]
    pg_DBref = config["DB"]["Ref"]
except:
    pg_database, pg_DBstructsub, pg_DBjob, pg_DBtype, pg_DBrecords, pg_DBuid, pg_DBuser, \
    pg_DBtopic, pg_DBapprole, pg_DBuserapp, pg_DBsetuserapp, pg_DBwork, pg_DBorganization, pg_DBref\
    = '', '', '', '', '', '', '', '', '', '', '', '', '', ''

class MyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Система контроля доступа")
        self.DBstructsub = pg_DBstructsub
        self.DBjob = pg_DBjob
        self.DBtype = pg_DBtype
        self.DBrecords = pg_DBrecords
        self.DBuid = pg_DBuid
        self.DBuser = pg_DBuser
        self.DBtopic = pg_DBtopic
        self.DBapprole = pg_DBapprole
        self.DBuserapp = pg_DBuserapp
        self.DBsetuserapp = pg_DBsetuserapp
        self.DBwork = pg_DBwork
        self.DBorganization = pg_DBorganization
        self.DBref = pg_DBref
        self.errorStatus = errorStatus
        # self.enableMqtt = enableMqtt
        self.btnHome = self.ui.btnHome
        self.btnReports = self.ui.btnReports
        self.btnEmployees = self.ui.btnEmployees
        self.btnDirectory = self.ui.btnDirectory
        self.btnOrganizations = self.ui.btnOrganizations
        self.btnOff = self.ui.btnOff
        self.btnSet = self.ui.btnSet
        self.btnInfo = self.ui.btnInfo
        self.btnOkStart = self.ui.btnOkStart
        self.stackedWidget = self.ui.stackedWidget
        self.ui.stackedWidget.setCurrentIndex(3)
        # self.btnRole = {self.btnReports: 1, self.btnEmployees: False, self.btnDirectory: False,
        #                 self.btnOrganizations: False, self.btnOff: 6, self.btnSet: 7, self.btnInfo: 8}
        self.btn = {self.btnHome: 0, self.btnReports: 1, self.btnEmployees: 2, self.btnDirectory: 4,
                    self.btnOrganizations: 5, self.btnOff: 6, self.btnSet: 7, self.btnInfo: 8}
        for i in self.btn:
            i.setDisabled(True)
        self.btnHome.clicked.connect(self.actWidget)
        self.btnReports.clicked.connect(self.actWidget)
        self.btnEmployees.clicked.connect(self.actWidget)
        self.btnDirectory.clicked.connect(self.actWidget)
        self.btnOrganizations.clicked.connect(self.actWidget)
        self.btnOff.clicked.connect(self.actWidget)
        self.btnSet.clicked.connect(self.actWidget)
        self.btnInfo.clicked.connect(self.actWidget)
        # Возможно доп кнопки при авторизации
        # self.ui.btnCloseOff.clicked.connect(self.close)
        # self.ui.btnRestartOff.clicked.connect(self.restart)
        # self.ui.btnUserOutOff.clicked.connect(self.logoOff)
        self.auStart = AuWidgetStart(self, self.ui, pgcon, conStatus, config)

    def logoOff(self):
        'Кнопка сменить пользователя'
        for i in self.btn:
            i.setDisabled(True)
        self.auStart = AuWidgetStart(self, self.ui, pgcon, conStatus, config)
        self.ui.stackedWidget.setCurrentIndex(3)

    def restart(self):
        'Перезагрузка программы'
        os.execl(executable, os.path.abspath(__file__), *argv)

    def actWidget(self):
        'Функция переключения виджетов'
        button = self.sender()
        button.setDisabled(True)
        for btns in self.btn:
            if btns != button:
                btns.setDisabled(False)
        self.ui.stackedWidget.setCurrentIndex(self.btn[button])

try:
    pgcon = psycopg2.connect(user=pg_user, password=pg_password, host=pg_host, port=pg_port, database=pg_database)
    conStatus = True
except:
    pgcon = None
    errorStatus += 'ConSQL,'

print(pg_user)
print(pg_password)
print(pg_host)
print(pg_port)
print(pg_database)

# try:
#     client = mqtt.Client(mqtt_client_id)
#     if enableMqtt:
#         client = mqtt.Client(mqtt_client_id)
#         client.username_pw_set(mqtt_username, mqtt_password)
#         client.connect(mqtt_broker, port=mqtt_port)
#         client.subscribe(mqtt_add)
# except:
#     client = mqtt.Client(mqtt_client_id)
#     if enableMqtt:
#         errorStatus += 'ConMqtt,'
#     print('erroe 1')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyQtApp()
    window.show()
    sys.exit(app.exec())