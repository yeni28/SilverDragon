<template>
  <div class="recommand_movie1">
    <h3 style="font-family: NeoBD">당신을 위한 추천 영화</h3>
    <div class="row row-cols row-cols-md-5 g-5 outcard" style="margin-top: 5px">
      <movie-recommand-card
        v-for="recomovie in recomovies"
        :key="recomovie.id"
        :recomovie="recomovie"
      />
    </div>
  </div>
</template>

<script>
import MovieRecommandCard from "../../components/MovieRecommandCard.vue";
export default {
  components: { MovieRecommandCard },
  name: "ReusltRecoView",
  computed: {
    recomovies() {
      return this.$store.state.movie.recommandation;
    },
  },
};
</script>

<style>
</style>