import matplotlib.pyplot as plt
from youtube_view import YouTubeAPI

def plot_top_10_videos(api_key, query1, query2, max_results=50):
    # YouTubeAPI 클래스 인스턴스 생성
    youtube_api = YouTubeAPI(api_key)

    # 비디오 상세 정보 가져오기
    video_details1 = youtube_api.get_video_details(query1, max_results=max_results)
    video_details2 = youtube_api.get_video_details(query2, max_results=max_results)

    # 데이터 정제
    top_10_videos1 = video_details1.head(10).copy()
    top_10_videos1['view'] = top_10_videos1['view'].str.replace(',', '').astype(int)
    top_10_videos1['순위'] = range(1, 11)

    top_10_videos2 = video_details2.head(10).copy()
    top_10_videos2['view'] = top_10_videos2['view'].str.replace(',', '').astype(int)
    top_10_videos2['순위'] = range(1, 11)

    # 그래프 그리기
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(12, 6))
    plt.bar(top_10_videos1['순위'] - 0.2, top_10_videos1['view'], width=0.4, color='blue', label=query1)
    plt.bar(top_10_videos2['순위'] + 0.2, top_10_videos2['view'], width=0.4, color='red', label=query2)

    plt.xticks(top_10_videos1['순위'])  # x 축 라벨을 순위로 설정
    plt.xlabel('순위')
    plt.ylabel('조회수')
    plt.title(f'Top 10 조회수 비교({query1} vs {query2})')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    api_key = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
    query1 = '푸바오'
    query2 = '태범이 무궁이'
    plot_top_10_videos(api_key, query1, query2, max_results=50)
