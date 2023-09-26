import pandas as pd
import matplotlib.pyplot as plt

class SalesComparison:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        self.quarters_1 = self.df[self.df['분기'].isin(['22년도 1분기', '23년도 1분기'])]
        self.quarters_2 = self.df[self.df['분기'].isin(['22년도 2분기', '23년도 2분기'])]

    def plot_sales_comparison(self):
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False

        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.bar(self.quarters_1['분기'], self.quarters_1['매출액(단위: 백만원)'], color=['skyblue', 'lightcoral'])
        plt.xlabel('분기')
        plt.ylabel('매출액(단위: 백만원)')
        plt.title('1분기 매출액 비교')

        plt.subplot(1, 2, 2)
        plt.bar(self.quarters_2['분기'], self.quarters_2['매출액(단위: 백만원)'], color=['skyblue', 'lightcoral'])
        plt.xlabel('분기')
        plt.ylabel('매출액(단위: 백만원)')
        plt.title('2분기 매출액 비교')

        plt.tight_layout()
        plt.show()
'''
# 클래스 인스턴스 생성
sales_comparison = SalesComparison('삼성물산 매출액.xlsx')

# 바차트 그리기
sales_comparison.plot_sales_comparison()
'''