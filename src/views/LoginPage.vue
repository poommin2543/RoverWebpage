<template>
  <v-container fluid class="fill-height ma-0 pa-0">
    <v-card
      color="black"
      class="fill-height rounded-0 d-flex justify-center align-center"
      width="100%"
      dark
    >
      <!-- Outer -->
      <v-card color="black" light height="70vh" width="60vw" class="rounded-0">
        <v-row>
          <v-col>
            <v-card
              class="d-flex align-center justify-center"
              height="70vh"
              color="transparent"
            >
              <img
                :src="require('../assets/img/Classgologologin.svg')"
                alt=""
              />
            </v-card>
          </v-col>
          <v-col>
            <v-card class="rounded-xl" height="70vh">
              <v-card
                flat
                color=" d-flex align-center justify-center "
                height="10vh"
              >
                <div class="headerstext">
                  <p class="mb-n8 pa-0">User Login</p>
                </div>
              </v-card>
              <v-card
                flat
                class="d-flex align-center justify-center rounded-0"
                height="10vh"
              >
                <div class="titletext text-center">
                  <p class="ma-0 pa-0">Enter your username & password</p>
                  <p class="mt-0">to get sign in your account</p>
                </div>
              </v-card>
              <v-card
                flat
                class="d-flex align-center justify-center rounded-0"
                height="20vh"
              >
                <v-form>
                  <v-text-field
                    v-model="email"
                    prepend-icon="person"
                    name="login"
                    label="Email"
                    type="text"
                    :rules="emailRules"
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    id="password"
                    prepend-icon="lock"
                    name="password"
                    label="Password"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card>
              <v-card
                flat
                class="d-flex align-center justify-center rounded-0"
                height="10vh"
              >
                <v-btn color="black" dark @click="login">Sign in</v-btn>
              </v-card>
              <v-card
                flat
                class="d-flex align-center justify-center"
                height="20vh"
              >
                <div class="textics text-center">
                  <p class="ma-0 pa-0">
                    Autonomous Delivery | by iCreative Systems
                  </p>
                </div>
              </v-card>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-card>
  </v-container>
  <!-- <div id="login" class="main-box">
        <form @submit="loginWithEmail">
            <h1>Login</h1>
            <div class="title">
                <h3>Email</h3>
                <input v-model="email" type="text" class="input" placeholder="Email">
            </div>
            <div class="title">
                <h3>Password</h3>
                <input v-model="password" type="password" class="input" placeholder="Password">
            </div>
            <v-btn type="submit" value="submit" class="btn" @click="login">Login</v-btn>
        </form>
        <div>or Sign in with 3rd Party</div>
        <v-btn id="google" @click="loginWithProvider" class="btn-pic">
        </v-btn>
    </div> -->
</template>
<script>
import firebase from "@/plugins/firebase";
export default {
  name: "LoginPage",
  data: function () {
    return {
      email: "",
      password: "",
      emailRules: [],
    };
  },
  watch: {
    email: function (mail) {
      // e_Mail is the exact name used in v-model
      if (mail !== "") {
        this.emailRules = [
          (v) =>
            v.match(
              /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            ) || "Invalid Email address",
        ];
        console.log(this.emailRules)
      } else if (mail === "") {
        this.emailRules = [];
      }
    },
  },
  methods: {
    login(e) {
      console.log(this.email, this.password);
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(
          (user) => {
            // this.$router.push("/home");
            // alert('Successfully login');
            this.$router.replace("/home");
            console.log(user);
          },
          (err) => {
            alert(err.message);
          }
        );
      e.preventDefault();
    },
    loginWithProvider(e) {
      console.log(e);
      var provider = new firebase.auth.GoogleAuthProvider();
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(
          (user) => {
            this.$router.replace("home");
            console.log(user);
          },
          (err) => {
            alert(err.message);
          }
        );
    },
  },
};
</script>
<style>
/* Sign in /Sign up /Reset password */

.imgclassgo {
  position: absolute;
  width: 424px;
  height: 457px;
  left: 305px;
  top: 312px;
}

.headerstext {
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 32px;
  line-height: 100%;
  /* or 32px */

  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: 0.1px;

  /* grey / grey-900 */

  color: #212121;
}

.titletext {
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 100%;
  /* or 20px */

  letter-spacing: 0.2px;

  /* grey / grey-900 */

  color: #212121;
}

.emailblock {
  width: 20px;
}

.v-text-field {
  width: 400px;
}

.v-btn {
  width: 400px;
}

.textics {
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 100%;
  /* identical to box height, or 16px */

  display: flex;
  align-items: center;
  text-align: center;

  /* grey / grey-900 */

  color: #212121;
}
</style>
