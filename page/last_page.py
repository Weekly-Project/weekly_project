import streamlit as st

class final:
    def __init__(self):
        self.subheader = '느낀점 및 참고자료' 

    def app4(self):
        st.subheader(self.subheader)

        tab1, tab2 = st.tabs(['마무리 및 소감', '참고자료'])
        with tab1:
            st.markdown('#### 마무리하며')
            st.info(f'''
                    **김영훈**: 프로젝트 초반부터 참신하고 재밌어 보이는 아이디어의 주제를 선정하면서 진행 방향을 잡고 시작하여 수월하게 진행하였습니다. 
                    조원 모두 각자의 분업 또한 착실하게 진행한 덕분에 시간적 여유가 있었고 그로 인해 계획했던 부분 이상의 분석도 진행할 수 있었습니다.
                    익숙치 않은 클래스화 과정에서 많은 오류가 발생해 어려움이 있었지만 충분히 해결 가능한 문제였습니다. 이번 프로젝트 과정에서 실수한 부분으로
                    문제 정의를 제대로 하지 못했다고 생각합니다. 멀티페이지 구성하는 방법에 대해 저희에게 요구된 문제를 제대로 정의하지 못한 부분이 아쉽게 느껴지지만 
                    그로 인해 모든 모듈 파일을 클래스화 하는 작업을 하면서 좀 더 익숙해지게 된 것 같습니다.
                    ''')
            st.info(f'''
                    **권지현**: 이번 주간프로젝트를 진행하면서 좋은 주제를 선택하여 재미있게 프로젝트를 진행할 수 있었습니다. 지난번 세미프로젝트 때 보다는 주제선정이나 프로젝트를 진행함에 있어서 조금 더 수월해진 모습을 느낄수 있었습니다. 다만, 작성한 코드를 class화 한다는 점에서 시행착오가 있었지만 좋은 조원들을 만나 해결할 수 있었습니다. \n
                    이번 프로젝트를 통해 마케팅의 중요성과 창의성이 얼마나 큰 역할을 하는지를 몸소 깨달았습니다. 동물원과 같은 엔터테인먼트 시설에서도 차별화된 전략을 통해 지속적인 성공을 이끌어낼 수 있다는 것을 배웠습니다. 이번 프로젝트를 통해 앞으로의 학습에 큰 도움이 될 것이라고 생각합니다.
                    ''')
            st.info(f'''
                    **김태은**: 색다른 주제로 주간 프로젝트를 진행하며 많은 것을 배울 수 있었습니다. \n
                    streamlit을 클래스화 하여 구현하는 것이 어려웠지만 팀원들의 도움을 받아가며 부족한 부분을 채워나갈 수 있었습니다. \n
                    독특하고 참신한 마케팅 방법이 많지만 에버랜드가 택했던 방식처럼 진심을 보여주는 것이 가장 기본적이지만 효과적인 마케팅 수단이 될 수 있다는 사실을 다시 한번 알게 되었습니다. \n
                    앞으로 에버랜드의 다른 동물들도 푸바오처럼 방문객들의 많은 사랑과 관심을 받을 수 있었으면 좋겠습니다.
                    ''')
        with tab2:
            st.write(f'**# 논문**')
            st.write('이향숙(가천대학교 조경학과). (2012). 동물원 방문객의 인식 및 만족도 영향요인 연구. 한국조경학회지.')
            st.write('')
            st.write('')
            st.write(f'**# 자료 출처**')
            st.write('기상자료개방포털(공통과제 - 시계열분석)')
            st.write('관광지식정보시스템(에버랜드 연도별 방문객 수)')
            st.write('구글 트랜드(푸바오 유튜브 검색량)')
            st.write('유튜브 API(유튜브 채널 동영상 비율, 푸바오vs한국호랑이 비교)')
            st.write('한국관광 데이터랩(에버랜드 SNS 언급량 변화)')
            st.write('전자공시시스템(에버랜드 매출량 변화)')

if __name__ == "__main__":
    main = final()
    main.app4()
        