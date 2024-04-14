# from PyQt6 import QtWidgets,QtSql
#
# class Data:
#     def __init__(self):
#         super(Data,self).__init__()
#
#     def create_connection(self):
#         db = QtSql.QSqlDatabase.addDatabase("SQL")
#         db.setDatabaseName('Access_Control.db')
#         if not db.open():
#             QtWidgets.QMessageBox.critical(None, "Cannot open database", "Click cancel to exit", QtWidgets.QMessageBox.Cansel())
#             return False
#
#         query = QtSql.QSqlQuery
#         query.exec("CREATE TABLE IS NOT EXISTS")
#         return True
#
#     def execute_query_with_params(self, sql_query, query_values=None):
#         query = QtSql.QSqlQuery()
#         query.prepare(sql_query) #объеденяет параметры и сам запрос
#
#         if query_values is not None:
#             for query_value in query_values:
#                 query.addBindValue(query_value)
#
#         query.exec()
#
#         def add_new_transaction_query(self, date,category, ...): #добавление в бд
#             sql_query = "INSERT INTO expenses (Date, Category, ....) values (?, ?, ....)"
#             self.execute__query_with_params(sql_query, [date, category,....])
#
#         def update_transaction_query(self, date,category, ...id): #изменение в бд
#             sql_query = "UPDATE expenses SET Date = ?, Category = ?, .... WHERE ID=?"
#             self.execute__query_with_params(sql_query, [date, category,...., id])
#
#         def delete_transaction_query(self, id): #удаление в бд
#             sql_query = "DELETE FROM expenses WHERE ID=?"
#             self.execute__query_with_params(sql_query, [id])
#
#
