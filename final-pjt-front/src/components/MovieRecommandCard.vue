<template>
  <div>
    
        <div class="col">
          <div class="card card-container border-0 moviecard" 
          @click="getMovieId()"
          style="width:16rem; height:24rem;">
            <p class="movie-title">{{recomovie.title}} </p>
            <img :src="`https://image.tmdb.org/t/p/w500${recomovie.poster_path}`" class="card-img-top reco-cardimg " alt="..."
            style="width:16rem; height:24rem;" 
            >
          </div>

    </div>


  </div>

</template>

<script>
export default {
    name:'MovieRecommandCard',
    props:{recomovie: Object,},
    methods:{
      getMovieId(){
        this.$router.push({name:'moviedetail', params:{movie_pk:this.recomovie.id}})
      }
    },
    created(){}

}
</script>

<style>
.moviecard{
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

.card-container{
  position:relative;
  background-color:transparent;

}

.moviecard:hover {
  background-color:transparent;
}

.reco-cardimg:hover{
  opacity: 0.3;
}


.movie-title{
  position: absolute;
  opacity: 0;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: NeoEB;
  font-size: 1.4rem;
  background-color:transparent;
  word-wrap: break-word;
  text-shadow: 0.2rem 0.2rem 5rem black ;

  }
  


.moviecard:hover .movie-title{
  opacity: 1;
  color: white;
  word-break: keep-all;

}

</style>