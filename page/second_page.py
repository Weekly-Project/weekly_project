import streamlit as st
from PIL import Image
from utils import zoo_donut_chart as zoo
from utils import trend_fubao as tf
from utils import youtube_vs_graph as yvg
from utils.visitor_gr import VisitorData
from utils.ss_sales import SalesComparison
from utils.yongin_sns import SNS

class project:
    def __init__(self):
        self.subheader = '조별 프로젝트'
        self.image1_path = 'page\\img\\fubao_news.png'
        self.image2_path = 'page\\img\\ba1.png'
        self.image3_path = 'page\\img\\ba2.png'
        self.image4_path = 'page\\img\\ba3.png'
        self.image5_path = 'page\\img\\ba4.png'
        self.image6_path = 'page\\img\\sales_fubao.png'
        self.image7_path = 'page\\img\\매출기준.png'
        self.image8_path = 'page\\img\\wp_prj_diagram.drawio.png'
        self.image9_path = 'page\\img\\everland.png'
        self.image10_path = 'page\\img\\zoo_count.png'
        self.image11_path = 'page\\img\\pvst.png'
        self.image1 = Image.open(self.image1_path)
        self.image2 = Image.open(self.image2_path)
        self.image3 = Image.open(self.image3_path)
        self.image4 = Image.open(self.image4_path)
        self.image5 = Image.open(self.image5_path)
        self.image6 = Image.open(self.image6_path)
        self.image7 = Image.open(self.image7_path)
        self.image8 = Image.open(self.image8_path)
        self.image9 = Image.open(self.image9_path)
        self.image10 = Image.open(self.image10_path)
        self.image11 = Image.open(self.image11_path)

    def app2(self):
        st.subheader(self.subheader)
        tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
            'Project Diagram','방문객 변화', '푸바오', '한국 호랑이', 'SNS 언급량 변화','매출량 변화'])
        with tab0:
            st.image(self.image8)
        with tab1:
            col1,col2 = st.columns([3,3])
            with col1:
                st.image(self.image2)
                st.image(self.image3)
            with col2:
                st.image(self.image4)
                st.image(self.image5)
            st.info('''위에 보이는 4개의 기사를 보았을 때 코로나로 인한 거리두기 기간동안 방문객 감소로 인한 매출액이 대폭 감소했던
                     에버랜드는 작년기준 가장 많은 사람이 방문한 관광지로 뽑히며 회복한 모습을 보여주고 있다.
                     이러한 결과가 푸바오의 인기를 통한 영향이 있었는지 알아보기위해 코로나 이전, 코로나 시기, 그 이후로 단계를 나눠
                     4년간의 방문객 데이터를 시각화 하여 도출하였다.''')

            vs = VisitorData()
            fig1 = vs.plot_visitor_data()
            st.pyplot(fig1)

        with tab2:
            st.write(f"**1. 에버랜드 판다 푸바오의 인기?**")
            st.image(self.image1)
            st.info('''
            푸바오의 인기는 그야말로 폭발적입니다. 국내 최초 자연번식으로 태어난 판다로서, 그의 독특한 매력은 많은 이들의 마음을 사로잡았습니다.\n
            푸바오가 최근 TV 프로그램에서 돌보는 사육사와의 따뜻한 이야기가 알려지면서, 그의 매력은 한층 더 돋보이게 되었습니다.\n
            인기에 힘입어 에버랜드 판다 푸바오의 다양한 굿즈들이 판매되었고, 해당 상품이 오픈된 직후 주문 폭주로 인해 홈페이지가 일시적으로 다운되는 사태가 발생하기도 하였습니다.
            ''')
            st.write(' ')
            st.write(' ')

            st.write(f"**2. 유튜브 검색량으로 알아보는 푸바오의 인기**")
            trend_fubao = tf.TrendFubao("trend_fubao.csv")
            fubao_graph = trend_fubao.plot_monthly_search_volume()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(fubao_graph)
            st.info('''
            올해 초, 우리는 긴 지친 코로나의 그림자로부터 벗어나며 새로운 희망과 함께 봄을 맞이했습니다. 그동안의 거리두기와 마스크 착용의 일상이 조금씩 누그러지자, 우리의 시선은 푸바오에게로 향했습니다.\n
            푸바오, 그 귀여운 판다는 이제까지 우리의 마음을 사로잡고 있었습니다. 그러나 4월부터, 푸바오의 존재와 이야기는 한층 더 주목받기 시작했습니다. 특히, 한 TV 프로그램을 통해 푸바오의 사육사와의 따뜻한 인연이 소개되면서, 그의 인기는 폭발적으로 증가했습니다.\n
            4월부터 차츰 푸바오의 검색량이 증가하더니 5월부터는 폭발적으로 증가하고 있는 추세입니다.
            ''')
            st.write(' ')
            st.write(' ')
            
            st.write(f"**3. 에버랜드 동물원 유튜브 채널 '말하는동물원 뿌빠TV'의 최근 50개 동영상 비율로 알아보는 푸바오 인기**")
            st.image(self.image10)
            st.info('''
            에버랜드는 푸바오를 효과적으로 마케팅 활용하고 있음을 확인할 수 있습니다. '말하는동물원 뿌빠TV'의 영상들은 에버랜드의 동물원과 관련된 컨텐츠로, 푸바오와 사육사분들의 모습을 다양하게 보여주고 있습니다. 푸바오가 포함된 영상은 전체의 과반수 이상을 차지하고 있습니다.\n
            더불어, 푸바오를 포함한 동영상의 조회수가 전체 조회수의 80% 이상을 차지하고 있으므로, 이 컨텐츠가 관람객들에게 높은 관심을 불러일으키고 있음을 알 수 있습니다. 이는 푸바오를 특별한 캐릭터로 활용하고 있는 결과로 보입니다.\n
            에버랜드가 푸바오를 성공적으로 마케팅하고 있다는 것은 동물원의 인기를 높이고, 더불어 에버랜드 방문객들에게 더 많은 관심을 끌고 있다는 것을 시사합니다. 푸바오의 매력을 잘 포착하여 다양한 콘텐츠를 제공함으로써, 에버랜드는 관람객들의 기대와 호기심을 충족시키며 성공적인 마케팅 전략을 시행하고 있는 것으로 평가됩니다.
            ''')
        with tab3:
            st.write(f'**1. 푸바오와 호랑이(태범이, 무궁이) 유튜브 조회수 비교**')
            st.image(self.image11)
            st.info('''
            에버랜드의 두 마스코트, 판다 푸바오와 호랑이 태범이 무궁이 유튜브에서의 조회수 경쟁은 흥미로운 결과를 보여주고 있습니다. 2020년에 공개된 호랑이 태범이, 무궁이의 영상이 가장 높은 조회수를 기록했으며, 그 인기는 매우 두드러졌습니다.\n
            그러나 흥미로운 점은 2위부터는 모두 최근에 올라온 푸바오의 영상들이 차지하고 있다는 것입니다. 푸바오의 사랑스러운 모습과 독특한 매력은 유튜브 사용자들 사이에서 큰 인기를 얻고 있으며, 그 결과로 그의 영상들은 높은 조회수를 기록하고 있습니다.\n
            이러한 결과를 통해 푸바오가 얼마나 많은 사람들에게 사랑받고 있는지, 푸바오의 매력이 얼마나 많은 이들을 매료시키고 있는지를 확인할 수 있습니다. 
            ''')

        with tab4:   
            st.markdown('##### 기간별 해당 지역 SNS 언급량')
            col1, col2 = st.columns([3, 3])
            with col1:
                st.image(self.image9)    
            with col2:
                st.write('''
                에버랜드는 경기도 용인시 처인구에 위치해 있는 어트렉션, 사파리, 리조트 등을 포함한 국내 최대의 테마파크입니다. \n
                실제로 호랑이 남매 및 푸바오로 인해 에버랜드가 위치한 용인시 처인구에 대한 대중의 관심이 증가했는지를 확인하기 위해 SNS에서 
                용인시 처인구의 언급량이 어떠한 추세로 변화하였는지 살펴보았습니다.
                ''')

            #graph = SNS('sns_yongin_2019.csv', 'sns_yongin_2021.csv', 'sns_yongin_2023.csv')
            graph = SNS()
            sns_graph = graph.plot_graph()
            st.pyplot(sns_graph)


        with tab5:
            st.write(f'**1. 동물 마케팅 성공에 따른 에버랜드 매출량 변화**')
            sales_comparison = SalesComparison('삼성물산 매출액.xlsx')
            st.pyplot(sales_comparison.plot_sales_comparison())
            st.info('''
            에버랜드의 푸바오를 통한 매출량 변화를 나타내는 그래프를 통해 지난 해와 올해 1,2분기의 매출 변화를 비교해 봤습니다. 그 결과, 작년 대비 1분기의 매출이 상당히 증가한 것을 확인할 수 있었습니다. 이는 코로나19 대응으로 인한 거리두기 및 마스크 착용 규제가 완화되면서, 많은 사람들이 에버랜드를 다시 방문하게 되었기 때문입니다.\n
            하지만 2분기의 매출 변화는 미미한 것으로 나타났습니다. 이것은 푸바오의 인기가 높아진다고 해서 반드시 매출이 급증하는 것은 아니라는 점을 보여줍니다. 푸바오는 분명히 관람객을 매료시키고 관심을 끄는데 성공하였지만, 실제로 이로 인한 매출 변화는 예상보다 미약한 것으로 나타났습니다.\n
            이러한 결과를 통해 푸바오의 인기는 에버랜드에 긍정적인 영향을 미치고 있지만, 매출 증가와 직결되지 않는다는 것을 알 수 있습니다. 따라서 에버랜드는 푸바오의 인기를 더욱 효과적으로 마케팅에 활용하고, 매출을 높이기 위한 다양한 전략을 고려할 필요가 있을 것으로 생각됩니다.
            ''')
            st.write(f'**#. 삼성물산 매출기준(리조트부문)**')
            st.image(self.image7)
            st.write(' ')
            st.write(' ')
            
            st.write(f'**2. 푸바오 중국반환에 따른 마케팅 변화 필요**')
            st.image(self.image6)
            st.info('''
            푸바오의 중국 반환 날짜가 다가옴에 따라, 푸바오의 동생인 쌍둥이 판다의 등장은 중요한 마케팅 기회로 여겨집니다. 이러한 상황에서 어떻게 쌍둥이 판다를 마케팅에 활용할 것인가가 더욱 중요해질 것으로 예상됩니다.\n
            쌍둥이 판다는 푸바오와 함께 매력적인 스토리를 만들 수 있는 주인공입니다. 이들의 성장 과정, 놀라운 모험, 그리고 동화같은 모습들은 에버랜드의 고객들에게 새로운 감동과 기대감을 안겨줄 것입니다.\n
            더불어, 환경 보호 및 교육적 가치를 강조함으로써 사회적 책임을 다하는 기업의 이미지를 높일 수 있을 것입니다.
            ''')


if __name__ == "__main__":
    main = project()
    main.app2()