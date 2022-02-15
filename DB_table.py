from datetime import datetime

class Log:

    def __init__(self, ip:str, acstime:datetime, url:str) -> None:
        self.ip:str = ip
        self.acstime:datetime = acstime
        self.url:str = url


class Scroll_Data():
    def __init__(self, ip:str, acstime:datetime, url:str, staytime:int, scroll:int) -> None:
        self.ip = ip
        self.acstime = acstime
        self.url = url
        self.staytime = staytime
        self.scroll = scroll


if __name__ == "__main__":

    ...
