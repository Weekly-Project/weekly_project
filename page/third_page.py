import streamlit as st
from utils.corr2 import Corr

class conclusion:
    def __init__(self):
        self.subheader = '분석 결과 및 앞으로 에버랜드의 마케팅 방향성'

    def app3(self):
        st.subheader(self.subheader)
        tab1, tab2, tab3 = st.tabs(['상관분석', '분석결과', '결론'])
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
            st. info('''푸바오와 사육사의 유대관계를 많은 사람들이 TV 프로그램, SNS, 유튜브 등 다양한
매체에서 접하면서 인기몰이를 하고 있으며, 이러한 관심에 비례해 방문객 또한 증가하는 추세이다.

- 출시 하루 만에 1위를 기록한 이모티콘
- 굿즈 판매량의 4배 증가
- 7일 만에 3만 건이 넘는 이름 공모전 응모
- 에세이 부분 1위를 기록한 포토 에세이

위와 같은 상황을 보면 한동안 푸바오에 대한 인기는 계속될 것으로 예상된다.''')

            st.write('''에버랜드만의 차별화된 마케팅 수단인 동물을 활용한 방법이 계속해서 진행될 것으로 예상되며 이는 긍정적인 효과를 불러올 것이라고 예상한다.
이러한 마케팅 방법은 유일하게 판다 사육이 가능한 시설을 갖추고 있으며
세계 최고 수준의 동물복지 운영 시스템을 구축하고 멸종 위기종 복원 사업에 참여하고 있는 에버랜드만의
무기라고 생각된다.''')
            st.subheader(' ')
            st.subheader('마케팅 방향성')
            st.write('''마케팅에 있어서 스토리텔링이 중요하다
처음 에버랜드 동물원 유튜브를 보면 더빙으로 나온다. 이때만 해도 유튜브 조회수나 구독자수는 미미했다. 
하지만 사육사들이 직접 동물과 교감하는 영상이 나온 후 + 미국판다 학대 논란으로 인해
푸바오가 한국에서 사랑받고 있는 영상을 접한 중국인들이 에버랜드 유튜브에 댓글을 달기 시작하면서 인기가 급상승하였다. 
푸바오의 반환 날짜가 다가오는 만큼 가족애를 살린 쌍둥이 판다들의 서사를 쌓아가는 것이 중요할 것이라고 생각한다.''')

            st.info(''' - **동물복지 및 도덕적 측면에 대한 이미지 메이킹 마케팅 :** 
                    쌍둥이 판다의 생태학적 가치와 중요성을 강조하는 교육적 콘텐츠를 제작. 
                    환경 보호 및 생태계에 대한 인식을 높이는 콘텐츠를 통해, 에버랜드는 사회적 책임을 다하는 기업으로 인식될 수 있다. 
                    동물 마케팅으로 인한 에버랜드에 대한 긍정적인 평가도 증가할 것이다.

                (ex. 판다 월드의 수익 일부를 멸종 위기 동물보호에 기부, 
                 세계 최고 수준의 동물 복지 시스템을 강조한 홍보 등)''' )
            st.subheader(' ')
            st.info(''' - **다양한 직접 체험 프로그램 및 한정된 상품과 생성 :**
                     푸바오의 관심도가 증가하면서 판다월드의 입장객이 2배이상 증가했다고 한다. 
                     이에따라 관광객들이 소리지르는 등 판다의 스트레스가 증가하면서 판다월드의 관람시간을 5분으로 제한 하고 있다.
                     이로인한 소비자들의 아쉬움을 대체할 체험 프로그램이나 유명 연예인 이나 인플루언서에게만 제공되던 홍보목적의 체험 기회를
                     일반 방문객에게도 제공하는 방식의 프로그램이 생성된다면 보다 관심도가 증가할 것이다.또한 방문객에 한정된 굿즈나 상품들을
                     기획하여  푸바오 반환전 다양한 이벤트로 소비자들에게 좋은 추억으로 남게 할 수 있을 것이다.

                (ex. VR체험, 푸바오 일일 매니저 체험, 판다와 사진촬영, 
            판다 가족 발바닥 도장 스티커, 판다 얼굴모양 볶음밥 등의 방문객 한정 상품 출시''')

            st.subheader(' ')
            st.info(''' - **국내 소비자 및 해외시장을 겨냥한 다양한 마케팅 :** 
                    세계 최고 수준의 복지 시스템을 갖추고 있으며 숙련된 사육사와 보호 환경을 갖춘 사육장을 보유하고 있는
                    에버랜드는 판다가 끝이 아닌 다양한 동물을 통해 푸바오와 같은 효과를 계속해서 창출하기 위해 노력할 것이다.
                    위에서 이야기한 에버랜드만의 장점을 통해 국내뿐만 아니라 해외에 있는 소비자들에게 어필할 수 있는
                    새로운 마케팅 방안이 필요하다.
                    
                (ex. 판다 - 중국처럼 다양한 국가에 홍보가 가능한 여러 동물들을 통한 영상 제작''' )
             
        
       

if __name__ == "__main__":
    main = conclusion()
    main.app3()

