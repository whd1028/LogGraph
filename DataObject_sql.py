#dataObject
from datetime import datetime
from SqlConn import SqlConn

class Log:

    def __init__(self, ip:str, acstime:datetime, url:str) -> None:
        self.ip:str = ip
        self.acstime:datetime = acstime
        self.url:str = url

    @staticmethod
    def selectAll() -> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Log "
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    @staticmethod
    def selectByip(ip:str, limit:int=None) -> list:
        cursor = SqlConn.Cursor()
        # query = str.format("select * from Log where IPaddr = {0}",ip)
        if limit != None:
            query = f"select * from Log where IPaddr = '{ip}' limit {limit}"
        else:    
            query = f"select * from Log where IPaddr = '{ip}'"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    @staticmethod
    def selectBytime(time1:str, time2:str=None, order:str='DESC') -> list:
        cursor = SqlConn.Cursor()
        if time2 == None:
            query = f"select * from Log where acstime > '{time1}' order by acstime {order}"
            ...
        else:
            query = f"select * from Log where acstime > '{time1}' and acstime < '{time2}' order by acstime {order}"
            ...
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    
    
class Scroll_Data():
    def __init__(self, ip:str, acstime:datetime, url:str, staytime:int, scroll:int) -> None:
        self.ip = ip
        self.acstime = acstime
        self.url = url
        self.staytime = staytime
        self.scroll = scroll
    
    @staticmethod
    def selectAll() -> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Scroll_Data"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    @staticmethod
    def selectByURL(url:str)-> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Scroll_Data where URL = '{url}'"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    @staticmethod
    def selectByn_id(n_id:str) -> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Scroll_Data where URL = 'news/news_post/{n_id}'"
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    ...

if __name__ == "__main__":
    # print(len(Log.selectByip('127.0.0.1')))
    # print(len(Log.selectAll()))

    ...
    