<template>

    <div class="carousel-item active">
        <img :src="`https://image.tmdb.org/t/p/original${randommovie.backdrop_path}`" class="d-block w-100" alt="#">
        <div class="carousel-caption d-none d-md-block">
            <h5>{{randommovie.title}}</h5>
        </div>
    </div>


</template>

<script>
export default {
    name:'MovieCarousel',
    props:{
        randommovie: Object,

    }
}
</script>

<style>

</style>