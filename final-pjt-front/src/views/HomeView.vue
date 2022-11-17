<template>
  <div class="home">
    
    <!-- 상위 랜덤 영화 보여주기 -->
    <div>

      <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false" >
        <div class="carousel-indicators" >
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img :src="`https://image.tmdb.org/t/p/original${random_movies[0].backdrop_path}`"  class="w-50" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random_movies[0].title}}</h5>
              <p>Some representative placeholder content for the first slide.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img :src="`https://image.tmdb.org/t/p/original${random_movies[1].backdrop_path}`" class="w-50" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random_movies[1].title}}</h5>
              <p>Some representative placeholder content for the second slide.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img :src="`https://image.tmdb.org/t/p/original${random_movies[2].backdrop_path}`" class="w-50" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random_movies[2].title}}</h5>
              <p>Some representative placeholder content for the third slide.</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>

    </div>



  </div>
</template>

<script>
// import MovieCarousel from '../components/MovieCarousel.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  data(){
    return{
      random_movies:null,
    }
  },
  // components: {MovieCarousel},
  methods:{
    getTitleRandomMovie(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/',
      })
      .then((res)=>{
        this.random_movies = res.data
      })
      .catch((err)=>console.log(err))
    }


  },
  created(){
    this.getTitleRandomMovie()
  }
}
</script>

<style>
.class
.category{
  font-family: NeoBD;
}


</style>