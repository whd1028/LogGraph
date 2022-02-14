import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from DataObject_sql import Log, Scroll_Data


class LogGraph():
    
    @staticmethod  # 사용자(개인)이 선호하는 언론사
    def make_graph_individual_like_press():
        
        ...
    
    @staticmethod  # 사용자(개인)이 선호하는 카테고리
    def make_graph_individual_like_category():
        ...

    @staticmethod  # 사용자 성별 선호하는 뉴스기사
    def make_graph_gender_like_news():
        ...

    @staticmethod  # 연령대별 선호하는 뉴스기사
    def make_graph_age_like_news():
        ...


    @staticmethod
    def select_Data(dataObject:str, **keyarg) -> pd.DataFrame:
        str = f"{dataObject}.selectData(**{keyarg})"
        return eval(str)
        ...

    @staticmethod
    def make_poltGraph(data, x, y) -> None:
        data_list = LogGraph.select_Data(data)
        ...

    @staticmethod
    def make_barGraph() -> None:
        ...

    @staticmethod
    def make_pieGraph() -> None:
        ...

    @staticmethod
    def show_Graph() -> None:
        ...

    @staticmethod
    def save_Graph(path: str) -> None:
        ...

if __name__ == "__main__":
    # print(LogGraph.select_Data("Log",ip="183.98.215.85",limit=100))
    data_list = LogGraph.select_Data("Log")
    plot_df = pd.DataFrame()
    for i in data_list:
        plot_df.append(i.__dict__, ignore_index=True)
    print(plot_df)

    ...

