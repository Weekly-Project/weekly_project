import streamlit as st
from page.main_page import Main
from page.first_page import assignment
from page.second_page import project
from page.third_page import conclusion
from page.last_page import final

def home():
    st.title('3조 주간 프로젝트')
    
    item_list = ['item0', 'item1', 'item2', 'item3', 'item4']
    item_labels = {
            'item0': 'Home',
            'item1': '공통과제',
            'item2': '3조 프로젝트',
            'item3': '결론',
            'item4': '마무리',
        }

    FIL = lambda x : item_labels[x]
    item = st.sidebar.selectbox('목록을 선택하세요.', item_list, format_func=FIL)

    if item == 'item0':
        main_page = Main()
        main_page.app()

    elif item == 'item1':
        first_page = assignment()
        first_page.app1()

    elif item == 'item2':
        second_page = project()
        second_page.app2()

    elif item == 'item3':
        third_page = conclusion()
        third_page.app3()

    elif item == 'item4':
        last_page = final()
        last_page.app4()
    

if __name__ == "__main__":
    home()
