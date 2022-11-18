<template>
  <div>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input
        type="text"
        id="username"
        v-model="username"
        class="text-light"
      /><br />

      <label for="password1"> password : </label>
      <input
        type="password"
        id="password1"
        v-model="password1"
        class="text-light"
      /><br />

      <label for="password2"> password confirmation : </label>
      <input
        type="password"
        id="password2"
        v-model="password2"
        class="text-light"
      />
      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUpView",
  data: function () {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signup: function () {
      const username = this.username;
      const password = this.password1;
      const password2 = this.password2;

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: {
          username,
          password,
          password2,
        },
      })
        .then(() => {
          this.$router.push({ name: "home" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
