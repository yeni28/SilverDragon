import requests
import json
# respons = requests.get("https://api.themoviedb.org/3/movie/123?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR")
# https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page=1

# 장르 url
# https://api.themoviedb.org/3/genre/movie/list?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR

# response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR")
# movie_popular_response =requests.get('https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page=1')
# print(movie_popular_response.json()['results']['id'])



## movie id값 구하기
## 1페이지부터 3페이지 까지 돌기

# 영화 json
movies_json_data = []

# 배우 json
actor_json_data = []
actor_pk_list = []
# 감독 json
director_json_data = []
director_pk_list = []
# 연관 영화 json
re_movie_data = []
re_movie_pk_list = []
# keyword
keyword_list = set()


for i in range(1,4):
    urls = f'https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page={i}'

    datas = requests.get(urls)
    movie_data = datas.json()

    for movie in movie_data['results']:
        # keyword 구하기
        keword_urls = f'https://api.themoviedb.org/3/movie/{movie["id"]}/keywords?api_key=6f6513726d3b3eef83b5927098909d71'
        respons_key = requests.get(keword_urls)
        key_data = respons_key.json()
        keyword_data = key_data["keywords"]
        for keyw in keyword_data:
            keyword_list.add(keyw["name"])


print(len(keyword_list))