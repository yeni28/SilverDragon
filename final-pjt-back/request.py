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

# 영화 json
movies_json_data = []

# 배우 json
actor_json_data = []
actor_pk_list = []
# 감독 json
director_json_data = []
director_pk_list = []


for i in range(1,4):
    urls = f'https://api.themoviedb.org/3/movie/popular?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR&page={i}'

    datas = requests.get(urls)
    movie_data = datas.json()

    for movie in movie_data['results']:

        # 가져온 movie["id"]로 crew 구하기
        movie_crew_path = f'https://api.themoviedb.org/3/movie/{movie["id"]}/credits?api_key=6f6513726d3b3eef83b5927098909d71&language=ko-KR'
        response_crew = requests.get(movie_crew_path)
        crew_data = response_crew.json()
        
        # 감독 데이터와 배우데이터를 너을 리스트
        director_movie = []
        actor_movie = []
        # 배우 데이터 만들기
        if len(crew_data["cast"]) >= 3:
            for n in range(3):
                cast = crew_data["cast"][n]
                # movie의 actor필드에 너을 것을 더해줌
                actor_movie.append(cast["id"])

                # actor 에 중복값을 제거하기위한
                if cast["id"] in actor_pk_list:
                    continue
                else:
                    actor_pk_list.append(cast["id"])

                    actor_json_data.append({
                        "model" : "movies.actor",
                        "pk" : cast["id"],
                        "fields" : {
                            "name" : cast["name"],
                            "profile_path" : cast["profile_path"]
                        }
                    })
            

        # 감독 데이터 만들기
        crews = crew_data["crew"]

        for crew in crews:
            if crew["job"] == "Director":
                director_movie.append(crew["id"])

                if crew["id"] not in director_pk_list:
                    director_pk_list.append(crew["id"])

                    director_json_data.append({
                        "model" : "movies.director",
                        "pk" : crew["id"],
                        "fields" : {
                            "name" : crew["name"],
                            "profile_path" : crew["profile_path"]
                        }
                    })


                break



        # 무비 json 구하기
        movies_json_data.append({
            "model" : "movies.movie",
            "pk" : movie["id"],
            "fields" : {
                "title" : movie["title"],
                "release_date" : movie["release_date"],
                "popularity" : movie["popularity"],
                "vote_count" : movie["vote_count"],
                "vote_average" : movie["vote_average"],
                "overview" : movie["overview"],
                "poster_path" : movie["poster_path"],
                "backdrop_path" : movie["backdrop_path"],
                "genres" : movie["genre_ids"],
                "actor" : actor_movie,
                "director" : director_movie,
            }
        })

# 영화 json 파일 쓰기
file_path_movie = './movies/fixtures/movie.json'

with open(file_path_movie, 'w') as file:
    json.dump(movies_json_data, file, indent=4)

# 배우 json 파일 쓰기
file_path_actor = './movies/fixtures/actor.json'

with open(file_path_actor, 'w') as file_actor:
    json.dump(actor_json_data, file_actor, indent=4)

# 감독 json 파일 쓰기
file_path_director = './movies/fixtures/director.json'

with open(file_path_director, 'w') as file_director:
    json.dump(director_json_data, file_director, indent=4)



# 장르json 작성

file_path = './movies/fixtures/genre.json'
data = response.json()["genres"]

js_data = []

for gen in data:
    js_data.append({
        "model" :  "movies.genre",
        "pk" : gen["id"],
        "fields" : {
            "name" : gen["name"]
        }
    })


with open(file_path, 'w') as file:
    json.dump(js_data, file, indent=4)
    # json.dump(js_data, file, ensure_ascii=False)


    
