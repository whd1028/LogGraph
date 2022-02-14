#dataObject
from datetime import datetime
from SqlConn import SqlConn
from typing import List

class Log:

    def __init__(self, ip:str, acstime:datetime, url:str) -> None:
        self.ip:str = ip
        self.acstime:datetime = acstime
        self.url:str = url


    @staticmethod
    def selectData(user_id:str =None, ip: str =None, time1: str =None, time2: str =None, limit: int=None, order: str ='DESC') -> list :
        if not any([user_id, ip, time1, time2, limit]):
            return Log.selectAll()
        elif user_id != None:
            return Log.selectByUserID(user_id)
        elif ip != None:
            return Log.selectByip(ip, limit=limit)
        elif time1 != None:
            return Log.selectBytime(time1, time2, order=order)
        ...

    @staticmethod
    def selectByUserID(user_id: str) -> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Log where id = '{user_id}'"
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url in results:
            object_list.append(Log(ip, acstime, url))

        return object_list
        ...

    @staticmethod
    def selectAll() -> None:
        cursor = SqlConn.Cursor()
        query = f"select * from Log "
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url in results:
            object_list.append(Log(ip, acstime, url))

        return object_list

    @staticmethod
    def selectByip(ip:str, limit:int=None) -> list:
        cursor = SqlConn.Cursor()
        # query = str.format("select * from Log where IPaddr = {0}",ip)
        if limit != None:
            query = f"select * from Log where IPaddr = '{ip}' limit {limit}"
        else:    
            query = f"select * from Log where IPaddr = '{ip}'"
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url in results:
            object_list.append(Log(ip, acstime, url))
            
        return object_list

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
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url in results:
            object_list.append(Log(ip, acstime, url))
            
        return object_list
    
    
class Scroll_Data():
    def __init__(self, ip:str, acstime:datetime, url:str, staytime:int, scroll:int) -> None:
        self.ip = ip
        self.acstime = acstime
        self.url = url
        self.staytime = staytime
        self.scroll = scroll

    @staticmethod
    def selectData(ip: str =None, url: str =None, n_id: str =None, limit: int =None) -> list or None:
        if not any([ip, url, n_id]):
            return Scroll_Data.selectAll()
        elif ip != None:
            return Scroll_Data.selectByip(ip=ip, limit=limit)
        elif url != None:
            return Scroll_Data.selectByURL(url=url)
        elif n_id != None:
            return Scroll_Data.selectByn_id(n_id=n_id)
        ...
    

    @staticmethod
    def selectAll() -> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Scroll_Data"
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url, staytime, scroll in results:
            object_list.append(Scroll_Data(ip, acstime, url, staytime, scroll))

        return object_list

    @staticmethod
    def selectByip(ip:str, limit:int=None) -> list :
        cursor = SqlConn.Cursor()
        # query = str.format("select * from Scroll_Data where ipaddr = {0}",ip)
        if limit != None:
            query = f"select * from Scroll_Data where ipaddr = '{ip}' limit {limit}"
        else:    
            query = f"select * from Scroll_Data where ipaddr = '{ip}'"
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url, staytime, scroll in results:
            object_list.append(Scroll_Data(ip, acstime, url, staytime, scroll))

        return object_list

    @staticmethod
    def selectByURL(url:str)-> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Scroll_Data where URL = '{url}'"
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url, staytime, scroll in results:
            object_list.append(Scroll_Data(ip, acstime, url, staytime, scroll))

        return object_list

    @staticmethod
    def selectByn_id(n_id:str) -> list:
        cursor = SqlConn.Cursor()
        query = f"select * from Scroll_Data where URL = 'news/news_post/{n_id}'"
        cursor.execute(query)
        results = cursor.fetchall()
        object_list = []
        for ip, acstime, url, staytime, scroll in results:
            object_list.append(Scroll_Data(ip, acstime, url, staytime, scroll))

        return object_list

    @staticmethod
    def selectNewsRank(n_id:str) -> None:
        ...
    ...

if __name__ == "__main__":
    # print(Log.selectByip('127.0.0.1'))
    # print(len(Log.selectAll()))
    # print(Log.selectData())
    print(__name__, __package__, __spec__, __annotations__, __file__, __builtins__)
    check = Log.__mro__
    check2 = Log.selectAll.__qualname__
    # print( [] == None)
    # Log.tt()
    Log.selectAll()
    ...
