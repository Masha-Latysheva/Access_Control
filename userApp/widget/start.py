# Виджет авторизации
from userApp.gui.mainui import *
from userApp.gui.icon_test import *

from cryptography.fernet import Fernet
from configparser import ConfigParser
from userApp.widget.directory import *
from userApp.widget.reports import *
from userApp.widget.home import *
from userApp.widget.organization import *
from userApp.widget.user import *
from userApp.widget.info import *
from userApp.widget.setconnect import *
from userApp.widget.msg import *

class AuWidgetStart:
    'Окно авторизации, нужно передать self'
    def __init__(self, main, ui, pgcon=None, client=None, constatus=False, config=None):
        self.main = main
        self.ui = ui
        self.pgcon = pgcon
        self.client = client
        self.constatus = constatus
        self.config = config

        if constatus:
            self.main.infoWgt = HomeWidget(self.main, self.ui, self.pgcon)
            self.ui.btnOkStart.clicked.connect(self.actAuStart)
            self.ui.btnResStart.clicked.connect(self.start)
        else:
            self.ui.btnOkStart.setDisabled(True)
            self.ui.btnResStart.setDisabled(True)
            self.ui.auSaveCh.setDisabled(True)
            self.ui.userNameStart.setDisabled(True)
            self.ui.userPassStart.setDisabled(True)
        erroeMsg = self.main.errorStatus.split(',')
        for msg in erroeMsg:
            if msg == 'SetSQL':
                msgInfo('Необходимо проверить настройки базы данных')
            # elif msg == 'SetMqtt':
            #     msgInfo('Необходимо проверить настройки MQTT')
            elif msg == 'ConSQL':
                msgInfo('Не удалось соеденится с базой данных')
            # elif msg == 'ConMqtt':
            #     msgInfo('Не удалось соеденится с MQTT')
            # self.ui.btnRestartStart.clicked.connect(self.main.restart)
            # self.ui.btnCloseStart.clicked.connect(self.main.close)
            # self.ui.btnSetStart.clicked.connect(self.startSeting)
    #         self.start()

    def start(self):
        'Заполнение сохраненного логина пароля'
        if self.config is not None and "APP" in self.config:
            app_config = self.config["APP"]
            loginIni = app_config.get("login", "")
            passwordIni = app_config.get("password", "")
            savePass = bool(app_config.get("savepass", False))

            self.ui.userNameStart.setText(loginIni)
            self.ui.userPassStart.setText(passwordIni)
            self.ui.auSaveCh.setChecked(savePass)
        else:
            # Обработка случая, когда конфигурация не загружена или отсутствуют ключи
            loginIni, passwordIni = '', ''
            savePass = False

            self.ui.userNameStart.setText(loginIni)
            self.ui.userPassStart.setText(passwordIni)
            self.ui.auSaveCh.setChecked(savePass)

    def actAuStart(self):
        'Действие при нажатии на кнопку войти'
        login = self.ui.userNameStart.text()
        password = self.ui.userPassStart.text()
        try:
            cursor = self.pgcon.cursor()
            cursor.execute(
                f'SELECT username, password, role, enable FROM "{self.main.DBuserapp}" WHERE (username=\'{login}\' AND password=\'{password}\')')
            query_out = cursor.fetchall()
            if len(query_out) != 0:
                if query_out[0][3] == True:
                    cursor.execute(
                        f'SELECT appau, dir_ed, repo_on, user_ed, org_ed, set_app, set_org, set_repo FROM "{self.main.DBapprole}" WHERE role=\'{query_out[0][2]}\'')
                    query_out = cursor.fetchall()
                    setRoleAppAu = query_out[0][0]
                    if setRoleAppAu:
                        self.main.setRoleDirEd = query_out[0][1]
                        self.main.setRoleRepoRepOn = query_out[0][2]
                        self.main.setRoleUserEd = query_out[0][3]
                        self.main.setRoleOrgEd = query_out[0][4]
                        self.main.setRoleSetApp = query_out[0][5]
                        self.main.setRoleSetOrg = query_out[0][6]
                        self.main.setRoleSetRepo = query_out[0][7]
                        self.main.ui.stackedWidget.setCurrentIndex(0)
                        for btns in self.main.btn:
                            btns.setDisabled(False)
                        self.main.btnHome.setDisabled(True)

                        self.main.userWgt = UserWidget(self.main, self.ui, self.pgcon, self.client)
                        self.main.repoWdt = RepoWidget(self.main, self.ui, self.pgcon)
                        self.main.dirWdt = DirWidget(self.main, self.ui, self.pgcon)
                        self.main.organizationWdt = OrganizationWidget(self.main, self.ui, self.pgcon)
                        self.main.infoWgt = InfoWidget(self.main, self.ui)
                        self.main.setWgt = SetConnect(self.main, self.ui, False, self.config)

                        if self.ui.auSaveCh.isChecked():
                            self.config["APP"]["login"] = login
                            self.config["APP"]["password"] = password
                            self.config["APP"]["savepass"] = '1'
                        else:
                            self.config["APP"]["login"] = ''
                            self.config["APP"]["password"] = ''
                            self.config["APP"]["savepass"] = ''
                        path = "settings.ini"
                        with open(path, "w") as config_file:
                            self.config.write(config_file)
                    else:
                        self.ui.auLabInfo.setText('! Нет прав на вход, обратитесь к администртору!')
                else:
                    self.ui.auLabInfo.setText('! Нет прав на вход, обратитесь к администртору!')
            else:
                self.ui.auLabInfo.setText('! Не верно введен логин, или пароль!')
        except Exception as e:
                msgInfoError(f'Внимание, связь с SQL сервером потеряна. Перезагрузить приложение?\nОшибка: {str(e)}')

    def startSeting(self):
        'Действие кнопки настройки'
        self.main.setStart = SetConnect(self.main, self.ui, True, self.config)
        self.main.ui.stackedWidget.setCurrentIndex(6)