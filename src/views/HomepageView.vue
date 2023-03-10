<template>
    <v-container fluid class="fill-height ma-0 pa-0">
        <v-navigation-drawer image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg" permanent color="primary"
            width="250">
            <!-- <v-icon>home</v-icon> -->
            <v-card width="100%" height="8%" color="red" class="">
                <v-row no-gutters>
                    <v-card cols="2">
                        <v-sheet class="pl-5 mt-4">
                            <v-avatar color="blue">
                                <span class="text-h5">NP</span>
                            </v-avatar>
                        </v-sheet>
                    </v-card>
                    <v-card>
                        <v-sheet class="pl-6 mt-6 ">
                            <p>Admin</p>
                        </v-sheet>
                    </v-card>
                </v-row>
            </v-card>
            <v-card width="100%" height="30%" color="blue" class="pa-0 ma-0">
                <p class="pt-3 ml-3">RoverList</p>
                <v-card width="90%" height="80%" color="white" class="pa-0 ma-3 mt-n4 scrolling rounded-3">
                    <v-list>
                        <v-list-item-group v-model="model" mandatory color="indigo">
                            <v-list-item v-for="(item, i) in items" :key="i">
                                <v-list-item-icon>
                                    <v-icon v-text="item.icon"></v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title v-text="item.text"></v-list-item-title>
                                </v-list-item-content>
                                <v-list-item-icon>
                                    <v-icon color="green">circle</v-icon>
                                </v-list-item-icon>
                            </v-list-item>
                        </v-list-item-group>
                    </v-list>
                </v-card>
            </v-card>
            <v-card width="100%" height="30%" color="red" class="">
                <p class="pt-4 ml-3">Status</p>
                <v-card width="90%" height="80%" class="pa-0 ma-3 mt-n4 scrolling">
                    <v-card width="89%" height="89%" class="pa-0 ma-3 bgg">
                        <p class="pl-8 ma-n3 ">Rover Status.</p>
                        <div width="100%" height="100%" class="pa-0 ma-0 bgg">
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ma-2 ">Rover No.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ma-2">Rover No.</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Status.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">Status.</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Door.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">Door.</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Battery.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">Battery.</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Velocity.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">Velocity.</p>
                                </v-col>
                            </v-row>
                        </div>
                    </v-card>
                </v-card>
                <v-card width="100%" height="50%" color="blue" class="">
                    <p class="pt-4 ml-3">RoverMode</p>
                    <v-card width="90%" height="52%" color="white" class="pa-0 ma-3 mt-n4 scrolling">
                        <v-btn block color="success" variant="outlined" class="pa-0 mb-1">
                            Click
                        </v-btn>
                        <v-btn block color="success">
                            Click
                        </v-btn>
                    </v-card>
                </v-card>
                <v-card width="100%" height="58%" color="red" class="">
                </v-card>
            </v-card>
        </v-navigation-drawer>
        <v-content class="fill-height">
            <v-card width="100%" height="25%" color="red" class="rounded-0">
            </v-card>
            <v-card width="100%" height="75%" color="blue" class="rounded-0">
            </v-card>
        </v-content>
    </v-container>
</template>
<script>
import firebaseApp from '@/plugins/firebase'

export default {
    data() {
        return {
            drawer: null,
            items: [
                // {
                //     icon: 'mdi-wifi',
                //     text: 'Wifi',
                // },
            ],
        }

    },
    mounted() {
        //   this.createConnection()
        // this.doSubscribe()
        //   this.interval = setInterval(() => this.Checkonline(), 3000);
        //   this.isOpened = this.isMenuOpen
        //   Janus.init({
        //     debug: true,
        //     dependencies: Janus.useDefaultDependencies(),
        //     callback: () => {
        //       console.log("Connecting to Janus api with server ", JANUS_URL)
        //       this.connect(JANUS_URL)
        //     }
        //   })
        this.dbRef.on('value', ss => {
            // console.log(ss.val());
            this.items = []
            // this.items.remove()
            for (const [key, value] of Object.entries(ss.val())) {
                console.log(`${key}: ${value}`);
                // console.log(`${key}`);
                this.items.push({
                    text: key,
                    // icon: require('../assets/img/class_front.png'),
                    icon: 'toys',
                });
            }
        })
    },
    created() {
        console.log("created()");
        // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
        this.dbRef = firebaseApp.database().ref('/')
        // this.dbStatus = firebaseApp.database().ref('/Rover1/status')
        // this.dbRef1 = firebaseApp.database().ref('Rover1/location/user')
    },
    beforeDestroy() {
        console.log("beforeDestroy()");
        // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
        this.dbRef.off()
        this.dbStatus.off()
        // this.dbRef1.off()
    }
}
</script>
<style>
.scrolling {
    overflow-y: auto;
}

.bgg {
    /*background-color: #133cf1;*/
    border: 0.8px solid rgba(0, 0, 0, 0.38);
    border-radius: 4px;
}

.textbg {
    background-color: aqua;
}
</style>