from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt

# 유튜브 API 연동 및 '말하는동물원 뿌빠TV' 검색
DEVELOPER_KEY = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
YOUTUBE_API__SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API__SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)

search_query = '말하는동물원 뿌빠TV'

zoo_channel = youtube.search().list(
    q = search_query,
    order = 'relevance', # 정확도순
    part = 'snippet',
    maxResults = 50
).execute()

# 채널 ID 추출
channel_id = zoo_channel['items'][0]['id']['channelId']

# 채널의 동영상 목록을 가져오기
request = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    order="date",  # 최신순으로 정렬
    maxResults=50,
)

response = request.execute()

video_title_zoo = []
video_id_zoo = []

for item in response["items"]:
    video_title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    video_title_zoo.append(video_title)
    video_id_zoo.append(video_id)

df = pd.DataFrame({"Video Title": video_title_zoo, "Video ID": video_id_zoo})
df.index = df.index + 1

# 말하는동물원 뿌빠TV 동영상의 상세 정보 추출
titles = []         # 동영상 제목
ids = []            # 동영상 id
dates = []          # 동영상 업로드 날짜
views = []          # 조회 수
likes = []          # 좋아요 수
comments = []       # 댓글 수


for i in range(len(video_id_zoo)):
    request = youtube.videos().list(
        id = video_id_zoo[i], # 동영상 id를 입력합니다
        part = 'snippet,contentDetails,statistics'
    )

    response = request.execute()

    if response['items'] == []: # 동영상 정보가 없을 경우 '-'로 입력
        titles.append('-')
        ids.append('-')
        dates.append('-')
        views.append('-')
        likes.append('-')
        comments.append('-')

    else:
        titles.append(response['items'][0]['snippet']['title'])
        ids.append(video_id_zoo[i])
        dates.append(response['items'][0]['snippet']['publishedAt'].split('T')[0])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        comments.append(response['items'][0]['statistics']['commentCount'])

detail_df_zoo = pd.DataFrame([titles,dates,views,likes,comments]).T
detail_df_zoo.index = detail_df_zoo.index+1
detail_df_zoo.columns = ['title','date','view','like','comment']

# 출력
print(detail_df_zoo)

contains_bao = len(detail_df_zoo[detail_df_zoo['title'].str.contains('바오')])
not_contains_bao = len(detail_df_zoo) - contains_bao

data = [contains_bao, not_contains_bao]
labels = ['bao', 'not bao']
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # 도넛 차트처럼 구멍을 뚫기 위해 explode 값을 설정합니다.

# 첫 번째 도넛 차트 그리기
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('bao contain ratio')

# 'view' 열을 int로 변환
detail_df_zoo['view'] = detail_df_zoo['view'].astype(int)

bao_views = detail_df_zoo[detail_df_zoo['title'].str.contains('바오')]['view'].sum()
not_bao_views = detail_df_zoo[~detail_df_zoo['title'].str.contains('바오')]['view'].sum()

data = [bao_views, not_bao_views]
labels = ['bao', 'not bao']
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)

# 두 번째 도넛 차트 그리기
plt.subplot(1, 2, 2)
plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('bao view comparison')

plt.tight_layout()
plt.show()