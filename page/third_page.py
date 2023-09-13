import streamlit as st




class conclusion:
    def __init__(self):
        self.subheader = '앞으로 에버렌드의 마케팅 방향성'

    def app3(self):
        st.subheader(self.subheader)
        st.write('test')


if __name__ == "__main__":
    main = conclusion()
    main.app3()