<template>
<div>
    <div class="">
        <div>
            <img class="col_image" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" alt="">
        </div>
        {{movie.title}}

    </div>
</div>
</template>

<script>
export default {
    name:"MovieCollectionCard",
    props:{
        movie:Object,
    }
}
</script>

<style>
.col_image{
    border-radius: 1rem;
    width:25rem;
    height: 14rem;
    box-shadow: 0.3rem 0.3rem 0.6rem black;
}
</style>