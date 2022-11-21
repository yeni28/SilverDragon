<template>
  <div>
    <form @submit.prevent="signup">
      <div class="form-group">
      <label for="username">username : </label>
      <input
        type="text"
        id="username"
        v-model="username"
        class="text-light"
      />
      <span class="error"></span>
      </div>
      <br />

      <div class="form-group">
      <label for="password1"> password : </label>
      <input
        type="password"
        id="password1"
        v-model="password1"
        class="text-light"
      />
      <span class="error"></span>
      </div>
      <br />

      <div class="form-group">
      <label for="password2"> password confirmation : </label>
      <input
        type="password"
        id="password2"
        v-model="password2"
        class="text-light"
      />
      <span class="error"></span>
      </div>
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

<!-- <script>

$(document).ready(function () {

'use strict';

const usernameError = true,
    passwordError = true,
    passConfirm   = true;

// Detect browser for css purpose
if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
    $('.form form label').addClass('fontSwitch');
}

// Label effect
$('input').focus(function () {

    $(this).siblings('label').addClass('active');
});

// Form validation
$('input').blur(function () {

    // User Name
    if ($(this).hasClass('name')) {
        if ($(this).val().length === 0) {
            $(this).siblings('span.error').text('Please type your full name').fadeIn().parent('.form-group').addClass('hasError');
            usernameError = true;
        } else if ($(this).val().length > 1 && $(this).val().length <= 6) {
            $(this).siblings('span.error').text('Please type at least 6 characters').fadeIn().parent('.form-group').addClass('hasError');
            usernameError = true;
        } else {
            $(this).siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
            usernameError = false;
        }
    }

    // PassWord
    if ($(this).hasClass('pass')) {
        if ($(this).val().length < 8) {
            $(this).siblings('span.error').text('Please type at least 8 charcters').fadeIn().parent('.form-group').addClass('hasError');
            passwordError = true;
        } else {
            $(this).siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
            passwordError = false;
        }
    }

    // PassWord confirmation
    if ($('.pass').val() !== $('.passConfirm').val()) {
        $('.passConfirm').siblings('.error').text('Passwords don\'t match').fadeIn().parent('.form-group').addClass('hasError');
        passConfirm = false;
    } else {
        $('.passConfirm').siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
        passConfirm = false;
    }

    // label effect
    if ($(this).val().length > 0) {
        $(this).siblings('label').addClass('active');
    } else {
        $(this).siblings('label').removeClass('active');
    }
});


// form switch
$('a.switch').click(function (e) {
    $(this).toggleClass('active');
    e.preventDefault();

    if ($('a.switch').hasClass('active')) {
        $(this).parents('.form-peice').addClass('switched').siblings('.form-peice').removeClass('switched');
    } else {
        $(this).parents('.form-peice').removeClass('switched').siblings('.form-peice').addClass('switched');
    }
});


// Form submit
$('form.signup-form').submit(function (event) {
    event.preventDefault();

    if (usernameError == true || emailError == true || passwordError == true || passConfirm == true) {
        $('.name, .email, .pass, .passConfirm').blur();
    } else {
        $('.signup, .login').addClass('switched');

        setTimeout(function () { $('.signup, .login').hide(); }, 700);
        setTimeout(function () { $('.brand').addClass('active'); }, 300);
        setTimeout(function () { $('.heading').addClass('active'); }, 600);
        setTimeout(function () { $('.success-msg p').addClass('active'); }, 900);
        setTimeout(function () { $('.success-msg a').addClass('active'); }, 1050);
        setTimeout(function () { $('.form').hide(); }, 700);
    }
});

// Reload page
$('a.profile').on('click', function () {
    location.reload(true);
}); -->


});


<!-- </script> -->

<style>

.span.error{
      color: crimson;
      font-family:;
      font-size: 12px;
      position: absolute;
      bottom: -20px;
      right: 0;
      display: none;
}

</style>
