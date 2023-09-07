import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as font_manager


# 그래프에서 한글 폰트 적용

font_path = 'E:/python_lecture/functionssssss/func/NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size = 20)



file_path = glob.glob('E:/python_lecture/functionssssss/func/temp/*.csv')


print(file_path)



def files(file_path):
    total = pd.DataFrame()
    for i in file_path:
        data = pd.read_csv(i, encoding = 'euc_kr')
        total = pd.concat([total,data],ignore_index = True)
    return total

df = files(file_path)
df
print(df.head())
print(df.info())

def check_na(df):
    check_1 = df['기온(°C)'].isna().any()
    if check_1:
        print("기온(°C) 열에 결측치가 있습니다.")
    else:
        print("기온(°C) 열에 결측치가 없습니다.")
    return df

check_na(df)

def check2(df):
    check_2 = df[(df['기온(°C)'] < -33) | (df['기온(°C)'] > 40)]

    if not check_2.empty:
        df.loc[check_2.index, '기온(°C)'] = np.nan
        print("기온(°C) 열에 이상있는 데이터를 nan값으로 처리했습니다.")
    else:
        print("물리한계검사 통과")
    return df

check2(df)

def check3(df):
    df['온도차'] = df['기온(°C)'].diff()#현재 온도에서 -1분전 온도 빼기

    df['온도차_체크'] = np.abs(df['온도차']) > 3
    if df['온도차_체크'].any():#단계검사
        print("이상있는 데이터가 있습니다.")
    else:
        print("단계검사 통과")
    return df
    
check3(df)
    
def check4(df):
    df['온도차'] = df['온도차'].abs()#절대값 처리

    df['온도차_누적합'] = df['온도차'].rolling(window=60).sum()#60분 간격으로 데이터 합

    df['온도차_체크2'] = df['온도차_누적합'] < 0.1
    if df['온도차_체크2'].any():
        print("지속성검사 통과")
    else:
        print("온도차_누적합이 0.1보다 작은 경우가 있습니다.")
    return df

check4(df)

df.head()


# 일시 열을 날짜/시간 형식으로 변환
df['일시'] = pd.to_datetime(df['일시'])

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

# x축에 일시 데이터, y축에 기온 데이터 설정
ax.plot(df['일시'], df['기온(°C)'], label='기온(°C)')

# x축 눈금 간격 설정 (일(Day) 단위로)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

# x축에 일시 포맷 설정 (월/일)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

plt.xticks(rotation=45)

plt.title('일별 기온 그래프', fontproperties=fontprop)
plt.xlabel('일시', fontproperties=fontprop)
plt.ylabel('기온(°C)', fontproperties=fontprop)

# 그래프 출력
plt.show()

#리샘플링해서 일별 평균 기온을 계산

day_mean = df.resample('D', on='일시')['기온(°C)'].mean()


eight_mean = df.resample('8H', on='일시')['기온(°C)'].mean()

three_mean = df.resample('3H', on='일시')['기온(°C)'].mean()

one_mean = df.resample('1H', on='일시')['기온(°C)'].mean()


def plot_(time, time2):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(time.index, time.values, label=f'{time2} 평균 기온')  
    plt.xticks(rotation=45)
    plt.title(f'{time2} 평균 기온 그래프', fontproperties=fontprop)  
    plt.xlabel('일시', fontproperties=fontprop)
    plt.ylabel('기온(°C)', fontproperties=fontprop)
    plt.show()
    

plot_(one_mean,'1시간')
plot_(three_mean,'3시간')
plot_(eight_mean,'8시간')
plot_(day_mean,'1일')

    
    
    
    
    





