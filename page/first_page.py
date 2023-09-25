import streamlit as st
from PIL import Image
from utils.temp_ import Temp

class assignment:
    def __init__(self):
        self.subheader = '공통 과제(기상 데이터 분석과 알고리즘)'
        self.image1_path = 'page\\img\\wp_streamlit(class).drawio.png'
        self.image1 = Image.open(self.image1_path)

    def app1(self):
        tab1, tab2, tab3 = st.tabs(['데이터 QC 검사', '시계열 분석', 'Streamlit Diagram'])

        with tab1:
            tm = Temp()
            st.info('''1. 결측치 검사
                    
                def check_na(df):
                check_1 = df['기온(°C)'].isna().any()
                if check_1:
                    print("기온(°C) 열에 결측치가 있습니다.")
                else:
                    print("기온(°C) 열에 결측치가 없습니다.")
                return df''')
            
            
            st.info('''2. 물리 한계 검사
                    
                def check2(df):
                    
                check_2 = df[(df['기온(°C)'] < -33) | (df['기온(°C)'] > 40)]
    
                if not check_2.empty:
                    df.loc[check_2.index, '기온(°C)'] = np.nan
                    print("기온(°C) 열에 이상있는 데이터를 nan값으로 처리했습니다.")
                else:
                    print("물리한계검사 통과")
                return df''')
            
            
            st.info('''3. 단계 검사
                    
                def check3(df):
                df['온도차'] = df['기온(°C)'].diff()#현재 온도에서 -1분전 온도 빼기
    
                df['온도차_체크'] = np.abs(df['온도차']) > 3
                if df['온도차_체크'].any():#단계검사
                    print("이상있는 데이터가 있습니다.")
                else:
                    print("단계검사 통과")
                return df''')    
           
            
            st.info('''4. 지속성 검사
                
                def check4(df):
                df['온도차'] = df['온도차'].abs()#절대값 처리
    
                df['온도차_누적합'] = df['온도차'].rolling(window=60).sum()
                #60분 간격으로 데이터 합
    
                df['온도차_체크2'] = df['온도차_누적합'] < 0.1
                
                if df['온도차_체크2'].any():
                    print("지속성검사 통과")
                else:
                    print("온도차_누적합이 0.1보다 작은 경우가 있습니다.")
                return df''')
            
            st.subheader('※수집한 데이터에 이상이 없음을 확인할 수 있다.')
        
        with tab2:
            st.write(f'**#. 일별 기온그래프**')
            fig1 = tm.plot_()
            st.pyplot(fig1)
            
            st.write(f'**#. 1시간 평균 그래프**')
            fig2 = tm.plot_temperature_graph('1h','1시간')
            st.pyplot(fig2)
            
            st.write(f'**#. 3시간 평균 그래프**')
            fig3 = tm.plot_temperature_graph('3h','3시간')
            st.pyplot(fig3)
            
            st.write(f'**#. 8시간 평균 그래프**')
            fig4 = tm.plot_temperature_graph('8h','8시간')
            st.pyplot(fig4)
            
            st.write(f'**#. 1일 평균 그래프**')
            fig5 = tm.plot_temperature_graph('D','1일')
            st.pyplot(fig5)

        with tab3:
            st.write(f"**1. Class를 사용한 Streamlit Multipage Diagram**")
            st.image(self.image1)
            

if __name__ == "__main__":
    main = assignment()
    main.app1()