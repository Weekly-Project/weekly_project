import streamlit as st


class project:
    def __init__(self):
        self.subheader = '조별 프로젝트'

    def app2(self):
        st.subheader(self.subheader)
        tab1, tab2, tab3, tab4 = st.tabs(['방문객 변화', '푸바오', '한국 호랑이', '매출량 변화'])
        with tab1:
            st.write('방문객 변화')
        with tab2:
            st.write('푸바오의 화제성')
        with tab3:
            st.write('한국 호랑이 관심도 증가에 따른 방문객 변화')
        with tab4:
            st.write('동물 마케팅 성공에 따른 에버랜드 매출량 변화')


if __name__ == "__main__":
    main = project()
    main.app2()