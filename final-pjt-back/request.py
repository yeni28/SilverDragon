import requests
import json
# respons = requests.get("https://api.themoviedb.org/3/movie/123?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR")
# https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page=1

# 장르 url
# https://api.themoviedb.org/3/genre/movie/list?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR

response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR")
movie_popular_response =requests.get('https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page=1')
# print(movie_popular_response.json()['results']['id'])

## movie id값 구하기
## 1페이지부터 3페이지 까지 돌기
movie_id = []

movies_json_data = []


for i in range(1,4):
    urls = f'https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page={i}'

    datas = requests.get(urls)
    movie_data = datas.json()

    for movie in movie_data['results']:
        movie_id.append(movie["id"])
        movies_json_data.append({
            "model" : "movies.movie",
            "fields" : {
                "title" : movie["title"],
                "release_date" : movie["release_date"],
                "popularity" : movie["popularity"],
                "vote_count" : movie["vote_count"],
                "vote_average" : movie["vote_average"],
                "overview" : movie["overview"],
                "poster_path" : movie["poster_path"],
                "backdrop_path" : movie["backdrop_path"],
                "genres" : movie["genre_ids"]
            }
        })

print(movies_json_data)

file_path_movie = './movies/fixtures/movie.json'


with open(file_path_movie, 'w') as file:
    json.dump(movies_json_data, file, indent=4)







# file_path = './movies/fixtures/genre.json'
# data = response.json()["genres"]

# js_data = []

# for gen in data:
#     js_data.append({
#         "model" :  "movies.genre",
#         "pk" : gen["id"],
#         "fields" : {
#             "name" : gen["name"]
#         }
#     })

# print(js_data)


# # print(data)

# with open(file_path, 'w') as file:
#     json.dump(js_data, file)
#     # json.dump(js_data, file, ensure_ascii=False)

