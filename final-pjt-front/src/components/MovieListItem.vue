<template>
  <div>
    <div class="col">
      <div
        class="card card-container border-0 moviecard"
        style="width: 16rem; height: 24rem"
        :class="{ ba }"
      >
        <p class="movie-title" :class="{ select: torf }">
          {{ recomovie.title }}
        </p>
        <img
          :src="`https://image.tmdb.org/t/p/w500${recomovie.poster_path}`"
          class="card-img-top cardimg"
          alt="..."
          @click="recommand_movie(recomovie)"
          style="width: 16rem; height: 24rem"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieListitem",
  props: { recomovie: Object, movie_cart: Array },
  methods: {
    recommand_movie(movie) {
      this.$emit("cart", movie);
    },
  },
  computed: {
    torf() {
      const res = this.movie_cart.some((x) => {
        console.log(x);
        return x.title === this.recomovie.title;
      });
      return res;
    },
  },
};
</script>

<style>
.moviecard {
  background-color: black;
  box-shadow: 10px 10px 30px black;
  position: relative;
}

/* .moviecard::before{
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  background-color: #000;
} */

.card-container {
  position: relative;
  background-color: transparent;
}

.moviecard:hover {
  background-color: transparent;
}

.cardimg:hover {
  opacity: 0.3;
}

.movie-title {
  position: absolute;
  opacity: 0;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: NeoEB;
  font-size: 1.4rem;
  background-color: transparent;
  word-wrap: break-word;
  text-shadow: 0.2rem 0.2rem 5rem black;
  /* -webkit-text-stroke-width: 0.8px;
  -webkit-text-stroke-color: rgb(8, 8, 8); */
}

.moviecard:hover .movie-title {
  opacity: 1;
  color: white;
  word-break: keep-all;
  /* z-index: 5 ; */
}

.select {
  opacity: 1;
  color: white;
  word-break: keep-all;
  /* z-index: 5 ; */
}
</style>