<template>
<div>

    <div class="detail">
    <div>
    <img class="backdropimg"  :src="`https://image.tmdb.org/t/p/original${movie_detail?.backdrop_path}`" alt="">
    </div>

    <div class="info">
        <img class="poseterimg"  :src="`https://image.tmdb.org/t/p/original${movie_detail?.poster_path}`" alt="">
        <span class="detail_title"> {{movie_detail?.title}} </span>
        <!-- 코멘트 -->
        <form @submit.prevent="movieComment(movie_detail?.id)">

            <div @mouseleave="showCurrentRating(0)" style="display:inline-block;">
                    <star-rating :show-rating="false" @current-rating="showCurrentRating" @rating-selected="setCurrentSelectedRating" :increment="0.5"></star-rating>
            </div>
            <div style="margin-top:10px;font-weight:bold;">{{currentRating}}</div>
            <input type="text" v-model="movie_comment">
        </form>

    </div>



  </div>

</div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

export default {
    name: 'MovieDetailView',
    data(){
        return{
            movie_detail: null,
            movie_comment:null,
            currentRating: null,
            currentSelectedRating: null,
            rate: null,

        }
    },
    components: {
    StarRating
    },
    methods:{
        getMovieDetail(movie_pk){
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/movies/${movie_pk}`,
            })
            .then((res)=>{
                this.movie_detail= res.data
            })
            .catch((err)=>console.log(err))
        },
        movieComment(movie_pk){
            axios({
                method:'post',
                url:`http://127.0.0.1:8000/movies/${movie_pk}/comment/`,
                data:{
                    'comment' : this.movie_comment,
                    'rate' : this.rate
                },
                headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
            })
            .then((res)=>{
                console.log(res)
            })
            .catch((err)=>{
                console.log(err)
            })
            
        },
        // 별점
        setRating: function(rating) {
            this.rating = rating;
        },
        showCurrentRating: function(rating) {
            this.currentRating = (rating === 0) ? this.currentSelectedRating : rating * 2 + "점"
        },
        setCurrentSelectedRating: function(rating) {
            this.currentSelectedRating = rating * 2 + "점";
            this.rate = rating * 2
        }
    },
    created(){
        this.getMovieDetail(this.$route.params.movie_pk)
    }
    
}
</script>

<style>
.detail{
    position: relative;
}
.backdropimg{
    width: 100%;
    opacity: 0.1;
    mask-image: linear-gradient(to top, transparent 5%, black 100%);

}
.poseterimg{
    width: 300px;
    border-radius: 30px;
}
.info{
    position: absolute;
    display: flex;
    top: 5%;
    margin: 5%;
    background-color:transparent;

}

.detail_title{
    font-family: NeoLT;
    font-size: 3rem;
    width:500px;
    background-color:transparent;
    margin-left: 10%;
}

</style>