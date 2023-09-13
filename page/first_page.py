import streamlit as st



class assignment:
    def __init__(self):
        self.subheader = '공통 과제(기상 데이터 분석과 알고리즘)'

    def app1(self):
        st.subheader(self.subheader)
        tab1, tab2 = st.tabs(['기상 데이터 분석', '알고리즘'])
        with tab1:
            st.write('test')
        with tab2:
            st.write('test2')

if __name__ == "__main__":
    main = assignment()
    main.app()