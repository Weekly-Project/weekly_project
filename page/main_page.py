import streamlit as st
from PIL import Image

# sidebar.py 파일은 삭제해주세요!

class Main:
    def __init__(self):
        self.subheader = '데이터 분석 & 시각화 주간 프로젝트'
        self.image1_path = 'page\\img\\datanalysis.png'
        self.image2_path = 'page\\img\\fubao.jpg'
        self.image3_path = 'page\\img\\fubao_profile.jpg'
        self.image4_path = 'page\\img\\tiger.png'
        self.image1 = Image.open(self.image1_path)
        self.image2 = Image.open(self.image2_path)
        self.image3 = Image.open(self.image3_path)
        self.image4 = Image.open(self.image4_path)

    def app(self):
        st.subheader(self.subheader)
        tab1, tab2, tab3 = st.tabs(['Home', '팀원 소개 및 역할분담', '발표 주제'])
        with tab1:
            st.markdown("")
            col1, col2 = st.columns([2, 3])
            with col1:
                st.image(self.image1)
            with col2:
                st.markdown("")
                st.markdown('### 안녕하세요, 주간 프로젝트 stremalit 구현 페이지입니다.')
                st.markdown('##### 조 : 3조 ')
                st.write('다음 탭으로 넘겨 자세한 정보를 확인해 주세요')

        with tab2:
            st.subheader('팀원 소개')
            st.markdown('##### 저희 조를 소개합니다')
            st.info('''
                    **김영훈 (조장)**  : 공통과제(시계열 데이터 처리), 자료조사 \n
                    **권지현**  : 다이어그램(공동과제, 조별 과제), 자료조사, PPT 제작 \n
                    **김태은**  : streamlit 페이지 구현, 자료조사, 발표
                    ''')
            
        with tab3:
            st.subheader('발표 주제')
            col1, col2 = st.columns([2, 3])
            with col1:
                st.image(self.image2)
            with col2:
                st.markdown('##### 푸바오를 통한 에버랜드의 매출 증가 및 향후 에버랜드의 마케팅 방항성')
                st.success('''
                            현재 에버랜드에서 가장 인기가 많은 동물인 자이언트 판다 푸바오를 통한 에버랜드의 마케팅 방식의 효과를 알아보고
                           이후 푸바오가 중국으로 반환된 이후 어떤 마케팅 방식을 유지 또는 신설하는 것이 적절할 지에 대해 알아보기 위해 
                           해당 주제를 선정하게 되었습니다
                            ''')
            st.markdown("")
            st.write('혹시 푸바오에 대해 잘 모르시나요? 밑에서 확인해 주세요')
            st.markdown("")
            st.markdown('##### 푸바오 프로필')
            col3, col4 = st.columns([2, 3])
            with col3:
                st.image(self.image3)
            with col4:
                st.info('''
                        **이름**  : 푸바오(Fubao, 福宝) \n
                        **종족**  : 자이언트 판다 \n
                        **출생**  : 2020년 7월 20일 / 에버랜드 판다월드(용인시 처인구) \n
                        **가족**  : 아빠(러바오), 엄마(아이바오), 쌍둥이 동생판다 \n
                        **특징**  : 국내 최초 자연번식으로 태어난 판다 \n
                        **별명**  : 푸뚠뚠, 뚠빵이, 푸린세스, 푸룽지, 푸공주, 용인시 털주먹, 푸질머리 등
                        ''')

            st.markdown("")
            st.write('한국 호랑이 태범이, 무궁이도 있어요!')
            st.markdown("")
            st.markdown('##### 태범이, 무궁이 프로필')
            col5, col6 = st.columns([2, 3])
            with col5:
                st.image(self.image4)
            with col6:
                st.info('''
                        **이름**  : 태범(太汎), 무궁(無窮) \n
                        **종족**  : 시베리아 호랑이 \n
                        **출생**  : 2020년 2월 20일 / 에버랜드 타이거밸리(용인시 처인구) \n
                        **가족**  : 아빠(태호), 엄마(건곤), 동생(아름, 다운, 우리, 나라) \n
                        **특징**  : 에버랜드에서 최초로 자연포육으로 길러진 호랑이, 21년 10월 25일부터 국립백두대간수목원 호랑이숲에서 지내고 있다. \n
                ''')


if __name__ == "__main__":
    main = Main()
    main.load_images()
    main.app()
