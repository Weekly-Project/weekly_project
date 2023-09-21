from googleapiclient.discovery import build
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

# 출력
if __name__ == "__main__":
    api_key = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
    youtube_api = YouTubeAPI(api_key)
    query = '푸바오'
    video_details = youtube_api.get_video_details(query, max_results=50)
    print(video_details)