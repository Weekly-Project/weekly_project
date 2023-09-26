import pandas as pd
import matplotlib.pyplot as plt


class SNS:
    def __init__(self, sns_2019, sns_2021, sns_2023):
        self.sns_2019 = sns_2019
        self.sns_2021 = sns_2021
        self.sns_2023 = sns_2023
        plt.rcParams['font.family'] = 'NanumGothic'
        plt.figure(figsize=(10, 5))
        plt.yticks(range(0, 31000, 5000))

    def load_data(self, file):
        return pd.read_csv(file, encoding='EUC-KR')

    def plot_graph(self):
        sns_2019 = self.load_data(self.sns_2019)
        sns_2021 = self.load_data(self.sns_2021)
        sns_2023 = self.load_data(self.sns_2023)

        plt.plot(sns_2019['기준연월'], sns_2019['검색량(건)'], marker='o', linestyle='-', color='blue', label='2018-19년')
        plt.plot(sns_2021['기준연월'], sns_2021['검색량(건)'], marker='o', linestyle='-', color='grey', label='2020-21년')
        plt.plot(sns_2023['기준연월'], sns_2023['검색량(건)'], marker='o', linestyle='-', color='red', label='2022-23년')

        plt.title('경기도 용인시 처인구 검색량 월별 변화')
        plt.xlabel('월별 (자료 출처: 한국 관광공사)', labelpad=10)
        plt.ylabel('검색량', rotation=0, labelpad=10)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        
        return plt

if __name__ == "__main__":
    sns_2019_file = '/utils/sns_yongin/sns_yongin_2019.csv'
    sns_2021_file = '/utils/sns_yongin/sns_yongin_2021.csv'
    sns_2023_file = '/utils/sns_yongin/sns_yongin_2023.csv'
    
    graph = SNS(sns_2019_file, sns_2021_file, sns_2023_file)
    graph.plot_graph()

 