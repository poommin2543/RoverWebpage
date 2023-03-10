<template>
    <div class="container-max-widths text-center grid-logo">
      <div class="row grid-color-black">
        <div class="col-xl-2 h-100">
          <div class="row grid-color-black  ">
            <div class="col-xl-12  ">
  
              <br><a>Admin</a>
            </div>
          </div>
          <div class="row grid-color-black  ">
            <div class="col-xl-12" id="cardroverList">
              <!-- <div class="cardframe blackcardframe"> -->
              <div class="card text-center">
                <!-- <p class="titleheader"> Rover list</p> -->
                <v-list>
                  <div class="centerList">
                    <v-list-item-group v-model="selectedItem" color="primary">
                      <v-list-item v-for="(item, i) in items" :key="i" @click="updateSelected(item)">
                        <v-list-item-content>
                          <!-- <p>{{ item.Name }}</p> -->
                          <button type="button" class="btn btn-light btn-block">{{ item.Name }}</button>
                          <!-- <button type="button" class="list-group-item list-group-item-action">{{ item.Name }}</button> -->
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </div>
                </v-list>
  
              </div>
            </div>
          </div>
          <!-- <div class="row grid-color-black ">
            <div class="col-xl-12">
              <p>Noom</p>
            </div>
          </div> -->
          <div></div>
          <div class="row grid-color-black ">
            <div class="col-xl-12" id = "cardStatus">
              <!-- <div class="cardframe blackcardframe"> -->
              <div class="cardRoverlist">
                <!-- <p class="titleheader"> Rover list</p> -->
                <!-- <p>Rover status</p> -->
                <!-- <div class=" Trancardframe text-center"> -->
                  <div class="row">
                    <div class="col-6">
                      <p class="text-right">Rover :</p>
                    </div>                 
                    <div class="col-6">
                      <p class="text-left">{{ namerover }}</p>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-6">
                      <p class="text-right">Status :</p>
                    </div>                 
                    <div class="col-6">
                      <p class="text-left">
                        <span v-if="StatusRover == 'offline'" class="badge badge-danger">{{ StatusRover }}</span>
                        <span v-if="StatusRover == 'on'" class="badge badge-success">{{ StatusRover }}</span>
                      </p>
                    </div>
                  </div>
                  
                  <div class="row">
                    <div class="col-6">
                      <p class="text-right">Door:</p>
                    </div>                 
                    <div class="col-6">
                      <p class="text-left">{{ DoorStatus }}</p>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-6">
                      <p class="text-right">Battery :</p>
                    </div>                 
                    <div class="col-6">
                      <p class="text-left">{{ Battery }}</p>
                    </div>
                  </div>
                  
                  <div class="row">
                    <div class="col-6">
                      <p class="text-right">Velocity:</p>
                    </div>                 
                    <div class="col-6">
                      <p class="text-left">{{ Velocity }}</p>
                    </div>
                  </div>
                  
  
  
                <!-- <div class="Rover_List Contact_Text">
                  <div class="Frame_857 autoFrame_857">
                    <div class="Asset_1_2">
                      <div class="Rover_Class_final_front_1">
                        <p>noomza</p>
                      </div>
                    </div>
                  </div>
                </div> -->
  
              </div>
            </div>
          </div>
          <div class="row grid-color-black ">
            <!-- <div v-if="isActiveOpencontorl" col-xl-12> -->
            <div class="col-xl-12">
  
              <!-- <div v-if="isActive === true">
                  <button type="button"  :class="isActive ? 'buttonclose-33' : 'button-33'"
                  @click="isActive = !isActive">Auto</button>
              </div> -->
              <!-- <button v-if="activeauto" class="ui button big" :class="[isActive ? 'buttonclose-33' : 'button-33']"
                @click="toggle()">
                {{ isActive ? 'Manual' : 'Auto' }}</button> -->
              <!-- <div v-if="isActiveOpencontorl === true">
                <button type="button" :class="isActive ? 'button-33' : 'buttonclose-33'" @click="toggle()">{{
                  isActive ? 'ON' : 'OFF' }}</button>
                </div> -->
                <div id="button-Auto-layout">
                  <button v-if="activeauto" type="button" class="btn btn-primary btn-lg btn-block" @click="toggle()">{{ isActive
                    ? 'Manual' : 'Auto' }}</button>
                <button v-if="isActive" type="button" class="btn btn-secondary btn-lg btn-block"
                  @click="doorS()">Opendoor</button>
                <button v-if="isActive" type="button" class="btn btn-secondary btn-lg btn-block"
                  @click="joystick()">Joy</button>
                <div v-if="isActiveJoy && isActive">
                  <button type="button" v-gamepad:button-a="pressedA" v-gamepad:button-a.released="releasedA"></button>
                  <button type="button" v-gamepad:button-x="pressedX" v-gamepad:button-x.released="releasedX"></button>
                  <button type="button" v-gamepad:button-y="pressedY" v-gamepad:button-y.released="releasedY"></button>
                  <button type="button" v-gamepad:button-b="pressedB" v-gamepad:button-b.released="releasedB"></button>
                  <button type="button" v-gamepad:shoulder-left="pressedReset"
                    v-gamepad:shoulder-left.released="releasedReset" v-on:click="pressedReset"></button>
                </div>
                </div>
            </div>
          </div>
          <div class="row grid-color-black ">
            <div class="col-xl-12">
              <div class="cardframelogo Trancardframe">
                <img src="../assets/img/class logo.png" class="img-fluid" alt="Responsive image">
  
              </div>
            </div>
          </div>
  
  
        </div>
        <div class="col-xl-10">
          <div class="col-xl-12  grid-color-black">
            <div class="row">
  
              <div class="col-xl-12 ">
                <h3 v-if="status == 'starting'"> Loading video stream ... </h3>
                <div class="video-vtn img-fluid " alt="Responsive image">
                  <!-- <h3>{{ status }}</h3> -->
                  <div v-if="status == 'started'" id='card-img-top'>
                    <div class="card-body">
                      <img v-if="status == 'started'" src="../assets/img/template.png" class="img-fluid" alt="Responsive image">
                      <!-- <video v-if="status == 'started'" autoplay="autoplay" :srcObject.prop="stream" ref="videoStream"
                        playsinline width="1280px" height="240px"></video> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-12 card-Footer grid-color-black grid-scall">
            <!-- <Map></Map> -->
          </div>
        </div>
      </div>
  
    </div>
  </template>
  
  <script>
//   import Map from "@/components/Map.vue"
  // import Stream from "@/components/Muticamera.vue"
  import firebaseApp from '@/plugins/firebase'
  import mqtt from 'mqtt/dist/mqtt'
  import { Janus } from 'janus-gateway'
//   let JANUS_URL = 'https://34.143.225.243:8089/janus'
  let PicVdotest = require('../assets/img/class_front.png')
  if (window.location.protocol === 'http:') {
    // console.log(JANUS_URL)
    // JANUS_URL = 'http://103.82.249.178:8088/janus'
    // console.log(JANUS_URL)
  }
  export default {
    components: {
    //   Map,
      // Stream
    },
    data() {
      return {
        PicVdotest,
        isOpened: true,
        isActive: false,
        isActiveJoy: false,
        isActiveDoor: false,
        isActiveOpencontorl: false,
        rover: "",
        selectedItem: 1,
        items: [
          // { text: 'Real-Time', icon: 'mdi-clock' },
          // { text: 'Audience', icon: 'mdi-account' },
          // { text: 'Conversions', icon: 'mdi-flag' },
        ],
        itemrover: {},
        namerover: "N/a",
        StatusRover: "N/a",
        Battery: "N/a",
        Velocity: "N/a",
        DoorStatus: "N/a",
        timeone: 0,
        timemqtt: 0,
        idcamera: 0,
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
        publish: {
          topic: 'rover1/status',
          qos: 0,
          payload: 'Hi',
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
        // Joy,
        textA: "A",
        textB: "B",
        textX: "X",
        textY: "Y",
        textLB: "Reset",
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
        for (const [key,value] of Object.entries(ss.val())) {
          console.log(`${key}: ${value}`);
          // console.log(`${key}`);
          this.items.push({
            Name: key,
          });
        }
      })
    },
    methods: {
      toggle() {
        this.isActive = this.isActive ? false : true;
        if (this.isActive) {
          this.dbRefAutoContorl = firebaseApp.database().ref("/" + this.namerover + '/status')
          this.dbRefAutoContorl.update({ auto: false });
        }
        else {
          this.dbRefAutoContorl = firebaseApp.database().ref("/" + this.namerover + '/status')
          this.dbRefAutoContorl.update({ auto: true });
        }
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
      updateSelected(totoal) {
        console.log(totoal)
        this.doUnSubscribe()
        this.activeauto = true
        this.isActiveJoy = false
        this.isActive = false
        this.isActiveOpencontorl = true
        if (this.status == 'started') {
          this.stop()
        }
        if (this.refStatus == true) {
          this.dbStatus.off()
          this.refStatus = false;
        }
        if (this.refJoystick == true) {
          this.dbRefJoystick.off()
          this.dbRefAutoContorl.off()
          this.refJoystick = false;
        }
        var refStatus = "";
        // this.yourFunction()
        for (const [key, value] of Object.entries(totoal)) {
          if (key === 'Name') {
            // var decodedStringBtoA = value;grid-scall
            // Encode the String
            var encodedStringBtoA = btoa(value);
            localStorage.setItem("name-Rover", encodedStringBtoA);
            this.StatusRover = "offline"
            this.namerover = value;
            this.subscription = [];
            // this.subscription.push({
            //     // topic: value.toLowerCase() + '/status',
            //     topic:  '/status',
            //     qos: 0,
            // })
            this.subscription = {
              qos: 0,
              topic: value.toLowerCase() + '/status'
            }
            this.doSubscribe();
            refStatus = "/" + value + '/status'
            this.dbStatus = firebaseApp.database().ref(refStatus)
            // refStatus = "/" + value + '/status/auto'
            // this.dbStatus = firebaseApp.database().ref(refStatus)
            this.refStatus = true;
            this.dbStatus.on('value', ss => {
              for (const [key, value] of Object.entries(ss.val())) {
                console.log(`${key}: ${value}`);
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
            })
          }
          // if (this.subscribeSuccess === false) {
          //     this.doSubscribe();
          //     console.log(this.subscribeSuccess)
          // }
          // else {
          //     this.doUnSubscribe();
          //     console.log(this.subscribeSuccess)
          // }
        }
      },
      Checkonline() {
        if ((this.timenow() - this.timemqtt) > 0.1) {
          // console.log("Offline", (this.timenow() - this.timemqtt) * 60)
          this.StatusRover = "offline"
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
              console.log(`Received message ${message} from topic ${topic}`)
              // console.log(message)
              this.StatusRover = message
              // this.text = "OFF"
              this.timemqtt = this.timenow()
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
        this.client.subscribe(topic, { qos }, (error, res) => {
          if (error) {
            console.log('Subscribe to topics error', error)
            return
          }
          this.subscribeSuccess = true
          console.log('Subscribe to topics res', res)
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
      joystick() {
        this.isActiveJoy = !this.isActiveJoy
        if (this.isActiveJoy == true) {
          console.log("/" + this.namerover + '/control')
          // this.dbRefAutoContorl = firebaseApp.database().ref("/" + this.namerover + '/auto')
          this.dbRefJoystick = firebaseApp.database().ref("/" + this.namerover + '/control')
          this.refJoystick == true
          // this.auto()
        }
      },
      close() {
        this.dbRefAutoContorl.off()
      },
      auto() {
        // this.dbRefJoystick.set({});
        console.log("======================>")
        console.log("/" + this.namerover + '/status')
        this.dbRefAutoContorl = firebaseApp.database().ref("/" + this.namerover + '/status')
        this.dbRefAutoContorl.update({ auto: false });
        // this.dbRefAutoContorl.on('value', ss => {
        //       for (const [key, value] of Object.entries(ss.val())) {
        //         console.log(`${key}: ${value}`);
        //       }
        //     })
      },
      pressedA(e) {
        this.textA = "Click";
        console.log(`pressA`, e);
        this.dbRefJoystick.set({
          forword: 0,
          backword: 1,
          right: 0,
          left: 0
        });
      },
      releasedA() {
        this.textA = "A";
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 0
        });
      },
      pressedX(e) {
        this.textX = "Click";
        console.log(`pressX`, e);
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 1
        });
      },
      releasedX() {
        this.textX = "X";
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 0
        });
      },
      pressedY(e) {
        this.textY = "Click";
        console.log(`pressY`, e);
        this.dbRefJoystick.set({
          forword: 1,
          backword: 0,
          right: 0,
          left: 0
        });
      },
      releasedY() {
        this.textY = "Y";
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 0
        });
      },
      pressedB(e) {
        this.textB = "Click";
        console.log(`pressB`, e);
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 1,
          left: 0
        });
      },
      releasedB() {
        this.textB = "B";
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 0
        });
      },
      pressedReset(e) {
        this.textLB = "Click";
        console.log(`pressLB`, e);
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 0
        });
      },
      releasedReset() {
        this.textLB = "Reset";
        this.dbRefJoystick.set({
          forword: 0,
          backword: 0,
          right: 0,
          left: 0
        });
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
  <style scoped src="@/assets/styles/stylesViewControl.css"></style>