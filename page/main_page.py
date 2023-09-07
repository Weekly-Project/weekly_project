import streamlit as st
from PIL import Image

image1 = Image.open('page\\datanalysis.png')
image2 = Image.open('page\\fubao.jpg')


class Main:
    def __init__(self):
        self.title = '데이터 분석 & 시각화 주간 프로젝트'

    def app():
        st.title(self.title)
        tab1, tab2, tab3 = st.tabs(['Home', '팀원 소개 및 역할분담', '발표 주제'])
        with tab1:
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image(image1)
            with col2:
                st.subheader('안녕하세요, 주간 프로젝트 stremalit 구현 페이지입니다.')
                st.markdown('##### 조 : 3조 ')
                st.write('다음 탭으로 넘겨 자세한 정보를 확인해 주세요')

        with tab2:
            st.subheader('팀원 소개')
            st.info('''
                    김영훈 (조장): 공통과제(시계열 데이터 처리), 자료조사 \n
                    권지현 : 다이어그램(공동과제, 조별 과제), 자료조사, PPT 제작 \n
                    김태은 : streamlit 페이지 구현, 자료조사, 발표
                    ''')
            
        with tab3:
            st.subheader('발표 주제')
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image(image2)
            with col2:
                st.markdown('##### 푸바오를 통한 에버랜드의 매출 증가 및 향후 에버랜드의 마케팅 방항성')
                st.success('''
                            현재 에버랜드에서 가장 인기가 많은 동물인 자이언트 판다 푸바오를 통한 에버랜드의 마케팅 방식의 효과를 알아보고
                           이후 푸바오가 중국으로 반환된 이후 어떤 마케팅 방식을 유지 또는 신설하는 것이 적절할 지에 대해 알아보기 위해 
                           해당 주제를 선정하게 되었습니다
                            ''')