# 유튜브 AIP 연동 및 푸바오 검색시 조회수 높은 순으로 이름 출력
from googleapiclient.discovery import build

DEVELOPER_KEY = 'AIzaSyCuvYdPw-Lf913DaDTgyEpUiCIjbRdv_yk'
YOUTUBE_API__SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API__SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)

search_query = '푸바오'

search_response = youtube.search().list(
    q = search_query,
    order = 'viewCount', # 조회수 높은 순으로 정렬
    part = 'snippet',
    maxResults = 50 # 0~50까지 가능. 기본값 5
).execute()

# 출력
print(search_response)

# 상세 정보를 불러오기 위해서 동영상 id 추출
video_ids = [item['id']['videoId'] for item in search_response['items']]

# 출력
print(video_ids)

# id에 해당하는 동영상 상세정보 추출
import pandas as pd

titles = []         # 동영상 제목
ids = []            # 동영상 id
dates = []          # 동영상 업로드 날짜
views = []          # 조회 수
likes = []          # 좋아요 수
#dislikes = []       # 싫어요 수는 미제공으로 주석처리
comments = []       # 댓글 수


for i in range(len(video_ids)):
    request = youtube.videos().list(
        id = video_ids[i], # 동영상 id를 입력합니다
        part = 'snippet,contentDetails,statistics'
    )

    response = request.execute()

    if response['items'] == []: # 동영상 정보가 없을 경우 '-'로 입력
        titles.append('-')
        ids.append('-')
        dates.append('-')
        views.append('-')
        likes.append('-')
        #dislikes.append('-')
        comments.append('-')

    else:
        titles.append(response['items'][0]['snippet']['title'])
        ids.append(video_ids[i])
        dates.append(response['items'][0]['snippet']['publishedAt'].split('T')[0])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        #dislikes.append(response['items'][0]['statistics']['dislikeCount'])
        comments.append(response['items'][0]['statistics']['commentCount'])

detail_df = pd.DataFrame([titles,dates,views,likes,comments]).T
detail_df.index = detail_df.index+1
detail_df.columns = ['title','date','view','like','comment']

# 출력
print(detail_df)
