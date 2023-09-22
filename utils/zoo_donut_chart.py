from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt

class YouTubeChannelAnalyzer:
    def __init__(self, api_key):
        self.DEVELOPER_KEY = api_key
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.YOUTUBE_API_VERSION = 'v3'
        self.youtube = build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY
        )

    # 채널 정보 가져오기
    def get_channel_info(self, channel_name):
        search_query = channel_name
        zoo_channel = self.youtube.search().list(
            q=search_query,
            order='relevance',
            part='snippet',
            maxResults=1  # 채널 정보는 하나만 필요하므로 maxResults를 1로 설정
        ).execute()

        if 'items' in zoo_channel and zoo_channel['items']:
            channel_id = zoo_channel['items'][0]['snippet']['channelId']
        else:
            print("채널 정보를 찾을 수 없습니다.")
            return None

        return channel_id

    # 채널의 동영상 목록 가져오기
    def get_channel_videos(self, channel_id, max_results=50):
        if not channel_id:
            return None

        request = self.youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",
            maxResults=max_results,
        )

        response = request.execute()

        video_titles = []
        video_ids = []

        for item in response["items"]:
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_titles.append(video_title)
            video_ids.append(video_id)

        return video_titles, video_ids

    # 비디오 상세 정보 가져오기
    def get_video_details(self, video_ids):
        if not video_ids:
            return None

        titles = []
        dates = []
        views = []
        likes = []
        comments = []

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
                likes.append('-')
                comments.append('-')
            else:
                titles.append(response['items'][0]['snippet']['title'])
                dates.append(response['items'][0]['snippet']['publishedAt'].split('T')[0])
                views.append(response['items'][0]['statistics']['viewCount'])
                likes.append(response['items'][0]['statistics']['likeCount'])
                comments.append(response['items'][0]['statistics']['commentCount'])

        detail_df = pd.DataFrame([titles, dates, views, likes, comments]).T
        detail_df.index = detail_df.index + 1
        detail_df.columns = ['title', 'date', 'view', 'like', 'comment']

        return detail_df

    # 채널 분석 결과 시각화
    def plot_channel_analysis(self, detail_df):
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False

        contains_bao = len(detail_df[detail_df['title'].str.contains('바오')])
        not_contains_bao = len(detail_df) - contains_bao

        data = [contains_bao, not_contains_bao]
        labels = ['바오포함', '바오 미포함']
        colors = ['#ff9999', '#66b3ff']
        explode = (0.1, 0)

        # 첫 번째 도넛 차트 그리기
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title("'바오'가 포함된 영상 갯수 비율")

        # 'view' 열을 int로 변환
        detail_df['view'] = detail_df['view'].astype(int)

        bao_views = detail_df[detail_df['title'].str.contains('바오')]['view'].sum()
        not_bao_views = detail_df[~detail_df['title'].str.contains('바오')]['view'].sum()

        data = [bao_views, not_bao_views]
        labels = ['바오포함', '바오 미포함']
        colors = ['#ff9999', '#66b3ff']
        explode = (0.1, 0)

        # 두 번째 도넛 차트 그리기
        plt.subplot(1, 2, 2)
        plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title("'바오'가 포함된 유튜브 조회수 비교")

        plt.tight_layout()
        plt.show()
'''
# 사용 예시
if __name__ == "__main__":
    api_key = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
    channel_analyzer = YouTubeChannelAnalyzer(api_key)
    channel_name = '말하는동물원 뿌빠TV'
    channel_id = channel_analyzer.get_channel_info(channel_name)

    if channel_id:
        video_titles, video_ids = channel_analyzer.get_channel_videos(channel_id)
        video_details = channel_analyzer.get_video_details(video_ids)
        print(video_details)
        channel_analyzer.plot_channel_analysis(video_details)
'''