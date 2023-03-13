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
                            <v-list-item v-for="(item, i) in items" :key="i" @click="updateSelected(item)">
                                
                                <v-list-item-icon>
                                    <v-icon v-text="item.icon"></v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title v-text="item.text"></v-list-item-title>
                                </v-list-item-content>
                                <v-list-item-icon>
                                    <!-- <v-icon :color="green">circle</v-icon> -->
                                    <v-icon :color="item.status == 'offline' ? 'red' : 'green'">circle</v-icon>
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
                                    <p class="pl-1 ma-2">{{ namerover }}</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Status.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">{{ StatusRover }}</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Door.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">{{ DoorStatus }}</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Battery.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2">{{ Battery }}</p>
                                </v-col>
                            </v-row>
                            <v-row no-gutters>
                                <v-col>
                                    <p class="pl-1 ml-2 ">Velocity.</p>
                                </v-col>
                                <v-col>
                                    <p class="pl-1 ml-2 text-red">{{ Velocity }}</p>
                                </v-col>
                            </v-row>
                        </div>
                    </v-card>
                </v-card>
                <v-card width="100%" height="50%" color="blue" class="">
                    <p class="pt-4 ml-3">RoverMode</p>
                    <v-card width="90%" height="52%" color="white" class="pa-0 ma-3 mt-n4 scrolling">
                        <v-btn block color="success" variant="outlined" class="pa-0 mb-1" @click="pushtext">
                            Click
                        </v-btn>
                        <v-btn block color="success" @click="printtext">
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
import mqtt from 'mqtt/dist/mqtt'
var dictRover = {};
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
            check: [],
            item: [
                {
                    icon: 'mdi-wifi',
                    text: 'n',
                    status: true,
                },
            ],

            namerover: "N/a",
            StatusRover: "N/a",
            Battery: "N/a",
            Velocity: "N/a",
            DoorStatus: "N/a",
            idcamera: 0,
            countRover: 0,
            connection: {
                protocol: 'ws',
                host: '34.143.225.243',
                // ws: 8083; wss: 8084
                port: 9001,
                endpoint: '/mqtt',
                // for more options, please refer to https://github.com/mqttjs/MQTT.js#mqttclientstreambuilder-options
                clean: true,
                connectTimeout: 30 * 1000, // ms
                reconnectPeriod: 4000, // ms
                clientId:
                    'emqx_vue_' +
                    Math.random()
                        .toString(16)
                        .substring(2, 8),
                // auth
                username: 'test',
                password: 'Test123',
            },
            subscription: {
                qos: 0,
                topic: 'rover1/status',
            },
            receiveNews: '',
            qosList: [0, 1, 2],
            client: {
                connected: false,
            },
            subscribeSuccess: false,
            connecting: false,
            retryTimes: 0,
            refStatus: false,
            refJoystick: false,
            activeauto: false,
        }

    },
    mounted() {
        this.createConnection()
        // this.doSubscribe()
        this.interval = setInterval(() => this.Checkonline(), 3000);
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

                this.countRover++;
                dictRover[key] = this.countRover;
                // console.log(this.countRover)
                // console.log(`${key}`);
                this.items.push({
                    text: key,
                    // icon: require('../assets/img/class_front.png'),
                    icon: 'toys',
                    status:'offline'
                });
                this.subscription = [];
                this.subscription = {
                    qos: 0,
                    topic: key.toLowerCase() + '/status'
                }
                this.doSubscribe();
            }
        })
    },
    methods: {
        updateSelected(text) {
            // this.doUnSubscribe()
            var refStatus = "";
            console.log(text.text)
            this.namerover = text.text
            // StatusRover
            this.StatusRover = this.items[dictRover[text.text]-1].status
            // Firebase
            refStatus = "/" + this.namerover + '/status'
            this.dbStatus = firebaseApp.database().ref(refStatus)
            this.refStatus = true;
            this.dbStatus.on('value', ss => {
                for (const [key, value] of Object.entries(ss.val())) {
                    // console.log(`${key}: ${value}`);
                    if (key == 'Battery') {
                        // console.log(`${key}: ${value}`);
                        this.Battery = value + ' %'
                    }
                    if (key == 'velocity') {
                        // console.log(`${key}: ${value}`);
                        this.Velocity = value + ' m/s'
                    }
                    if (key == 'idcam') {
                        // console.log(`${key}: ${value}`);
                        this.idcamera = value
                        // this.start();
                    }
                    if (key == 'door') {
                        // console.log(`${key}: ${value}`);
                        if (value == true) {
                            this.DoorStatus = "Open"
                        }
                        else {
                            this.DoorStatus = "Close"
                        }
                    }
                }
            }
            )
        },
        pushtext() {
            // item: [
            //     {
            //         icon: 'mdi-wifi',
            //         text: 'n',
            //         status: true,
            //     },
            // ],
            this.$set(this.item[0], 'textx', 'nom');

            // this.item.text['n']="noom"
            // console.log(this.item.text)
        },
        printtext() {
            // console.log(this.item)
            // console.log(this.items)
            console.log(dictRover["Rover1"]-1)
            console.log(this.items[dictRover["Rover1"]-1].status)

        },
        doorS() {
            // this.isActiveDoor = this.isActiveDoor ? false : true;
            this.isActiveDoor = !this.isActiveDoor
            if (this.isActiveDoor) {
                this.dbRefAutoDoor = firebaseApp.database().ref("/" + this.namerover + '/status')
                this.dbRefAutoDoor.update({ door: false });
            }
            else {
                this.dbRefAutoDoor = firebaseApp.database().ref("/" + this.namerover + '/status')
                this.dbRefAutoDoor.update({ door: true });
            }
        },
        Checkonline() {
            // if ((this.timenow() - this.timemqtt) > 0.1) {
            //     // console.log("Offline", (this.timenow() - this.timemqtt) * 60)
            //     this.StatusRover = "offline"
            // }
            for (let i = 0; i < this.countRover; i++) {
                if ((this.timenow() - this.check[i]) > 0.1) {
                    this.$set(this.items[i], 'status', "offline");
                    if (this.namerover != "N/a"){
                        this.StatusRover = this.items[dictRover[this.namerover]-1].status                    
                    }

                    // console.log("offline")
                }
                else if ((this.timenow() - this.check[i]) < 0.1){
                    this.$set(this.items[i], 'status', "online");
                    if (this.namerover != "N/a"){
                        this.StatusRover = this.items[dictRover[this.namerover]-1].status                    
                    }
                    // this.StatusRover = this.items[dictRover[this.namerover]-1].status
                    // console.log("online")
                }
                // console.log(this.namerover)
                // console.log((this.timenow() - this.check[i]))
            }


        },
        timenow() {
            var one_day = 60 * 60 * 24
            const today = new Date();
            // this.timeone=today/one_day
            return today / one_day
            // console.log(this.timeone)
        },
        initData() {
            this.client = {
                connected: false,
            }
            this.retryTimes = 0
            this.connecting = false
            this.subscribeSuccess = false
        },
        handleOnReConnect() {
            this.retryTimes += 1
            if (this.retryTimes > 5) {
                try {
                    this.client.end()
                    this.initData()
                    this.$message.error('Connection maxReconnectTimes limit, stop retry')
                } catch (error) {
                    this.$message.error(error.toString())
                }
            }
        },
        createConnection() {
            try {
                this.connecting = true
                const { protocol, host, port, endpoint, ...options } = this.connection
                const connectUrl = `${protocol}://${host}:${port}${endpoint}`
                this.client = mqtt.connect(connectUrl, options)
                if (this.client.on) {
                    this.client.on('connect', () => {
                        this.connecting = false
                        console.log('Connection succeeded!')
                    })
                    this.client.on('reconnect', this.handleOnReConnect)
                    this.client.on('error', error => {
                        console.log('Connection failed', error)
                    })
                    this.client.on('message', (topic, message) => {
                        this.receiveNews = this.receiveNews.concat(message)
                        // console.log(`Received message ${message} from topic ${topic}`)
                        // console.log(message)
                        
                        // this.text = "OFF"
                        this.timemqtt = this.timenow()
                        // console.log()
                        for (let i = 0; i < this.countRover; i++) {
                            if (topic === 'rover' + (i + 1) + '/status') {
                                this.check[i] = this.timenow()
                            }
                            // console.log('rover'+ (i+1) +'/status')
                        }

                    })
                }
            } catch (error) {
                this.connecting = false
                console.log('mqtt.connect error', error)
            }
        },
        // subscribe topic
        // https://github.com/mqttjs/MQTT.js#mqttclientsubscribetopictopic-arraytopic-object-options-callback
        doSubscribe() {
            const { topic, qos } = this.
                subscription
            // this.client.subscribe(topic, { qos }, (error, res) => {
            this.client.subscribe(topic, { qos }, (error) => {
                if (error) {
                    console.log('Subscribe to topics error', error)
                    return
                }
                this.subscribeSuccess = true
                // console.log('Subscribe to topics res', res)
            })
        },
        // unsubscribe topic
        // https://github.com/mqttjs/MQTT.js#mqttclientunsubscribetopictopic-array-options-callback
        doUnSubscribe() {
            const { topic } = this.subscription
            this.client.unsubscribe(topic, error => {
                if (error) {
                    console.log('Unsubscribe error', error)
                }
            })
        },

    },
    created() {
        // console.log("created()");
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