#sqlConn.py
import mysql.connector  # pip install mysql-connector-python

class SqlConn:
    hostlink = 'finalproject-2.c4jotwudvoiz.ap-northeast-2.rds.amazonaws.com'
    conn = mysql.connector.connect(host = hostlink, port = '3306', user='admin', password='12341234', database='News_Summary')  # 해당 인자도 다 변수로 사용할 수 있으면 좋다

    @staticmethod
    def Cursor():
        return SqlConn.conn.cursor()

    @staticmethod
    def Close():
        SqlConn.conn.close()

    @staticmethod
    def Commit():
        SqlConn.conn.commit()