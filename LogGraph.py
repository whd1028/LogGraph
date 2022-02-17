import numpy as np
import pandas as pd
import re
# from collections import defaultdict as Ddict
import matplotlib.pyplot as plt
from SqlConn import SqlConn
from DB_table import Log, Scroll_Data
from typing import Tuple


class LogGraph():

    # 쿼리문을 실행하여 데이터 얻어오기
    @staticmethod
    def selectData(query: str) -> list:
        cursor = SqlConn.Cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        return results

    @staticmethod  # 사용자(개인,회원)이 많이 읽은 언론사 TOP 5
    def make_graph_individual_like_press(user_id: str) -> pd.DataFrame:
        # 1. Log에서 특정 사용자의 URL기록을 얻어온다.
        query_URL = f"select URL from Log inner join memberinfo  as m on Log.user_id = m.id where Log.user_id = '{user_id}'"
        urls = LogGraph.selectData(query_URL)
        
        # 2. 얻어온 URL에서 기사의 n_id를 추출한 값을 이용해 언론사를 검색한다.
            # urls_df = pd.DataFrame(urls, columns=['URL'])
            # urls_df['URL'] = urls_df['URL'].apply(lambda x: re.search("/news/news_post/([0-9]*)",x).group(1))
        query_pid = f"select p_id from News where n_id in ("
        for url in urls:
            query_pid += "\'" + re.search("/news/news_post/([0-9]*)", url[0]).group(1) + "\'" + ","
        query_pid = query_pid[:-1]
        query_pid += ")"

        pid_list = LogGraph.selectData(query_pid)

        # 3. 언론사별로 횟수를 기록하고 많이 기록된 순으로 5개를 반환한다.
        # ddict = Ddict(int)
        # for pid in pid_list:
        #     ddict[pid[0]] += 1
        
        # return ddict
        pid_df = pd.DataFrame(pid_list, columns=['pid'])
        return pid_df.value_counts().iloc[:5]
    
    @staticmethod  # 사용자(개인,회원)이 많이 읽은 카테고리 TOP 5
    def make_graph_individual_like_category(user_id: str) -> pd.DataFrame:
        # 1. Log테이블에서 특정 사용자의 URL기록을 얻어온다.
        query_URL = f"select URL from Log inner join memberinfo  as m on Log.user_id = m.id where Log.user_id = '{user_id}'"
        urls = LogGraph.selectData(query_URL)

        # 2. 얻어온 URL에서 기사의 n_id를 추출한 값을 이용해 News테이블에 있는 해당기사의 카테고리를 얻어온다.
        query_cdid = f"select cd_id from News where n_id in ("
        for url in urls:
            query_cdid += "\'" + re.search("/news/news_post/([0-9]*)", url[0]).group(1) + "\'" + ","  # n_id값을 URL에서 추출해서 쿼리문의 조건문에 추가
        query_cdid = query_cdid[:-1]
        query_cdid += ")"

        cdid_list = LogGraph.selectData(query_cdid)

        # 3. 카테고리별로 기록횟수를 세고 큰 숫자 순으로 5개를 반환한다.
        cdid_df = pd.DataFrame(cdid_list, columns=['cdid'])
        return cdid_df.value_counts().iloc[:5]

    @staticmethod  # 회원들의 성별 많이 읽은 뉴스기사 TOP 5
    def make_graph_gender_like_news() -> Tuple[pd.Series,pd.Series]:
        # 1. Log테이블에서 user_id가 있는 모든 사용자들의 URL을 얻어온다.
        query_URL = f"select Log.URL, m.sex from Log inner join memberinfo  as m on Log.user_id = m.id "
        urls_sex = LogGraph.selectData(query_URL)

        # 2. 얻어온 URL에서 기사의 n_id를 얻어온다.
        urls_sex_df = pd.DataFrame(urls_sex, columns=['URL', 'sex'])
        urls_sex_df['URL'] = urls_sex_df['URL'].apply(lambda x: re.search("/news/news_post/([0-9]*)",x).group(1))
        urls_sex_df.rename(columns={'URL':'nid'}, inplace=True) # URL에서 nid를 추출했으니 컬럼 이름도 바꿔주자

        # 3. 성별 n_id를 카운트한다.
        male_series = urls_sex_df[urls_sex_df['sex'] == '남자'].value_counts()
        female_series = urls_sex_df[urls_sex_df['sex'] == '여자'].value_counts()
        return (male_series, female_series)
        # gender_df = pd.DataFrame(data={'male':male_series, 'female':female_series})
        # test = urls_sex_df.value_counts()
        ...

    @staticmethod  # 회원들의 연령대(10,20,30,40,50)별 많이 읽은 뉴스기사 TOP 5
    def make_graph_age_like_news() -> pd.DataFrame:
        # 1. 모든 회원들의 로그에서 URL(/news_post/<n_id>)*과 생년일을 얻어온다.(*{n_id값 추출할 예정})
        query = f"select l.URL, m.birth from Log as l inner join memberinfo as m on l.user_id = m.id"
        url_birth = LogGraph.selectData(query)

        # 2. 연령대별로 인원 구하기
        url_birth_df = pd.DataFrame(url_birth, columns=['URL', 'birth'])
        url_birth_df['URL'] = url_birth_df['URL'].apply(lambda x: re.search("/news/news_post/([0-9]*)",x).group(1))
        url_birth_df.rename(columns={'URL':'nid'}, inplace=True) # URL에서 nid를 추출했으니 컬럼 이름도 바꿔주자

        


        ...

    ...
    

if __name__ == "__main__":
    # print(LogGraph.make_graph_individual_like_press('park_test'))
    print(*LogGraph.make_graph_gender_like_news())
    
    ...
