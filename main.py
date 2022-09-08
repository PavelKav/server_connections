import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#import psycopg2
#from conf import host, user, password, db_name
from gui01 import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cat_web.clicked.connect(self.watch_category)
        # self.ui.cat_pk.clicked.connect(self.connect_serv)


    def watch_category(self):
        # self.ui.listWidget.currentItem().text()
        self.ui.listWidget.addItem('login')
    '''    
    def connect_serv(self):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
            )
            connection.autocommit = True

        # info server
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT version();"
                )
                self.ui.plainTextEdit.appendPlainText(f"Server version: {cursor.fetchone()}")

        finally:
            if connection:
                connection.close()
                self.ui.plainTextEdit.appendPlainText("[INFO] PostgreSQL connection closed")
    '''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
