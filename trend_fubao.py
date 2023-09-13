import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

class TrendFubao:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, encoding='cp949')
        self.df['날짜'] = pd.to_datetime(self.df['날짜'])
        self.df.set_index('날짜', inplace=True)

    def plot_monthly_search_volume(self):
        monthly = self.df.resample('M').sum()

        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
        # 월별 검색량 그래프 그리기
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(monthly.index.to_numpy().reshape(-1, 1), monthly['검색량'].to_numpy(), marker='o', linestyle='-')
        ax.set_xlabel('월')
        ax.set_ylabel('검색량 합계')
        ax.set_title("월별 '푸바오' 검색량 추이")

        date_format = DateFormatter("%Y-%m")
        ax.xaxis.set_major_formatter(date_format)

        plt.xticks(monthly.index)
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    tf = TrendFubao('trend_fubao.csv')
    tf.plot_monthly_search_volume()
