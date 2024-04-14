#Виджет дом
import random
from random import randint
from datetime import date, timedelta
from userApp.widget.msg import *


class HomeWidget:
    'Окно информация о системе'
    def __init__(self, main, ui, pgcon):
        self.main = main
        self.ui = ui
        self.pgcon = pgcon
        self.page_Home()

    def page_Home(self):
        day = date.today().day
        try:
            cursor = self.pgcon.cursor()
            cursor.execute(f'SELECT count(*) FROM "{self.main.DBuser}"')
            self.ui.infoAllUser.setText(f'Всего стортудников в базе данных: {cursor.fetchall()[0][0]}')
            cursor.execute(f'SELECT count(*) FROM "{self.main.DBuid}"')
            self.ui.infoAllUid.setText(f'Всего UID в базе данных: {cursor.fetchall()[0][0]}')
            cursor.execute(f'SELECT count(DISTINCT user_id) FROM "{self.main.DBrecords}" RIGHT JOIN "{self.main.DBuid}" ON "{self.main.DBrecords}".uid = "{self.main.DBuid}" .uid WHERE data = \'{date.today()}\'')
            self.ui.infoInDay.setText(f'Всего сотрудников отметилось сегодня: {cursor.fetchall()[0][0]}')
            cursor.execute(f'SELECT count(*) FROM "{self.main.DBrecords}" WHERE data = \'{date.today()}\'')
            self.ui.infoInUserDay.setText(f'Всего раз отметились сегодня: {cursor.fetchall()[0][0]}')
            cursor.execute(f'SELECT count(*) FROM "{self.main.DBrecords}" WHERE (data BETWEEN \'{date.today() - timedelta(days=7)}\' AND \'{date.today()}\')')
            self.ui.infoInUserWeek.setText(f'Всего раз отметились за неделю: {cursor.fetchall()[0][0]}')
            cursor.execute(f'SELECT count(*) FROM "{self.main.DBrecords}" WHERE (data BETWEEN \'{date.today() - timedelta(days=day)}\' AND \'{date.today()}\')')
            self.ui.infoInUserMonth.setText(f'Всего раз отметились за текущий месяц: {cursor.fetchall()[0][0]}')
            cursor.execute(f'SELECT count(*) FROM "{self.main.DBrecords}"')
            cursor.close()
        except:
            msgInfoError('Внимание, связь с SQL сервером потеряна, перезагрузить приложение?')