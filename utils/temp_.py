import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as font_manager

class Temp:
    def __init__(self, font_path='NanumGothic.ttf'):
        self.font_path = font_path
        self.fontprop = font_manager.FontProperties(fname=font_path, size=20)
        self.load_files()
    
    def load_files(self):
        self.file_path = glob.glob('temp/*.csv')
        total = pd.DataFrame()
        for i in self.file_path:
            data = pd.read_csv(i, encoding='euc_kr')
            total = pd.concat([total, data], ignore_index=True)
        self.df = total
        

    def check_na(self):
        check_1 = self.df['기온(°C)'].isna().any()
        if check_1:
            print("기온(°C) 열에 결측치가 있습니다.")
        else:
            print("기온(°C) 열에 결측치가 없습니다.")

    def check2(self):
        check_2 = self.df[(self.df['기온(°C)'] < -33) | (self.df['기온(°C)'] > 40)]
        if not check_2.empty:
            self.df.loc[check_2.index, '기온(°C)'] = np.nan
            print("기온(°C) 열에 이상있는 데이터를 nan값으로 처리했습니다.")
        else:
            print("물리한계검사 통과")

    def check3(self):
        self.df['온도차'] = self.df['기온(°C)'].diff()  # 현재 온도에서 -1분전 온도 빼기
        self.df['온도차_체크'] = np.abs(self.df['온도차']) > 3
        if self.df['온도차_체크'].any():
            print("이상있는 데이터가 있습니다.")
        else:
            print("단계검사 통과")

    def check4(self):
        self.df['온도차'] = self.df['온도차'].abs()  # 절대값 처리
        self.df['온도차_누적합'] = self.df['온도차'].rolling(window=60).sum()  # 60분 간격으로 데이터 합
        self.df['온도차_체크2'] = self.df['온도차_누적합'] < 0.1
        if self.df['온도차_체크2'].any():
            print("지속성검사 통과")
        else:
            print("온도차_누적합이 0.1보다 작은 경우가 있습니다.")
        
    def plot_(self):
        self.df['일시'] = pd.to_datetime(self.df['일시'])

        # 그래프 생성
        fig, ax = plt.subplots(figsize=(12, 6))

        # x축에 일시 데이터, y축에 기온 데이터 설정
        ax.plot(self.df['일시'], self.df['기온(°C)'], label='기온(°C)')

        # x축 눈금 간격 설정 (일(Day) 단위로)
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

        # x축에 일시 포맷 설정 (월/일)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

        plt.xticks(rotation=45)

        plt.title('일별 기온 그래프', fontproperties=self.fontprop)
        plt.xlabel('일시', fontproperties=self.fontprop)
        plt.ylabel('기온(°C)', fontproperties=self.fontprop)

        # 그래프 출력
        return fig
    
    def plot_temperature_graph(self, resample_period='D',time2 = None):
        df = self.df.copy()
        self.df['일시'] = pd.to_datetime(df['일시'])
        day_mean = df.resample(resample_period, on='일시')['기온(°C)'].mean()

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(day_mean.index, day_mean.values, label=f'{resample_period} 평균 기온')
        plt.xticks(rotation=45)
        plt.title(f'{time2} 평균 기온 그래프', fontproperties=self.fontprop)
        plt.xlabel('일시', fontproperties=self.fontprop)
        plt.ylabel('기온(°C)', fontproperties=self.fontprop)
        return fig
        
if __name__ == "__main__":
    tm = Temp()  
    tm.check_na()
    tm.check2()
    tm.check3()
    tm.check4()
    tm.plot_temperature_graph('D')
    tm.plot_temperature_graph('1H')
    tm.plot_temperature_graph('3H')
    tm.plot_temperature_graph('8H')
        
        
        