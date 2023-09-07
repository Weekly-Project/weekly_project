import streamlit as st
from page.main_page import Main
from page.sidebar import sidebar




def home():
    st.title('3조 주간 프로젝트')
    sidebar = Sidebar()
    main_page = Main()

    sidebar.render_sidebar()
    main_page.render_main_page()




if __name__ == "__home__":
    home()


