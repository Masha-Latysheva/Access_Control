# Виджет отчетов
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from userApp.widget.msg import *
from datetime import datetime

class RepoWidget:
    'Окно сотрудники'
    def __init__(self, main, ui, pgcon):
        self.main = main
        self.ui = ui
        self.pgcon = pgcon
        self.dictType = {}
        self.dictTypes = {}
        self.dictJob = {}
        self.dictJobs = {}
        self.dictStructur = {}
        self.dictStructurs = {}
        # self.ui.btnEXELRepo.clicked.connect(self.exportToExcel)
        #self.ui.btnDOCXRepo.clicked.connect(self.exportToWord)
        # self.ui.btnPDFRepo.clicked.connect(self.exportToPDF)
        self.ui.btnSearchRepo.clicked.connect(self.tableSQL)
        # self.ui.btnResetRepo.clicked.connect(self.resetRepo)
        self.ui.tableViewRepo.cellClicked.connect(self.viewInfo)
        self.ui.tableViewRepo.setColumnWidth(0, 120)
        self.ui.tableViewRepo.setColumnWidth(1, 340)
        self.ui.tableViewRepo.setColumnWidth(2, 90)
        self.ui.tableViewRepo.setColumnWidth(3, 90)
        self.ui.tableViewRepo.setColumnWidth(4, 120)
        self.ui.tableViewRepo.setColumnWidth(5, 120)
        self.ui.tableViewRepo.setColumnWidth(6, 120)
        self.ui.tableViewRepo.setColumnWidth(7, 120)
        self.ui.tableViewRepo.setColumnWidth(8, 120)
        self.ui.tableViewRepo.setHorizontalHeaderLabels(
            ['UID чипа', 'Фамилия Имя Отчество', 'Дата', 'Время', 'Место отметки', 'Подразделение', 'Должность',
             'Тип работника', 'Ссылка'])
        self.resetRepo()

    def viewInfo(self):
        self.curentFio = self.ui.tableViewRepo.item(self.ui.tableViewRepo.currentRow(), 1).text()
        self.ui.textFioRepo.setText(self.curentFio)

    def resetRepo(self):
            self.update()
            self.ui.textUidRepo.setText('')
            self.ui.textFioRepo.setText('')
            self.ui.edData1Repo.setDate(datetime.now().date())
            self.ui.edData2Repo.setDate(datetime.now().date())
            self.ui.edTime1Repo.setTime(QtCore.QTime(00, 00, 00))
            self.ui.edTime2Repo.setTime(QtCore.QTime(23, 59, 59))
            self.tableSQL()

    def tableSQL(self):
            'Табица отображения результатов'
            try:
                cursor = self.pgcon.cursor()
                self.ui.tableViewRepo.setSortingEnabled(False)
                self.qu_data_start = self.ui.edData1Repo.date().toPyDate()
                self.qu_data_end = self.ui.edData2Repo.date().toPyDate()
                self.qu_time_start = self.ui.edTime1Repo.time().toPyTime()
                self.qu_time_end = self.ui.edTime2Repo.time().toPyTime()

                type = self.dictTypes.get(self.ui.boxTypeRepo.currentText())
                job = self.dictJobs.get(self.ui.boxJobRepo.currentText())
                struct = self.dictStructurs.get(self.ui.boxStructurRepo.currentText())
                uid = self.ui.textUidRepo.displayText()
                fio = self.ui.textFioRepo.displayText()
                #####
                quSelect = f'SELECT query_in_2.uid, fio, data, time, topic_name, structsub, jobtype, worktype, ref'
                quFrom = f'FROM'
                quSelUser1 = f'(SELECT uid, fio, structsub, jobtype, worktype, ref FROM "{self.main.DBuser}" '
                quSelUser2 = f'INNER JOIN "{self.main.DBuid}" ON "{self.main.DBuser}".id = "{self.main.DBuid}".user_id'
                quSelUser3 = f'INNER JOIN "{self.main.DBjob}" ON "{self.main.DBuser}".job_id = "{self.main.DBjob}".id'
                quSelUser4 = f'INNER JOIN "{self.main.DBtype}" ON "{self.main.DBuser}".type_id = "{self.main.DBtype}".id'
                quSelUser5 = f'INNER JOIN "{self.main.DBstructsub}" ON "{self.main.DBuser}".structsub_id = "{self.main.DBstructsub}".id'
                quSelUser6 = f'INNER JOIN "{self.main.DBref}" ON"{self.main.DBuser}".ref_id = "{self.main.DBref}".id'
                quWhere = f'WHERE'
                quWhereFio = f'fio LIKE \'%{fio}%\''
                quUserfinish = f')query_in_1'
                quUid1 = f'JOIN (SELECT uid, data, time, topic_name FROM "{self.main.DBrecords}"'
                quUid2 = f'INNER JOIN "{self.main.DBtopic}" ON "{self.main.DBrecords}".topic = "{self.main.DBtopic}".topic'
                quWhereData = f'WHERE (data BETWEEN \'{self.qu_data_start}\' AND \'{self.qu_data_end}\') AND (time BETWEEN \'{self.qu_time_start}\' AND \'{self.qu_time_end}\')'
                quWhereUid = f'uid LIKE \'%{uid}%\''
                quEnd = f') query_in_2 ON query_in_1.uid = query_in_2.uid'
                quAND1, quAND2, quWhereType, quWhereJob, quWhereStr, quRigh = '', '', '', '', '', ''

                if type != None:
                    quWhereType = f'AND "{self.main.DBuser}".type_id = \'{type}\''
                if job != None:
                    quWhereJob = f'AND "{self.main.DBuser}".job_id = \'{job}\''
                if struct != None:
                    quWhereStr = f'AND "{self.main.DBuser}".structsub_id = \'{struct}\''
                if self.ui.chhNoneRepo.isChecked():
                    quRigh = 'RIGHT'
                queryWhereUser = f'{quWhere} {quWhereFio} {quWhereType} {quWhereJob} {quWhereStr}'
                queryWhereUid = f'{quWhereData} AND {quWhereUid}'

                query = f'{quSelect} {quFrom} {quSelUser1} {quSelUser2} {quSelUser3} {quSelUser4} {quSelUser5} {quSelUser6} {queryWhereUser} {quUserfinish} {quRigh} {quUid1} {quUid2} {queryWhereUid} {quEnd}'
                cursor.execute(query)
                query_out = cursor.fetchall()
                self.tablerow, rowCount = 0, 0
                self.ui.tableViewRepo.setRowCount(rowCount)
                for i in query_out:
                    rowCount += 1
                    self.ui.tableViewRepo.setRowCount(rowCount)
                    self.ui.tableViewRepo.setItem(self.tablerow, 0, QTableWidgetItem(str(i[0])))  # UID чипа
                    self.ui.tableViewRepo.setItem(self.tablerow, 1, QTableWidgetItem(str(i[1])))  # Фамилия Имя Отчество
                    self.ui.tableViewRepo.setItem(self.tablerow, 2, QTableWidgetItem(str(i[2])))  # Дата
                    self.ui.tableViewRepo.setItem(self.tablerow, 3, QTableWidgetItem((str(i[3])[:8])))  # Время
                    self.ui.tableViewRepo.setItem(self.tablerow, 4, QTableWidgetItem(str(i[4])))  # Место отметки
                    self.ui.tableViewRepo.setItem(self.tablerow, 5, QTableWidgetItem(str(i[5])))  # Подразделение
                    self.ui.tableViewRepo.setItem(self.tablerow, 6, QTableWidgetItem(str(i[6])))  # Должность
                    self.ui.tableViewRepo.setItem(self.tablerow, 7, QTableWidgetItem(str(i[7])))  # Тип работника
                    self.ui.tableViewRepo.setItem(self.tablerow, 8, QTableWidgetItem(str(i[8])))  # Ссылка
                    self.tablerow += 1
                self.pgcon.commit()
                cursor.close()
                self.ui.tableViewRepo.setSortingEnabled(True)
            except Exception as e:
                msgInfoError(f'Внимание, связь с SQL сервером потеряна. Перезагрузить приложение?\nОшибка: {str(e)}')
    # def exportToExcel(self):
    #     noneFunc()
    #
    # def exportToWord(self):
    #     self.docxUi = DocxExport(self, self.main, self.ui, self.pgcon)
    #
    # def exportToPDF(self):
    #     noneFunc()

    def boxStructurs(self, setitem=None):
        'Функция отображения комбобокса структурных подразделений'
        try:
            cursor = self.pgcon.cursor()
            cursor.execute(f'SELECT structsub, id FROM {self.main.DBstructsub}')
            sqlout = list(cursor)
            self.dictStructur = {}
            self.dictStructurs = {}
            out, outfor = list(), list()
            out.append('Все')
            for i in sqlout:
                outfor.append(i[0])
                self.dictStructurs[i[0]] = i[1]
                self.dictStructur[i[1]] = i[0]
            outfor.sort()
            out += outfor
            self.listToDoc = outfor
            self.ui.boxStructurRepo.clear()
            self.ui.boxStructurRepo.addItems(out)
            self.pgcon.commit()
            if setitem != None:
                index = self.ui.boxStructurRepo.findText(self.dictStructur.get(setitem))
                if index >= 0:
                    self.ui.boxStructurRepo.setCurrentIndex(index)
            cursor.close()
        except Exception as e:
            msgInfoError(f'Внимание, связь с SQL сервером потеряна. Перезагрузить приложение?\nОшибка: {str(e)}')

    def boxJobs(self, setitem=None):
        'Функция отображения комбобокса должностей'
        try:
            cursor = self.pgcon.cursor()
            cursor.execute(f'SELECT jobtype, id FROM {self.main.DBjob}')
            sqlout = list(cursor)
            self.dictJob = {}
            self.dictJobs = {}
            out, outfor = list(), list()
            out.append('Все')
            for i in sqlout:
                outfor.append(i[0])
                self.dictJobs[i[0]] = i[1]
                self.dictJob[i[1]] = i[0]
            outfor.sort()
            out += outfor
            self.ui.boxJobRepo.clear()
            self.ui.boxJobRepo.addItems(out)
            self.pgcon.commit()
            if setitem != None:
                index = self.ui.boxJobRepo.findText(self.dictJob.get(setitem))
                if index >= 0:
                    self.ui.boxJobRepo.setCurrentIndex(index)
            cursor.close()
        except Exception as e:
            msgInfoError(f'Внимание, связь с SQL сервером потеряна. Перезагрузить приложение?\nОшибка: {str(e)}')

    def boxTypes(self, setitem=None):
        'Функция отображения комбобокса типов сотрудников'
        try:
            cursor = self.pgcon.cursor()
            cursor.execute(f'SELECT worktype, id FROM {self.main.DBtype}')
            self.dictType = {}
            self.dictTypes = {}
            sqlout = list(cursor)
            out, outfor = list(), list()
            out.append('Все')
            for i in sqlout:
                outfor.append(i[0])
                self.dictType[i[1]] = i[0]
                self.dictTypes[i[0]] = i[1]
            outfor.sort()
            out += outfor
            self.ui.boxTypeRepo.clear()
            self.ui.boxTypeRepo.addItems(out)
            self.pgcon.commit()
            if setitem != None:
                index = self.ui.boxType.findText(self.dictType.get(setitem))
                if index >= 0:
                    self.ui.boxType.setCurrentIndex(index)
            cursor.close()
        except Exception as e:
            msgInfoError(f'Внимание, связь с SQL сервером потеряна. Перезагрузить приложение?\nОшибка: {str(e)}')

    def update(self):
         self.boxStructurs()
         self.boxJobs()
         self.boxTypes()