<template>
  <div>
    <div class="form-check" @click="makelist">
      <input
        class="form-check-input"
        type="checkbox"
        v-model="torf"
        :id="movie_list.id"
      />
      <label
        class="form-check-label"
        :for="movie_list.id"
        style="background-color: transparent"
      >
        {{ movie_list.title }}
      </label>
    </div>
    <button @click="deletelist">삭제</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieListCheck",
  props: {
    movie_list: Object,
    movie_id: Number,
  },
  computed: {
    torf: {
      get() {
        const res = this.movie_list.movies.some((x) => {
          return x.id === this.movie_id;
        });
        return res;
      },
      set() {
        const res = this.movie_list.movies.some((x) => {
          return x.id === this.movie_id;
        });
        return res;
      },
    },
  },
  methods: {
    makelist() {
      if (this.torf) {
        axios({
          method: "put",
          url: `http://127.0.0.1:8000/movies/likemovielist/${this.movie_id}/append/${this.movie_list.id}/`,
          headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        })
          .then(() => {
            this.$store.commit("like_movie_list");
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/movies/likemovielist/${this.movie_id}/append/${this.movie_list.id}/`,
          headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        })
          .then(() => {
            this.$store.commit("like_movie_list");
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    deletelist() {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/movies/likemovielist/${this.movie_id}/append/${this.movie_list.id}/`,
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
      })
        .then(() => {
          this.$store.commit("like_movie_list");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>