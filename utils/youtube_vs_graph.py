from googleapiclient.discovery import build
import matplotlib.pyplot as plt
import pandas as pd

class YouTubeAPI:
    # YouTubeAPI 클래스의 생성자
    def __init__(self, api_key):
        self.DEVELOPER_KEY = api_key
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.YOUTUBE_API_VERSION = 'v3'
        self.youtube = build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY
        )

    # YouTube에서 비디오를 검색하고 비디오 ID를 반환
    def search_videos(self, query, max_results=50):
        search_response = self.youtube.search().list(
            q=query,
            order='viewCount',
            part='snippet',
            maxResults=max_results
        ).execute()
        video_ids = [item['id']['videoId'] for item in search_response['items']]
        return video_ids

    # 비디오 ID 목록에 해당하는 비디오의 상세 정보를 반환
    def get_video_details(self, query, max_results=50):
        video_ids = self.search_videos(query, max_results)
        titles = []
        dates = []
        views = []
        #comments = []

        for video_id in video_ids:
            request = self.youtube.videos().list(
                id=video_id,
                part='snippet,contentDetails,statistics'
            )

            response = request.execute()

            if response['items'] == []:
                titles.append('-')
                dates.append('-')
                views.append('-')
                #comments.append('-')
            else:
                titles.append(response['items'][0]['snippet']['title'])
                dates.append(response['items'][0]['snippet']['publishedAt'].split('T')[0])
                views.append(response['items'][0]['statistics']['viewCount'])
                #comments.append(response['items'][0]['statistics']['commentCount'])

        detail_df = pd.DataFrame([titles, dates, views]).T
        detail_df.index = detail_df.index + 1
        detail_df.columns = ['title', 'date', 'view']
        return detail_df

    # Top 10개 그래프
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
        plt.bar(top_10_videos1['순위'] - 0.2, top_10_videos1['view'], width=0.4, color='#ff9999', label=query1)
        plt.text(0.3, 10000000, '2021.06.29 업로드', rotation=60)
        plt.bar(top_10_videos2['순위'] + 0.2, top_10_videos2['view'], width=0.4, color='#66b3ff', label=query2)
        plt.text(0.7, 40000000, '2020.06.07 업로드', rotation=60)

        plt.xticks(top_10_videos1['순위'])  # x 축 라벨을 순위로 설정
        plt.xlabel('순위')
        plt.ylabel('조회수')
        plt.title(f'Top 10 조회수 비교({query1} vs {query2})')
        plt.legend()
        plt.show()

'''
# 출력 예시
if __name__ == "__main__":
    api_key = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
    query1 = '푸바오'
    query2 = '태범이 무궁이'
    YouTubeAPI.plot_top_10_videos(api_key, query1, query2, max_results=10)
'''