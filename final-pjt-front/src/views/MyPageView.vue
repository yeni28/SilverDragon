<template>
  <div>
    <div class="mypage">
      <div class="profile_area">
        <div>
          프로필이 들어갈 자리
        </div>
      </div>

      <div class="mycontent">
        <div>
          콘텐츠 들어갈 자리
        </div>
        <div>
          {{commentLists}}
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'MyPageView',
    data(){
      return{
        commentLists:null,
      }
    },
    methods:{
      commentList(){
        axios({
          method:'get',
          url:"http://127.0.0.1:8000/movies/comment/",
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
        })
        .then((res)=>{
          console.log(res)
          this.commentLists = res.data
        })
        .catch((err)=>console.log(err))
      }
    },
    created(){
      this.commentList()
    }
}
</script>

<style>
.mypage{
  display: block;
}

.profile_area{
  float:left;
  width:25%;
  height: 20rem;
  border: solid 0.1rem white;
}

.mycontent{
  float:right;
  width:65%;
  border: solid 0.1rem white;

}

</style>