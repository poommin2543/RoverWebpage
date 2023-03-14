<template>
    <v-container fluid class="fill-height ma-0 pa-0">
        <v-navigation-drawer image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg" permanent color="primary"
            width="250">
            <!-- <v-icon>home</v-icon> -->
            <v-card width="100%" height="6%" color="red" class="">
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
            <v-card width="100%" height="25%" color="blue" class="pa-0 ma-0">
                <p class="pt-3 ml-3">RoverList</p>
                <v-card width="90%" height="85%" color="white" class="pa-0 ma-3 mt-n4 scrolling rounded-3">
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
            <v-card width="100%" height="24%" color="red" class="">
                <p class="pt-1 ml-3">Status</p>
                <v-card width="90%" height="86%" color="blue" class="pa-0 ma-3 ">
                    <v-card width="89%" height="93%" color="orange" class="pa-0 ma-3">
                        <p class="pl-8 ma-n3 ">Rover Status.</p>
                        <div width="100%" height="100%" class="bgg">
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

            </v-card>
            <v-card width="100%" height="20%" color="blue" class="">
                <p class="pt-4 ml-3">RoverMode</p>
                <v-card width="90%" height="70%" color="white" class="pa-0 ma-3 mt-n4">
                    <v-card width="100%" height="33%" color="red" class="pb-0 mt-0">
                        <v-btn v-if="isActiveOpencontorl" color="black" outlined class="pl-16 pr-16 ml-6 mt-3"
                            @click="clickAuto">
                            Auto
                        </v-btn>
                    </v-card>
                    <v-card width="100%" height="33%" color="green" class="pt-0 pb-0 mt-0">
                        <v-btn v-if="isActiveOpencontorl && isActiveDoor" color="black" outlined
                            class="pl-16 pr-16 ml-6 mt-0" @click="clickDoor">
                            Door
                        </v-btn>
                    </v-card>
                    <v-card width="100%" height="33%" color="yellow" class=" pt-0 pa-0 ma-0">
                        <v-btn v-if="isActiveOpencontorl && isActiveDoor" color="red" class="pl-16 pr-16 ml-6 mt-n4"
                            @click="clickJoy">
                            Joy
                        </v-btn>
                    </v-card>
                </v-card>
            </v-card>
            <v-card width="100%" height="20%" color="red" class="">
            </v-card>
        </v-navigation-drawer>
        <v-content class="fill-height">
            <v-card width="100%" height="20%" color="black" class="rounded-0 justify-center">
            <v-card-actions width="80%" height="100%" color="while" class="justify-center pl-n5">
                <!-- <img v-if="isActiveOpencontorl && isActiveDoor" src="../assets/img/template.png" class="img-fluid" alt="Responsive image"> -->
                <video v-if="status == 'started'" autoplay="autoplay" :srcObject.prop="stream" ref="videoStream"
                playsinline width="1280px" height="240px"></video>
            </v-card-actions>
                <!-- <h3 v-if="status == 'starting'"> Loading video stream ... </h3> -->
                <!-- <v-img src="../assets/img/template.png" class="img-fluid" alt="Responsive image"> -->
                    <!-- <v-img
                    contain
                    max-height="300"
                    min-height="240"
                    src="../assets/img/template.png"
                  ></v-img> -->
                  <!-- <h3>{{ status }}</h3> -->
                  <!-- <div v-if="status == 'started'" id='card-img-top'>
                    <div class="card-body">
                      <img v-if="status == 'started'" src="../assets/img/template.png" class="img-fluid" alt="Responsive image">
                      <video v-if="status == 'started'" autoplay="autoplay" :srcObject.prop="stream" ref="videoStream"
                        playsinline width="1280px" height="240px"></video>
                    </div>
                  </div> -->
             
            </v-card>
            <v-card width="100%" height="70%" color="blue" class="rounded-0">
                <Map></Map>
            </v-card>
        </v-content>
    </v-container>
</template>
<script>
import Map from "@/components/Map.vue"
import firebaseApp from '@/plugins/firebase'
import mqtt from 'mqtt/dist/mqtt'
import { Janus } from 'janus-gateway'
let JANUS_URL = 'https://34.143.225.243:8089/janus'
if (window.location.protocol === 'http:') {
    // console.log(JANUS_URL)
    JANUS_URL = 'http://103.82.249.178:8088/janus'
    console.log(JANUS_URL)
}
var dictRover = {};
export default {
    components: {
      Map,
      // Stream
    },
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
            isActiveJoy: false,
            isActiveDoor: false,
            isOpenDoor: false,
            isActiveOpencontorl: false,
            StatusDoor: false,
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
            //Stream
            janus: null,
            error: null,
            plugin: null,
            status: null,
            stream: null,
            streamList: {
                selected: null,
                options: []
            },
            remoteTracks: {},
            remoteVideos: 0,
        }

    },
    mounted() {
        this.createConnection()
        // this.doSubscribe()
        this.interval = setInterval(() => this.Checkonline(), 3000);
        //   this.isOpened = this.isMenuOpen
          Janus.init({
            debug: true,
            dependencies: Janus.useDefaultDependencies(),
            callback: () => {
              console.log("Connecting to Janus api with server ", JANUS_URL)
              this.connect(JANUS_URL)
            }
          })
        // this.dbRef = firebaseApp.database().ref('/')
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
                    status: 'offline'
                });
                this.subscription = [];
                this.subscription = {
                    qos: 0,
                    topic: key.toLowerCase() + '/status'
                }
                this.doSubscribe();
            }
        })
        // this.dbRef.off()
    },
    methods: {
        clickAuto() {
            this.isActiveDoor = !this.isActiveDoor
        },
        clickDoor() {
            this.StatusDoor = true
            // this.isActiveDoor = this.isActiveDoor ? false : true; 
            this.isOpenDoor = !this.isOpenDoor
            this.dbRefAutoDoor = firebaseApp.database().ref("/" + this.namerover + '/status')
            if (this.isOpenDoor) {
                this.dbRefAutoDoor.update({ door: false });
            }
            else {
                // this.dbRefAutoDoor = firebaseApp.database().ref("/" + this.namerover + '/status')
                this.dbRefAutoDoor.update({ door: true });
            }
        },
        clickJoy() {
            this.isActiveJoy = !this.isActiveJoy
        },
        updateSelected(text) {
            this.dbRef.off()
            // this.doUnSubscribe()
            //check DbStatusDoor
            if (this.StatusDoor == true) {
                this.dbRefAutoDoor.off()
            }

            //Click button open 
            this.isActiveOpencontorl = true
            this.isActiveDoor = false
            var refStatus = "";
            if (this.refStatus === true) {
                this.dbStatus.off()
            }
            console.log(text.text)
            this.namerover = text.text
            // StatusRover
            this.StatusRover = this.items[dictRover[text.text] - 1].status
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
                        this.start();
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
        Checkonline() {
            // if ((this.timenow() - this.timemqtt) > 0.1) {
            //     // console.log("Offline", (this.timenow() - this.timemqtt) * 60)
            //     this.StatusRover = "offline"
            // }
            for (let i = 0; i < this.countRover; i++) {
                if ((this.timenow() - this.check[i]) > 0.1) {
                    this.$set(this.items[i], 'status', "offline");
                    if (this.namerover != "N/a") {
                        this.StatusRover = this.items[dictRover[this.namerover] - 1].status
                    }

                    // console.log("offline")
                }
                else if ((this.timenow() - this.check[i]) < 0.1) {
                    this.$set(this.items[i], 'status', "online");
                    if (this.namerover != "N/a") {
                        this.StatusRover = this.items[dictRover[this.namerover] - 1].status
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
        //Stream
      connect(server) {
        this.janus = new Janus({
          server,
          // Call success callback
          success: () => {
            console.log("Connected")
            this.attachPlugin()
          },
          // Call error callback 
          error: (error) => {
            console.log("Error")
            this.onError('Failed to connect janus server', error)
          },
          // Call destroyed callback
          destroyed: () => {
            console.log("Destroyed")
            window.location.reload()
          }
        })
      },
      attachPlugin() {
        this.janus.attach({
          plugin: "janus.plugin.streaming",
          opaqueId: 'thisisopaqueid',
          success: (pluginHandle) => {
            this.plugin = pluginHandle
            console.log("getBitrate : ", this.plugin.getBitrate())
            // this.updateStreamsList()
          },
          error: (error) => {
            this.onError('Error attaching plugin... ', error)
          },
          iceState: (state) => {
            console.log("ICE state changed to ", state)
          },
          webrtcState: (on) => {
            console.log("Janus says our WebRTC PeerConnection is " + (on ? "up" : "down") + " now")
          },
          slowLink: (uplink, lost, mid) => {
            console.log("Janus reports problems " + (uplink ? "sending" : "receiving") +
              " packets on mid " + mid + " (" + lost + " lost packets)")
          },
          onmessage: (msg, jsep) => {
            // Receive status of plugin streaming 
            console.log(" ::: Got a message :::", msg)
            let result = msg.result
            if (result) {
              if (result.status) {
                this.status = result.status
              }
            }
            // Handle msg error status 
            else if (msg.error) {
              this.onError(msg.error)
              this.stop()
              return;
            }
            if (jsep) {
              Janus.debug("Handling SDP as Well... ", jsep)
              let stereo = (jsep.sdp.indexOf("stereo=1") !== -1)
              this.plugin.createAnswer({
                jsep: jsep,
                media: {
                  audioSend: false,
                  videoSend: false,
                  data: true
                },
                customizeSdp: (jsep) => {
                  if (stereo && jsep.sdp.indexOf("stereo=1") == -1) {
                    jsep.sdp = jsep.sdp.replace("useinbandfec=1", "useinbandfec=1;stereo=1")
                  }
                },
                success: (jsep) => {
                  Janus.debug("Got SDP!", jsep)
                  let body = { request: "start" }
                  this.plugin.send({
                    message: body,
                    jsep: jsep
                  })
                },
                error: (error) => {
                  this.onError("WebRTC Error: ", error)
                  alert("WebRTC error... ", error)
                }
              })
            }
          },
          onremotetrack: (track, mid, on) => {
            Janus.debug("Remote track (mid=" + mid + ") " + (on ? "added" : "removed") + ":", track)
            // New track was added 
            if (track.kind === "video") {
              this.remoteVideos++
              this.stream = new MediaStream()
              this.stream.addTrack(track.clone())
              this.remoteTracks.mid = this.stream
              Janus.log("Created remote audio stream:", this.stream)
            }
          },
          oncleanup: () => {
            this.onCleanup()
          }
        })
      },
      updateStreamsList() {
        this.plugin.send({
          message: { request: "list" },
          success: (result) => {
            if (!result) {
              this.onError("Got no response to our query for available streams.")
            }
            console.log("Updating StreamList....", result)
            this.streamList.options = result.list
            if (result.list.length) {
              this.streamList.selected = this.streamList.options[0].id
            }
          }
        })
      },
      start() {
        // this.plugin.send({ message: { request: "watch", id: this.streamList.selected } })
        this.plugin.send({ message: { request: "watch", id: this.idcamera } })
      },
      stop() {
        this.plugin.send({ message: { request: "stop" } })
        this.plugin.hangup()
      },
      // Reset data.params to null 
      onCleanup() {
        Janus.log(" ::: Got a cleanup notification :::");
        this.stream = null
        this.status = null
        this.remoteTracks = {}
        this.remoteVideos = 0
        this.error = null
      },
      // Handle on error event occur
      onError(message, error = '') {
        Janus.error(message, error)
        this.error = message + error
        alert(this.error, function () {
          window.location.reload()
        })
      }


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