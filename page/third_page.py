import streamlit as st
from utils.corr2 import Corr

class conclusion:
    def __init__(self):
        self.subheader = '분석 결과 및 앞으로 에버렌드의 마케팅 방향성'

    def app3(self):
        st.subheader(self.subheader)
        tab1, tab2, tab3 = st.tabs(['상관분석', '분석결과', '마케팅 방향성'])
        with tab1:
            st.subheader('방문객 데이터 - 구글 및 유튜브 검색량의 상관도 분석')
            st.info('''검색량이 얼마인지 알 수 있는 정확한 수치를 보여주는 데이터를 수집했다면 더 좋았겠지만,
                    해당 부분에는 어려움이 있어 비율 척도를 나타내는 데이터를 수집하여 분석 가능한 
                    피어슨 상관분석을 진행하였다.''')
            # 파일을 불러와서 객체 초기화
            data_file = 'co_data.csv'
            font_path = 'NanumGothic.ttf'
            corr_obj = Corr(data_file)


            google_corr, google_pvalue, google_result = corr_obj.corr('google')
            st.write(f'구글 검색량과 방문객수의 상관 계수: {google_corr}')
            st.write(f'구글 검색량과 방문객수의 p-value: {google_pvalue}')
            st.markdown(f'**<font color="red">구글 검색량과 방문객 수의 검정 결과: {google_result}</font>**', unsafe_allow_html=True)
            st.text("")
            st.text("")
            st.text("")
            
            youtube_corr, youtube_pvalue, youtube_result = corr_obj.corr('youtube')
            st.write(f'유튜브 검색량과 방문객수의 상관 계수: {youtube_corr}')
            st.write(f'유튜브 검색량과 방문객수의 p-value: {youtube_pvalue}')
            st.markdown(f'**<font color="red">유튜브 검색량과 방문객수의 검정 결과: {youtube_result}</font>**', unsafe_allow_html=True)        
            
            st.write('''**예상과 달리 두 변수 모두 방문객 수에 유의미한 영향을 미치지 않는다는 결과가 도출되었다.
                     하지만 아래에 나와있는 일반적인 해석범위를 보면 영향이 없다고 말할 수는 없다.**''')
            correlation_ranges = [
        "-1.0에서 -0.7: 강한 음의 상관 관계 (Negative Strong Correlation)",
        "-0.7에서 -0.3: 뚜렷한 음의 상관 관계 (Negative Moderate Correlation)",
        "-0.3에서 -0.1: 약한 음의 상관 관계 (Negative Weak Correlation)",
        "-0.1에서 0.1: 거의 상관 관계 없음 (No or Negligible Correlation)",
        "**0.1에서 0.3: 약한 양의 상관 관계 (Weak Positive Correlation)**",
        "0.3에서 0.7: 뚜렷한 양의 상관 관계 (Moderate Positive Correlation)",
        "0.7에서 1.0: 강한 양의 상관 관계 (Strong Positive Correlation)"
    ]

            st.write("상관 계수 범위 :")
            for range_description in correlation_ranges:
                st.write(range_description)
            
        with tab2:
            st.subheader('산점도를 통한 추가 분석')
            st.info('''산점도를 보면 검색량이 많은 경우에는 선형 관계로 보이지만,
                    검색량이 적은 다수의 경우에는 멀리 떨어져 있는 걸 볼 수 있었다. 해당 내용을 토대로
                    분석했을 때 검색량이 적은 시기(푸바오가 등장 초반부)는 코로나로 인한 사회적 거리 두기가 이루어지던 시기여서
                    이러한 결과를 보여준다고 생각한다. ''')
            cr = Corr(data_file)
            fig1 = cr.corr_plot('google')
            st.pyplot(fig1)

            fig2 = cr.corr_plot('youtube')
            st.pyplot(fig2)
            
            st.info('''추가적으로 붉은색으로 표시된 데이터 중에서 많이 벗어난 데이터들이 있는데 해당 데이터들은 봄, 가을에
                    사람이 몰리는 특성과 할로윈, 어린이날 등의 요인으로 인한 결과인 것을 알 수 있었다.''')
            st.markdown('''**<font color="red">검정결과를 보았을 때 단편적으로 영향이 없다고 생각할 수 있지만, 위에서 말한 내용을 토대로
생각했을 때 방문객 수에 대해 상상이상의 큰 영향을 끼치는 것은 아니지만 어느정도의 영향력을
보이고 있음을 알 수있다. 
</font>**''',unsafe_allow_html=True)
        with tab3:
            st.subheader('결론')
            
        
       

if __name__ == "__main__":
    main = conclusion()
    main.app3()

