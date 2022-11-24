import Vue from "vue";
import Vuex from "vuex";
import article from "@/store/modules/article";
import movie from "@/store/modules/movie";
import axios from "axios";
import _ from 'lodash'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    is_logined: false,
    user_movie_list: null,
    movies: null,
    onscreen_movie: null,
    user_movie: null,
  },
  getters: {},
  mutations: {
    like_movie_list(state) {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/likemovie/`,
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
      })
        .then((res) => {
          state.user_movie_list = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 추천 영화 만약 리스트에 정보가 있으면,

    // 무비 리스트 불러오기
    logins(state) {
      if (localStorage.getItem("jwt")) {
        state.is_logined = true;
        axios({
          method: "get",
          url: `http://127.0.0.1:8000/movies/likemovie/`,
          headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        })
          .then((res) => {
            state.user_movie_list = res.data;
          })
          .then(() => {
            let m = [];
            state.user_movie_list.forEach((movie_list) => {
              m = m.concat(movie_list.movies)
            });
            let a = _.random(m.length)
            m = [m[a]]
            axios({
              method: "POST",
              url: 'http://127.0.0.1:8000/movies/recommend/',
              data: {
                'movies': m,
              },
              headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
            })
              .then((res) => {
                state.user_movie = res.data
                console.log(res.data);
              })
              .catch(() => {
                axios({
                  method: "get",
                  url: "http://127.0.0.1:8000/movies/nothing/",
                })
                  .then(() => {
                  })
                  .catch((err) => {
                    console.log(err);
                  });
              });
          })
      } else {
        state.is_logined = false;
      }
    },
    // 로그아웃기능
    logout(state) {
      localStorage.removeItem("jwt");
      state.is_logined = false;
      state.user_movie_list = null;
    },
    // 영화 저장하기
    CREATE_MOIVE(state) {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/",
      })
        .then((res) => {
          state.movies = res.data;
        })
        .catch(() => {
          axios({
            method: "get",
            url: "http://127.0.0.1:8000/movies/nothing/",
          })
            .then(() => {
            })
            .catch((err) => {
              console.log(err);
            });
        });
    },
    ONSCREEN(state, onsc) {
      state.onscreen_movie = onsc;
    },
  },
  actions: {
    movie_list_create(context, payload) {
      axios({
        method: "POST",
        url: `http://127.0.0.1:8000/movies/likemovielist/${payload?.movie_id}/${payload?.list_id}/`,
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        data: {
          title: payload?.title,
        },
      })
        .then(() => {
          context.commit("like_movie_list");
        })
        .catch(() => {
          axios({
            method: "get",
            url: "http://127.0.0.1:8000/movies/nothing/",
          })
            .then(() => {
            })
        });
    },
    movie_list_new(context, payload) {
      axios({
        method: "POST",
        url: `http://127.0.0.1:8000/movies/likemovienew/${payload?.movie_id}/`,
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        data: {
          title: payload?.title,
        },
      })
        .then(() => {
          context.commit("like_movie_list");
        })
        .catch(() => {
          axios({
            method: "get",
            url: "http://127.0.0.1:8000/movies/nothing/",
          })
            .then(() => {
            })
        });
    },
    onscreen_movie(context) {
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/movies/onscreen/`,
      })
        .then((res) => {
          context.commit("ONSCREEN", res.data);
        })
        .catch(() => {
          axios({
            method: "get",
            url: "http://127.0.0.1:8000/movies/nothing/",
          })
            .then(() => {
            })
        });
    },
  },
  modules: {
    article,
    movie,
  },
});
