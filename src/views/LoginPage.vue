<template>
    <v-app id="inspire">
        <v-content>
           <v-container fluid fill-height>
              <v-layout align-center justify-center>
                 <v-flex xs12 sm8 md4>
                    <v-card class="elevation-12">
                       <v-toolbar dark color="primary">
                          <v-toolbar-title>Login form</v-toolbar-title>
                       </v-toolbar>
                       <v-card-text>
                          <v-form>
                             <v-text-field v-model="email"
                                prepend-icon="person"
                                name="login1"
                                label="Login"
                                type="text"
                             ></v-text-field>
                             <v-text-field v-model="password"
                                id="password"
                                prepend-icon="lock"
                                name="password"
                                label="Password"
                                type="password"
                             ></v-text-field>
                          </v-form>
                       </v-card-text>
                       <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn color="primary" @click="login">Login</v-btn>
                       </v-card-actions>
                    </v-card>
                 </v-flex>
              </v-layout>
           </v-container>
        </v-content>
     </v-app>
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
import firebase from '@/plugins/firebase'
export default {
    name: "LoginPage",
    data: function () {
        return { email: "", password: "" };
    },
    methods: {
        login(e) {
            console.log(this.email, this.password)
            firebase
                .auth()
                .signInWithEmailAndPassword(this.email, this.password)
                .then(
                    user => {
                        // this.$router.push("/home");
                        // alert('Successfully login');
                        this.$router.replace("/home");
                        console.log(user)
                    },
                    err => {
                        alert(err.message)
                    });
            e.preventDefault();
        },
        loginWithProvider(e) {
            console.log(e)
            var provider = new firebase.auth.GoogleAuthProvider();
            firebase
                .auth()
                .signInWithPopup(provider)
                .then(
                    user => {
                        this.$router.replace("home")
                        console.log(user)
                    },
                    err => {
                        alert(err.message)
                    });
        }
    }
}
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
</style>