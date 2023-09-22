import streamlit as st
from PIL import Image
from utils import zoo_donut_chart as zoo
from utils import trend_fubao as tf
from utils import youtube_vs_graph as yvg
from utils.visitor_gr import VisitorData
class project:
    def __init__(self):
        self.subheader = '조별 프로젝트'
        self.image1_path = 'page\\img\\fubao_news.png'
        self.image1 = Image.open(self.image1_path)
        self.image2_path = 'page\\img\\ba1.png'
        self.image3_path = 'page\\img\\ba2.png'
        self.image4_path = 'page\\img\\ba3.png'
        self.image5_path = 'page\\img\\ba4.png'
        self.image2 = Image.open(self.image2_path)
        self.image3 = Image.open(self.image3_path)
        self.image4 = Image.open(self.image4_path)
        self.image5 = Image.open(self.image5_path)

    def app2(self):
        st.subheader(self.subheader)
        tab1, tab2, tab3, tab4 = st.tabs(['방문객 변화', '푸바오', '한국 호랑이', '매출량 변화'])
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
            푸바오의 인기는 그야말로 폭발적입니다. 국내 최초 자연번식으로 태어난 판다로서, 그의 독특한 매력은 많은 이들의 마음을 사로잡았습니다.
            푸바오가 최근 TV 프로그램에서 돌보는 사육사와의 따뜻한 이야기가 알려지면서, 그의 매력은 한층 더 돋보이게 되었습니다. 
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
            올해 초, 우리는 긴 지친 코로나의 그림자로부터 벗어나며 새로운 희망과 함께 봄을 맞이했습니다. 그동안의 거리두기와 마스크 착용의 일상이 조금씩 누그러지자, 우리의 시선은 푸바오에게로 향했습니다.
            푸바오, 그 귀여운 판다는 이제까지 우리의 마음을 사로잡고 있었습니다. 그러나 4월부터, 푸바오의 존재와 이야기는 한층 더 주목받기 시작했습니다. 특히, 한 TV 프로그램을 통해 푸바오의 사육사와의 따뜻한 인연이 소개되면서, 그의 인기는 폭발적으로 증가했습니다.
            4월부터 차츰 푸바오의 검색량이 증가하더니 5월부터는 폭발적으로 증가하고 있는 추세입니다.
            ''')
            st.write(' ')
            st.write(' ')
            
            st.write(f"**3. 에버랜드 동물원 유튜브 채널 '말하는동물원 뿌빠TV'의 최근 50개 동영상 비율로 알아보는 푸바오 인기**")
            api_key = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
            channel_analyzer = zoo.YouTubeChannelAnalyzer(api_key)
            channel_name = '말하는동물원 뿌빠TV'
            channel_id = channel_analyzer.get_channel_info(channel_name)

            if channel_id:
                video_titles, video_ids = channel_analyzer.get_channel_videos(channel_id)
                video_details = channel_analyzer.get_video_details(video_ids)
                fig = channel_analyzer.plot_channel_analysis(video_details)
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(fig)
            else:
                st.write("채널 정보를 찾을 수 없습니다.")
            st.info('''
            에버랜드는 푸바오를 효과적으로 마케팅 활용하고 있음을 확인할 수 있습니다. '말하는동물원 뿌빠TV'의 영상들은 에버랜드의 동물원과 관련된 컨텐츠로, 푸바오와 사육사분들의 모습을 다양하게 보여주고 있습니다. 푸바오가 포함된 영상은 전체의 과반수 이상을 차지하고 있습니다.
            더불어, 푸바오를 포함한 동영상의 조회수가 전체 조회수의 80% 이상을 차지하고 있으므로, 이 컨텐츠가 관람객들에게 높은 관심을 불러일으키고 있음을 알 수 있습니다. 이는 푸바오를 특별한 캐릭터로 활용하고 있는 결과로 보입니다.
            에버랜드가 푸바오를 성공적으로 마케팅하고 있다는 것은 동물원의 인기를 높이고, 더불어 에버랜드 방문객들에게 더 많은 관심을 끌고 있다는 것을 시사합니다. 푸바오의 매력을 잘 포착하여 다양한 콘텐츠를 제공함으로써, 에버랜드는 관람객들의 기대와 호기심을 충족시키며 성공적인 마케팅 전략을 시행하고 있는 것으로 평가됩니다.
            ''')
        with tab3:
            st.write(f'**1. 푸바오와 호랑이(태범이, 무궁이) 유튜브 조회수 비교**')
            api_key = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
            query1 = '푸바오'
            query2 = '태범이 무궁이'
            vs_graph = yvg.YouTubeAPI.plot_top_10_videos(api_key, query1, query2, max_results=10)
            st.pyplot(vs_graph)
            st.info('''
            에버랜드의 두 마스코트, 판다 푸바오와 호랑이 태범이 무궁이 유튜브에서의 조회수 경쟁은 흥미로운 결과를 보여주고 있습니다. 2020년에 공개된 호랑이 태범이, 무궁이의 영상이 가장 높은 조회수를 기록했으며, 그 인기는 매우 두드러졌습니다.
            그러나 흥미로운 점은 2위부터는 모두 최근에 올라온 푸바오의 영상들이 차지하고 있다는 것입니다. 푸바오의 사랑스러운 모습과 독특한 매력은 유튜브 사용자들 사이에서 큰 인기를 얻고 있으며, 그 결과로 그의 영상들은 높은 조회수를 기록하고 있습니다.
            이러한 결과를 통해 푸바오가 얼마나 많은 사람들에게 사랑받고 있는지, 푸바오의 매력이 얼마나 많은 이들을 매료시키고 있는지를 확인할 수 있습니다. 
            ''')
            
        with tab4:
            st.write('동물 마케팅 성공에 따른 에버랜드 매출량 변화')


if __name__ == "__main__":
    main = project()
    main.app2()