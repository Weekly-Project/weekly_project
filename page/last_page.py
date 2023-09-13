import streamlit as st

#수정해서 최종 업로드 해주시면 됩니다 : )

class final:
    def __init__(self):
        self.subheader = '느낀점 및 참고자료' 

    def app4(self):
        st.subheader(self.subheader)

        tab1, tab2 = st.tabs(['마무리 및 소감', '참고자료'])
        with tab1:
            st.markdown('#### 마무리하며')
            st.info('''
                    김영훈: test1 \n
                    권지현: test2 \n
                    김태은: test3 \n
                    ''')


if __name__ == "__main__":
    main = final()
    main.app4()
        