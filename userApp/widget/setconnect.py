from cryptography.fernet import Fernet

from PyQt6.QtWidgets import QLineEdit
from userApp.widget.msg import *

cipher_key = '1gJKl236LeNKiaL06-tTf_Uq8pJLKC2aw2DggHa7ZXU='
cipher = Fernet(cipher_key)

class SetConnect:
    'Окно авторизации, нужно передать self'
    def __init__(self, main, ui, set=False, config=None, auEnable=False):
        self.main = main
        self.ui = ui
        self.set = set
        self.config = config
        self.auEnable = auEnable
#         self.btn = (self.ui.btnSetProg, self.ui.btnSetRepo, self.ui.btnSetOrg, self.ui.btnSetSQL, self.ui.btnSetMqtt)
#         if self.set:
#             self.ui.btnSetProg.setDisabled(True)
#             self.ui.btnSetRepo.setDisabled(True)
#             self.ui.btnSetOrg.setDisabled(True)
#             self.setSQL()
#         else:
#             self.setProg()
#         self.ui.btnSetProg.clicked.connect(self.setProg)
#         self.ui.btnSetRepo.clicked.connect(self.setRepo)
#         self.ui.btnSetOrg.clicked.connect(self.setOrg)
#         self.ui.btnSetSQL.clicked.connect(self.setSQL)
#         #self.ui.btnSetMqtt.clicked.connect(self.setMqtt)
#         if auEnable == False:
#             self.ui.btnSetCancel.clicked.connect(self.inAuWiget)
#         else:
#             self.ui.btnSetCancel.setDisabled(True)
#
#     def inAuWiget(self):
#         'возврат по кнопке отмена к авторизации'
#         self.ui.mainWidget.setCurrentIndex(4)
#
#     def setProg(self):
#         'Настройка программы'
#         self.ui.setWidget.setCurrentIndex(0)
#         self.coonectBtn = self.ui.btnSetProg
#         self.coonectBtn.setDisabled(True)
#         for btns in self.btn:
#             if btns != self.coonectBtn:
#                 btns.setDisabled(False)
#
#     def setRepo(self):
#         'Настройка отчетов'
#         self.ui.setWidget.setCurrentIndex(1)
#         self.coonectBtn = self.ui.btnSetRepo
#         self.coonectBtn.setDisabled(True)
#         for btns in self.btn:
#             if btns != self.coonectBtn:
#                 btns.setDisabled(False)
#
#     def setOrg(self):
#         'Настройка организации'
#         self.ui.setWidget.setCurrentIndex(2)
#         self.coonectBtn = self.ui.btnSetOrg
#         self.coonectBtn.setDisabled(True)
#         for btns in self.btn:
#             if btns != self.coonectBtn:
#                 btns.setDisabled(False)
#
#     def setSQL(self):
#         'Настройка SQL'
#         self.ui.setWidget.setCurrentIndex(3)
#         self.coonectBtn = self.ui.btnSetSQL
#         self.coonectBtn.setDisabled(True)
#         try:
#             self.ui.SetStartDBuser.setText(cipher.decrypt(self.config["SQL"]["user"]).decode("utf-8"))
#             self.ui.SetStartDBpas.setText(cipher.decrypt(self.config["SQL"]["password"]).decode("utf-8"))
#             self.ui.SetStartIP.setText(cipher.decrypt(self.config["SQL"]["host"]).decode("utf-8"))
#             self.ui.SetStartPort.setText(cipher.decrypt(self.config["SQL"]["port"]).decode("utf-8"))
#         except:
#             msgInfo('Произошла ошибка чтения конфигурационного файла')
#         if self.set:
#             self.ui.btnSetMqtt.setDisabled(False)
#             self.ui.SetStartDBuser.setEchoMode(QLineEdit.EchoMode.Password)
#             self.ui.SetStartDBpas.setEchoMode(QLineEdit.EchoMode.Password)
#             self.ui.SetStartIP.setEchoMode(QLineEdit.EchoMode.Password)
#             self.ui.SetStartPort.setEchoMode(QLineEdit.EchoMode.Password)
#         else:
#             for btns in self.btn:
#                 if btns != self.coonectBtn:
#                     btns.setDisabled(False)
#
#         try:
#             self.ui.SetStartDB.setText(self.config["SQL"]["database"])
#             self.ui.SetStartStruct.setText(self.config["DB"]["structsub"])
#             self.ui.SetStartJob.setText(self.config["DB"]["job"])
#             self.ui.SetStartType.setText(self.config["DB"]["type"])
#             self.ui.SetStartRecords.setText(self.config["DB"]["records"])
#             self.ui.SetStartUid.setText(self.config["DB"]["uid"])
#             self.ui.SetStartUser.setText(self.config["DB"]["user"])
#             self.ui.SetStartShedule.setText(self.config["DB"]["organization"])
#             self.ui.SetStartTopic.setText(self.config["DB"]["topic"])
#             self.ui.SetStartSetApp.setText(self.config["DB"]["setuserapp"])
#             self.ui.SetStartRol.setText(self.config["DB"]["approle"])
#             self.ui.SetStartUserApp.setText(self.config["DB"]["userapp"])
#             self.ui.SetStartWork.setText(self.config["DB"]["work"])
#         except:
#             msgInfo('Произошла ошибка чтения конфигурационного файла')
#         self.ui.btnSetSave.clicked.connect(self.saveSQL)
#         self.ui.btnSetReset.clicked.connect(self.setSQL)
#
#     def saveSQL(self):
#         'Кнопка сохранить в настройках SQL'
#         self.config["SQL"]["user"] = str(cipher.encrypt(bytes(self.ui.SetStartDBuser.text(), 'UTF-8')), 'UTF-8')
#         self.config["SQL"]["password"] = str(cipher.encrypt(bytes(self.ui.SetStartDBpas.text(), 'UTF-8')), 'UTF-8')
#         self.config["SQL"]["host"] = str(cipher.encrypt(bytes(self.ui.SetStartIP.text(), 'UTF-8')), 'UTF-8')
#         self.config["SQL"]["port"] = str(cipher.encrypt(bytes(self.ui.SetStartPort.text(), 'UTF-8')), 'UTF-8')
#         self.config["SQL"]["database"] = self.ui.SetStartDB.displayText()
#         self.config["DB"]["Structsub"] = self.ui.SetStartStruct.displayText()
#         self.config["DB"]["Job"] = self.ui.SetStartJob.displayText()
#         self.config["DB"]["Type"] = self.ui.SetStartType.displayText()
#         self.config["DB"]["Records"] = self.ui.SetStartRecords.displayText()
#         self.config["DB"]["UID"] = self.ui.SetStartUid.displayText()
#         self.config["DB"]["User"] = self.ui.SetStartUser.displayText()
#         self.config["DB"]["Organization"] = self.ui.SetStartOrganization.displayText()
#         self.config["DB"]["Topic"] = self.ui.SetStartTopic.displayText()
#         self.config["DB"]["AppRole"] = self.ui.SetStartRol.displayText()
#         self.config["DB"]["AppUser"] = self.ui.SetStartUserApp.displayText()
#         self.config["DB"]["Work"] = self.ui.SetStartWork.displayText()
#         path = "settings.ini"
#         with open(path, "w", encoding='utf-8') as config_file:
#             self.config.write(config_file)
#         if msgInfoKey('Для применения настроек необходимо перезагрузить приложение'):
#             self.main.restert()
#         self.setSQL()
#
#     def setMqtt(self):
#         'Настройка MQTT'
#         self.ui.setWidget.setCurrentIndex(4)
#         self.coonectBtn = self.ui.btnSetMqtt
#         self.coonectBtn.setDisabled(True)
#         try:
#             self.ui.SetStartMqttIP.setText(cipher.decrypt(self.config["MQTT"]["broker"]).decode("utf-8"))
#             self.ui.SetStartMqttPort.setText(cipher.decrypt(self.config["MQTT"]["port"]).decode("utf-8"))
#             self.ui.SetStartMqttUser.setText(cipher.decrypt(self.config["MQTT"]["username"]).decode("utf-8"))
#             self.ui.SetStartMqttPass.setText(cipher.decrypt(self.config["MQTT"]["password"]).decode("utf-8"))
#         except:
#             pass
#         if self.set:
#             self.ui.btnSetSQL.setDisabled(False)
#             try:
#                 self.ui.SetStartMqttIP.setEchoMode(QLineEdit.EchoMode.Password)
#                 self.ui.SetStartMqttPort.setEchoMode(QLineEdit.EchoMode.Password)
#                 self.ui.SetStartMqttUser.setEchoMode(QLineEdit.EchoMode.Password)
#                 self.ui.SetStartMqttPass.setEchoMode(QLineEdit.EchoMode.Password)
#             except:
#                 msgInfo('Произошла ошибка чтения конфигурационного файла')
#         else:
#             for btns in self.btn:
#                 if btns != self.coonectBtn:
#                     btns.setDisabled(False)
#
#         mqtt_version = self.config["MQTT"]["version"]
#         mqtt_tcp = self.config["MQTT"]["tcp"]  # 'tcp' or 'websockets'
#
#         self.ui.SetStartMqttTopic.setText(self.config["MQTT"]["topic_info"])
#         self.ui.SetStartMqttMsg.setText(self.config["MQTT"]["mes_info"])
#         self.ui.SetStartMqttID.setText(self.config["MQTT"]["client_id"])
#         self.ui.SetStartMqttAdd.setText(self.config["MQTT"]["add"])
#         self.ui.btnSetSave.clicked.connect(self.saveMqtt)
#         self.ui.btnSetReset.clicked.connect(self.setMqtt)
#
#     def saveMqtt(self):
#         'Кнопка сохранить в настройках SQL'
#         self.config["MQTT"]["broker"] = str(cipher.encrypt(bytes(self.ui.SetStartMqttIP.text(), 'UTF-8')), 'UTF-8')
#         self.config["MQTT"]["port"] = str(cipher.encrypt(bytes(self.ui.SetStartMqttPort.text(), 'UTF-8')), 'UTF-8')
#         self.config["MQTT"]["username"] = str(cipher.encrypt(bytes(self.ui.SetStartMqttUser.text(), 'UTF-8')), 'UTF-8')
#         self.config["MQTT"]["password"] = str(cipher.encrypt(bytes(self.ui.SetStartMqttPass.text(), 'UTF-8')), 'UTF-8')
#         self.config["MQTT"]["topic_info"] = self.ui.SetStartMqttTopic.displayText()
#         self.config["MQTT"]["mes_info"] = self.ui.SetStartMqttMsg.displayText()
#         self.config["MQTT"]["client_id"] = self.ui.SetStartMqttID.displayText()
#         # self.config["MQTT"]["version"] =
#         # self.config["MQTT"]["tcp"] =
#         self.config["MQTT"]["add"] = self.ui.SetStartMqttAdd.displayText()
#         path = "settings.ini"
#         with open(path, "w", encoding='utf-8') as config_file:
#             self.config.write(config_file)
#         if msgInfoKey('Для применения настроек необходимо перезагрузить приложение'):
#             self.main.restert()
#         self.setMqtt()
