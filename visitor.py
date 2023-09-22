import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

df = pd.read_excel('./visitor_data/visitor_data.xls')

df.drop(['2019년','2020년','2021년','2022년','2023년'], axis = 1, inplace = True)
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

df1 = df.loc[2, '2019년 06월':'2020년 05월']

df2 = df.loc[2, '2020년 06월': '2021년 05월']

df3 = df.loc[2, '2021년 06월' : '2022년 05월']

df4 = df.loc[2, '2022년 06월' : '2023년 05월']

font_path = './NanumGothic.ttf'


fontprop = font_manager.FontProperties(fname=font_path, size=12)


x_values = ['6월', '7월', '8월', '9월', '10월', '11월', '12월', '1월', '2월', '3월', '4월', '5월']


plt.plot(x_values, df1, label='19~20')
plt.plot(x_values, df2, label='20~21')
plt.plot(x_values, df3, label='21~22')
plt.plot(x_values, df4, label='22~23')


plt.xlabel('기간', fontproperties=fontprop) 
plt.ylabel('방문객 수', fontproperties=fontprop)  
plt.title('연도별 방문객 수 그래프', fontproperties=fontprop)  
plt.legend()
plt.xticks(fontproperties=fontprop)

plt.show()

