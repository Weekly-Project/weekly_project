import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import scipy.stats as stats
import seaborn as sns

class Corr:
    def __init__(self, data_file):
        self.df = pd.read_csv(data_file)

    def corr(self, data_name):
        cc, p_value = stats.pearsonr(self.df['visitor'], self.df[data_name])
        result = ""
        if p_value <= 0.05:
            result = '귀무가설을 기각합니다. 두 변수 간에 통계적으로 유의미한 상관관계가 있다고 판단합니다.'
        else:
            result = '귀무 가설을 채택합니다. 두 변수 간에 통계적으로 유의미한 상관관계가 없다고 판단합니다.'
        return cc, p_value, result


    def corr_plot(self, data_name):
        font_path = './NanumGothic.ttf'
        fontprop = font_manager.FontProperties(fname=font_path, size=12)
        

        fig, ax = plt.subplots()
        sns.regplot(x=data_name, y=self.df['visitor'], data=self.df, ci=None, ax=ax)
        ax.set_title(f'방문객수와 {data_name} 산점도', fontproperties=fontprop)
        ax.set_xlabel(data_name, fontproperties=fontprop)
        ax.set_ylabel('방문객수', fontproperties=fontprop)
        ax.grid(True)
        
        last_14_data = self.df.tail(14)
        sns.scatterplot(x=data_name, y='visitor', data=last_14_data, ax=ax, color='red', label='거리두기 종료 후 데이터')
       
        return ax.figure



if __name__ == '__main__':
    cr = Corr('co_data.csv')
    cr.corr('google')
    cr.corr_plot('google')
    cr.corr('youtube')
    cr.corr_plot('youtube')