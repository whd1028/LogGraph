from SqlConn import SqlConn
from random import choice, randrange

def insert_memberinfo(num: int=10) -> None:
    query = "insert into memberinfo (id, password, name, birth, sex, email, phone) values "
    dummy_data = ""
    for i in range(num):
        dummy_data += f"('park_test_{i}', '12341234', 'park{i}', '{randrange(1990,2020)}-01-01 00:00:00', '{choice(['남자','여자'])}', 'test@test{i}.com', '010-123-456')"
        dummy_data += ","
    dummy_data = dummy_data[:-1] + ";"
    query += dummy_data

    cursor = SqlConn.Cursor()
    cursor.execute(query)
    SqlConn.Commit()


def delete_memberinfo():
    query = 'delete from memberinfo where id like "park_test_%"'
    cursor = SqlConn.Cursor()
    cursor.execute(query)
    SqlConn.Commit()

def insert_Log(num: int=10):
    query = "insert into Log (IPaddr, acstime, URL, user_id) values "
    dummy_data = ""
    for _ in range(num):
        dummy_data += f"('0.0.0.0', now(), '/news/news_post/{randrange(1,100,2)}', 'park_test_{randrange(0,num)}')"
        dummy_data += ","
    dummy_data = dummy_data[:-1] + ";"
    query += dummy_data

    cursor = SqlConn.Cursor()
    cursor.execute(query)
    SqlConn.Commit()

def delete_Log():
    query = 'delete from Log where user_id like "park_test_%"'
    cursor = SqlConn.Cursor()
    cursor.execute(query)
    SqlConn.Commit()


if __name__ == "__main__":
    # insert_memberinfo(100)
    # delete_memberinfo()

    # insert_Log(100)
    # delete_Log()
    print(choice(['생선구이', '돼지국밥', '라멘', '돈까스', '짜장면', '1층 뷔페', '언더그라운드', '칼국수', '하노이의 아침(쌀국수)']))
    ...

