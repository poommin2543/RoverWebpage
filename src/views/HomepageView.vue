<template>
  <v-container fluid class="fill-height ma-0 pa-0">
    <!-- <v-flex xs12 sm12 md12> -->
    <v-navigation-drawer height="100%" permanent color="black" width="250">
      <!-- <v-icon>home</v-icon> -->
      <v-card width="100%" color="black" class="rounded-0 pa-0">
        <v-row no-gutters>
          <v-card height="25%" class="mt-5 ml-5" color="black">
            <v-avatar color="blue">
              <span class="text-h5">{{ shortuserLast }}</span>
            </v-avatar>
          </v-card>
          <v-card height="40%" class="pa-0 mt-5 ml-3" color="black">
            <p style="color: #fff">{{ username }}</p>
            <p class="mt-n3" style="color: #fff">{{ lastname }}</p>
          </v-card>
          <v-card
            height="40px"
            width="50px"
            class="pa-0 mt-5 ml-3"
            color="black"
          >
            <v-icon dark size="x-large" style="height: 50px" @click="logout">
              login</v-icon
            >
            <!-- <v-icon icon="login" size="x-large">login</v-icon> -->
          </v-card>
        </v-row>
      </v-card>
      <v-card flat width="100%" color="black" class="pa-3 ma-0 rounded-5">
        <v-card width="100%" color="green" class="pa-0 ma-0">
          <!-- <p class="pt-3 ml-3">RoverList</p> -->
          <v-card
            width="100%"
            color="white"
            class="pa-0 mt-0 scrolling rounded-3"
          >
            <v-list>
              <v-list-item-group color="indigo">
                <v-list-item
                  v-for="(item, i) in items"
                  :key="i"
                  @click.prevent="updateSelected(item)"
                >
                  <v-list-item-icon>
                    <!-- <v-icon v-text="item.icon"></v-icon> -->
                    <v-img
                      width="30px"
                      height="20px"
                      :src="require('../assets/img/Rovericon.svg')"
                      cover
                    ></v-img>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title v-text="item.text"></v-list-item-title>
                  </v-list-item-content>
                  <v-list-item-icon>
                    <v-icon :color="item.status == 'offline' ? 'red' : 'green'"
                      >circle</v-icon
                    >
                  </v-list-item-icon>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>
        </v-card>
      </v-card>
      <v-card width="100%" color="black" class="pa-3 ma-0 rounded-5">
        <v-card width="100%" height="98%" color="black" class="rounded-5">
          <p class="pt-1 ml-3" style="color: #fff">Status</p>
          <v-card flat width="100%" color="white" class="mt-n3 pt-n3">
            <v-card
              flat
              width="90%"
              height="90%"
              color="white"
              class="ml-3 pt-4"
            >
              <div width="100%" height="100%" class="bgg">
                <v-card
                  class="pa-0 ml-3 mt-n4 text-center"
                  width="110px"
                  color="white"
                  flat
                >
                  <span class="text-red">Rover Status.</span>
                </v-card>
                <v-row no-gutters class="d-flex justify-center pt-0 pa-0 ma-0">
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      Rover No.
                    </p>
                  </v-col>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      {{ namerover }}
                    </p>
                  </v-col>
                </v-row>
                <v-row no-gutters>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">Status.</p>
                  </v-col>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      {{ StatusRover }}
                    </p>
                  </v-col>
                </v-row>
                <v-row no-gutters>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">Door.</p>
                  </v-col>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      {{ DoorStatus }}
                    </p>
                  </v-col>
                </v-row>
                <v-row no-gutters>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">Battery.</p>
                  </v-col>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      {{ Battery }}
                    </p>
                  </v-col>
                </v-row>
                <v-row no-gutters>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      Velocity.
                    </p>
                  </v-col>
                  <v-col>
                    <p class="d-flex justify-center pt-0 pa-0 ma-0">
                      {{ Velocity }}
                    </p>
                  </v-col>
                </v-row>
              </div>
            </v-card>
          </v-card>
        </v-card>
      </v-card>
      <!-- :outlined="this.isActiveDoor == true ? 'false':'true'" -->
      <v-card width="100%" color="black" class="">
        <p class="pt-4 ml-3" style="color: #fff">RoverMode</p>
        <v-card
          width="90%"
          style="height: 140px"
          color="black"
          class="pa-0 ma-3 mt-n4"
        >
          <v-card
            width="100%"
            color="black"
            class="d-flex justify-center pt-0 pa-0 ma-0"
          >
            <v-btn
              v-if="isActiveOpencontorl"
              width="75%"
              dark
              :color="this.isActiveDoor != true ? 'white' : 'green'"
              :outlined="this.isActiveDoor != true ? true : false"
              class="pt-0 pa-0 mt-2 mb-1"
              @click="clickAuto"
            >
              {{ this.isActiveDoor != true ? "manual" : "auto" }}
            </v-btn>
          </v-card>
          <v-card
            width="100%"
            color="black"
            class="d-flex justify-center pt-0 pa-0 ma-0"
          >
            <v-btn
              v-if="isActiveOpencontorl && isActiveDoor != true"
              width="75%"
              color="white"
              outlined
              @click="clickDoor"
            >
              Door
            </v-btn>
          </v-card>
          <v-card
            width="100%"
            color="black"
            class="d-flex justify-center pt-0 pa-0 ma-0"
          >
            <v-btn
              v-if="isActiveOpencontorl && isActiveDoor != true"
              width="75%"
              :color="this.isActiveJoy == true ? 'red' : 'green'"
              class="pt-0 pa-0 mt-1"
              @click="clickJoy"
            >
              Joy
            </v-btn>
          </v-card>
          <v-card
            width="100%"
            color="black"
            class="d-flex justify-center pt-0 pa-0 ma-0"
          >
            <!-- <p class="pt-4 ml-3" style="color:#fff">{{ isActiveJoy }}</p> -->
            <v-card
              v-if="isActiveJoy"
              width="75%"
              color="red"
              class="d-flex justify-center pt-0 pa-0 ma-0"
            >
              <!-- <v-icon width="10px" v-gamepad:button-a="aaaa"
                                  v-gamepad:button-a.released="aaaa"></v-icon> -->
              <v-icon
                width="10px"
                v-gamepad:button-a="pressedA"
                v-gamepad:button-a.released="releasedA"
              ></v-icon>
              <v-icon
                type="button"
                width="20%"
                v-gamepad:button-x="pressedX"
                v-gamepad:button-x.released="releasedX"
              ></v-icon>
              <v-icon
                type="button"
                width="20%"
                v-gamepad:button-y="pressedY"
                v-gamepad:button-y.released="releasedY"
              ></v-icon>
              <v-icon
                type="button"
                width="20%"
                v-gamepad:button-b="pressedB"
                v-gamepad:button-b.released="releasedB"
              ></v-icon>
              <v-icon
                type="button"
                width="20%"
                v-gamepad:shoulder-left="releasedReset"
                v-gamepad:shoulder-left.released="releasedReset"
                @click="releasedReset"
              ></v-icon>
            </v-card>
          </v-card>
        </v-card>
      </v-card>
      <v-card
        width="100%"
        color="black"
        class="d-flex justify-center align-baseline pt-0 pa-0 ma-0"
      >
        <v-card
          width="70%"
          color="black"
          class="d-flex justify-center pt-0 pa-0 ma-0"
        >
          <v-img
            class="FullPage"
            :src="require('../assets/img/Classlogo.svg')"
            cover
            @click="reloadPage"
          ></v-img>
        </v-card>
      </v-card>
      <v-card
        width="100%"
        color="black"
        class="d-flex justify-center align-baseline pt-0 pa-0 ma-0"
      >
        <v-card width="100%" color="black" class="text-center mt-3">
          <p style="color: #fff">v0.01</p>
        </v-card>
      </v-card>
    </v-navigation-drawer>
    <!-- </v-flex> -->
    <v-content class="fill-height" height="100%" width="100%">
      <v-card
        v-if="mapState == true"
        width="100%"
        flat
        height="100%"
        color="red"
        class="rounded-0"
      >
        <v-card
          width="100%"
          flat
          height="25%"
          color="black"
          class="rounded-0 d-flex justify-center"
        >
          <v-flex xs12 sm12 md12>
            <!-- <v-card 
          flat
          width="100%"
          height="100%"
        > -->
            <v-img cover>
              <video
                v-if="status == 'started'"
                autoplay="autoplay"
                :srcObject.prop="stream"
                ref="videoStream"
                playsinline
                width="100%"
                height="100%"
              ></video>
            </v-img>
            <!-- </v-card> -->
          </v-flex>
        </v-card>
        <v-card width="100%" flat height="75%" color="black" class="rounded-0">
          <Map :propNameRover="namerover"></Map>
        </v-card>
      </v-card>
      <v-card
        v-if="mapState == false"
        width="100%"
        flat
        height="100%"
        color="red"
        class="rounded-0"
      >
        <v-card width="100%" flat height="100%" color="black" class="rounded-0">
          <MapAll :propC="namerover"> </MapAll>
        </v-card>
      </v-card>
    </v-content>
  </v-container>
</template>
<script>
import Map from "@/components/Map.vue";
import MapAll from "@/components/MapAllRover.vue";
import firebaseApp from "@/plugins/firebase";
import mqtt from "mqtt/dist/mqtt";
import { Janus } from "janus-gateway";
const db = firebaseApp.firestore();
// let JANUS_URL = 'https://34.143.225.243:8089/janus'
let JANUS_URL = "https://janus.roverautonomous.com/janus";
console.log(JANUS_URL);
if (window.location.protocol === "http:") {
  // console.log(JANUS_URL)
  // JANUS_URL = 'http://103.82.249.178:8088/janus'
  JANUS_URL = "https://janus.roverautonomous.com/janus";
  console.log(JANUS_URL);
}
var dictRover = {};
export default {
  beforeCreate() {
    firebaseApp.auth().onAuthStateChanged((user) => {
      if (!user) {
        this.$router.push("/");
        // alert("You don't have a permission");
      }
    });
  },
  components: {
    Map,
    MapAll,
    // Stream
  },

  data() {
    return {
      drawer: null,
      username: "Admin",
      lastname: "Rover",
      shortuserLast: "AR",
      items: [
        // {
        //     icon: 'mdi-wifi',
        //     text: 'Wifi',
        // },
      ],
      check: [],
      item: [
        {
          icon: "mdi-wifi",
          text: "n",
          status: true,
        },
      ],
      isActiveJoy: false,
      isActiveDoor: false,
      isOpenDoor: null,
      isActiveOpencontorl: false,
      StatusDoor: false,
      namerover: "N/a",
      StatusRover: "N/a",
      Battery: "N/a",
      Velocity: "N/a",
      DoorStatus: "N/a",
      idcamera: 0,
      Hisidcamera: 0,
      countRover: 0,
      mapState: false,
      connection: {
        protocol: "wss",
        // protocol: "ws",
        host: "mqtt.roverautonomous.com",
        // host: "103.82.249.178",
        // ws: 8083; wss: 8084
        port: 0,
        // port: 9001,
        endpoint: "/mqtt",
        // for more options, please refer to https://github.com/mqttjs/MQTT.js#mqttclientstreambuilder-options
        clean: true,
        connectTimeout: 30 * 1000, // ms
        reconnectPeriod: 4000, // ms
        clientId: "emqx_vue_" + Math.random().toString(16).substring(2, 8),
        // auth
        username: "rover",
        password: "Rover123",
      },
      subscription: {
        qos: 0,
        topic: "rover1/status",
      },
      receiveNews: "",
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
        options: [],
      },
      remoteTracks: {},
      remoteVideos: 0,
      // Joy,
      textA: "A",
      textB: "B",
      textX: "X",
      textY: "Y",
      textLB: "Reset",
    };
  },
  mounted() {
    console.log("*******************************************");
    // console.log((localStorage.getItem("mail")))
    this.createConnection();
    // var ststusdb = true;
    // this.doSubscribe()
    this.interval = setInterval(() => this.Checkonline(), 3000);
    //   this.isOpened = this.isMenuOpen

    Janus;
    Janus.init({
      debug: true,
      dependencies: Janus.useDefaultDependencies(),
      callback: () => {
        // console.log("Connecting to Janus api with server ", JANUS_URL);
        this.connect(JANUS_URL);
      },
    });

    // this.dbRef = firebaseApp.database().ref('/')
    db.collection("user")
      .get()
      .then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
          // console.log(doc.id, " => ", doc.data());
          // employeesData.push({
          //   id: doc.id,
          //   name: doc.data().name,
          //   date: doc.data().date
          // });
          // console.log(doc.id, " => ", doc.data());

          if (doc.id == localStorage.getItem("mail")) {
            this.username = doc.data().name;
            this.lastname = doc.data().lastname;
            // console.log(doc.data().name);
            // console.log(doc.data().lastname);
            this.shortuserLast =
              this.username.charAt(0) + this.lastname.charAt(0);
          }
        });
        // this.employeesData = employeesData; // Update the component data property
      })
      .catch((error) => {
        console.log("Error getting documents: ", error);
      });
    this.dbRef.on("value", (ss) => {
      // console.log(ss.val());
      this.items = [];
      // this.items.remove()
      for (const [key] of Object.entries(ss.val())) {
        // console.log(`${key}: ${value}`);

        this.countRover++;
        dictRover[key] = this.countRover;
        // console.log(this.countRover)
        // console.log(`${key}`);
        this.items.push({
          text: key,
          // icon: require('../assets/img/class_front.png'),
          icon: "toys",
          status: "offline",
        });
        if (key == "nnn") {
          // console.log("+++++++++done++++++++++++++");
          this.dbRef.off();
          // console.log("+++++++++done++++++++++++++");
        }
        this.subscription = [];
        this.subscription = {
          qos: 0,
          topic: key.toLowerCase() + "/status",
        };
        this.doSubscribe();
      }
    });
    // this.dbRef.off()
    // setTimeout(function () {
    //     console.log("done++++++++++++++")
    //     if (ststusdb == true){

    //         this.dbRef.off()
    //     }
    //     console.log("done++++++++++++++")
    // }, 3000);
  },
  methods: {
    logout() {
      firebaseApp
        .auth()
        .signOut()
        .then(() => {
          alert("Successfully logged out");
          this.$router.push("/");
        })
        .catch((error) => {
          alert(error.message);
          this.$router.push("/");
        });
    },
    reloadPage() {
      this.mapState = false;
      // window.location.reload();
    },
    clickAuto() {
      this.dbRefJoystick = firebaseApp
        .database()
        .ref("/" + this.namerover + "/control");
      this.releasedReset();
      //SetJoy Off
      this.isActiveDoor = !this.isActiveDoor;
      this.isActiveJoy = false;
      this.dbRefAutoBtn = firebaseApp
        .database()
        .ref("/" + this.namerover + "/status");
      if (this.isActiveDoor) {
        this.dbRefAutoBtn.update({ auto: true });
        // this.dbRefAutoDoor.off()
      } else {
        // this.dbRefAutoDoor = firebaseApp.database().ref("/" + this.namerover + '/status')
        this.dbRefAutoBtn.update({ auto: false });
        // this.dbRefAutoDoor.off()
      }
    },
    clickDoor() {
      this.StatusDoor = true;
      // this.isActiveDoor = this.isActiveDoor ? false : true;
      this.isOpenDoor = !this.isOpenDoor;
      this.dbRefAutoDoor = firebaseApp
        .database()
        .ref("/" + this.namerover + "/status");
      if (this.isOpenDoor) {
        this.dbRefAutoDoor.update({ door: true });
      } else {
        this.dbRefAutoDoor.update({ door: false });
      }
    },
    clickJoy() {
      //ActiveJoy
      this.dbRefJoystick = firebaseApp
        .database()
        .ref("/" + this.namerover + "/control");
      this.releasedReset();
      this.isActiveJoy = !this.isActiveJoy;
      if (this.isActiveJoy === true) {
        // console.log("/" + this.namerover + '/control')
        this.dbRefJoystick = firebaseApp
          .database()
          .ref("/" + this.namerover + "/control");
        this.refJoystick == true;
      }
    },
    updateSelected(text) {
      // this.dbRef.off()
      //open Map and VideO

      //SetJoy Off
      this.ActiveJoy = false;
      // this.doUnSubscribe()
      //check DbStatusDoor
      if (this.StatusDoor == true) {
        this.dbRefAutoDoor.off();
      }
      //CheckSteamVideo
      if (this.status == "started") {
        this.stop();
      }

      //Click button open
      this.isActiveOpencontorl = true;
      this.isActiveDoor = false;
      var refStatus = "";
      if (this.refStatus === true) {
        this.dbStatus.off();
      }
      // console.log(text.text);
      this.namerover = text.text;
      // localStorage.setItem(this.namerover)
      localStorage.setItem("Name-rover", this.namerover);
      this.mapState = true;
      //SetAuto is True
      // this.dbRefAutoBtn = firebaseApp.database().ref("/" + this.namerover + '/status')
      // this.dbRefAutoBtn.update({ auto: true });
      // StatusRover
      this.StatusRover = this.items[dictRover[text.text] - 1].status;
      // Firebase
      refStatus = "/" + this.namerover + "/status";
      this.dbStatus = firebaseApp.database().ref(refStatus);
      this.refStatus = true;
      this.dbStatus.on("value", (ss) => {
        for (const [key, value] of Object.entries(ss.val())) {
          // console.log(`${key}: ${value}`);
          if (key == "Battery") {
            // console.log(`${key}: ${value}`);
            this.Battery = value + " %";
          }
          if (key == "velocity") {
            // console.log(`${key}: ${value}`);
            this.Velocity = value + " m/s";
          }
          if (key == "idcam") {
            // console.log(`${key}: ${value}`);
            this.idcamera = value;
            if (this.Hisidcamera != this.idcamera) {
              this.start();
              this.Hisidcamera = this.idcamera;
            }
          }
          if (key == "door") {
            // console.log(`${key}: ${value}`);
            if (value == true) {
              this.DoorStatus = "Open";
              this.isOpenDoor = true;
            } else {
              this.DoorStatus = "Close";
              this.isOpenDoor = false;
            }
          }
          if (key == "auto") {
            // console.log(`${key}: ${value}`);
            if (value == true) {
              this.isActiveDoor = true;
            } else {
              this.isActiveDoor = false;
            }
          }
        }
      });
    },
    Checkonline() {
      // if ((this.timenow() - this.timemqtt) > 0.1) {
      //     // console.log("Offline", (this.timenow() - this.timemqtt) * 60)
      //     this.StatusRover = "offline"
      // }
      for (let i = 0; i < this.countRover; i++) {
        if (this.timenow() - this.check[i] > 0.1) {
          this.$set(this.items[i], "status", "offline");
          if (this.namerover != "N/a") {
            this.StatusRover = this.items[dictRover[this.namerover] - 1].status;
          }

          // console.log("offline")
        } else if (this.timenow() - this.check[i] < 0.1) {
          this.$set(this.items[i], "status", "online");
          if (this.namerover != "N/a") {
            this.StatusRover = this.items[dictRover[this.namerover] - 1].status;
          }
          // this.StatusRover = this.items[dictRover[this.namerover]-1].status
          // console.log("online")
        }
        // console.log(this.namerover)
        // console.log((this.timenow() - this.check[i]))
      }
    },
    timenow() {
      var one_day = 60 * 60 * 24;
      const today = new Date();
      // this.timeone=today/one_day
      return today / one_day;
      // console.log(this.timeone)
    },
    initData() {
      this.client = {
        connected: false,
      };
      this.retryTimes = 0;
      this.connecting = false;
      this.subscribeSuccess = false;
    },
    handleOnReConnect() {
      this.retryTimes += 1;
      if (this.retryTimes > 5) {
        try {
          this.client.end();
          this.initData();
          this.$message.error("Connection maxReconnectTimes limit, stop retry");
        } catch (error) {
          this.$message.error(error.toString());
        }
      }
    },
    createConnection() {
      try {
        this.connecting = true;
        const { protocol, host, port, endpoint, ...options } = this.connection;
        const connectUrl = `${protocol}://${host}:${port}${endpoint}`;
        this.client = mqtt.connect(connectUrl, options);
        if (this.client.on) {
          this.client.on("connect", () => {
            this.connecting = false;
            // console.log('Connection succeeded!')
          });
          this.client.on("reconnect", this.handleOnReConnect);
          this.client.on("error", (error) => {
            console.log("Connection failed", error);
          });
          this.client.on("message", (topic, message) => {
            this.receiveNews = this.receiveNews.concat(message);
            // console.log(`Received message ${message} from topic ${topic}`)
            // console.log(message)

            // this.text = "OFF"
            this.timemqtt = this.timenow();
            // console.log()
            for (let i = 0; i < this.countRover; i++) {
              if (topic === "rover" + (i + 1) + "/status") {
                this.check[i] = this.timenow();
              }
              // console.log('rover'+ (i+1) +'/status')
            }
          });
        }
      } catch (error) {
        this.connecting = false;
        console.log("mqtt.connect error", error);
      }
    },
    // subscribe topic
    // https://github.com/mqttjs/MQTT.js#mqttclientsubscribetopictopic-arraytopic-object-options-callback
    doSubscribe() {
      const { topic, qos } = this.subscription;
      this.client.subscribe(topic, { qos }, (error, res) => {
        // this.client.subscribe(topic, { qos }, (error) => {
        if (error) {
          console.log("Subscribe to topics error", error, res);
          return;
        }
        this.subscribeSuccess = true;
        // console.log("Subscribe to topics res", res);
      });
    },
    // unsubscribe topic
    // https://github.com/mqttjs/MQTT.js#mqttclientunsubscribetopictopic-array-options-callback
    doUnSubscribe() {
      const { topic } = this.subscription;
      this.client.unsubscribe(topic, (error) => {
        if (error) {
          console.log("Unsubscribe error", error);
        }
      });
    },
    //Stream
    connect(server) {
      this.janus = new Janus({
        server,
        // Call success callback
        success: () => {
          console.log("Connected Janus");
          this.attachPlugin();
        },
        // Call error callback
        error: (error) => {
          console.log("Error");
          this.onError("Failed to connect janus server", error);
        },
        // Call destroyed callback
        destroyed: () => {
          console.log("Destroyed");
          window.location.reload();
        },
      });
    },
    attachPlugin() {
      this.janus.attach({
        plugin: "janus.plugin.streaming",
        opaqueId: "thisisopaqueid",
        success: (pluginHandle) => {
          this.plugin = pluginHandle;
          console.log("getBitrate : ", this.plugin.getBitrate());
          // this.updateStreamsList()
        },
        error: (error) => {
          this.onError("Error attaching plugin... ", error);
        },
        iceState: (state) => {
          console.log("ICE state changed to ", state);
        },
        webrtcState: (on) => {
          console.log(
            "Janus says our WebRTC PeerConnection is " +
              (on ? "up" : "down") +
              " now"
          );
        },
        slowLink: (uplink, lost, mid) => {
          console.log(
            "Janus reports problems " +
              (uplink ? "sending" : "receiving") +
              " packets on mid " +
              mid +
              " (" +
              lost +
              " lost packets)"
          );
        },
        onmessage: (msg, jsep) => {
          // Receive status of plugin streaming
          // console.log(" ::: Got a message :::", msg);
          let result = msg.result;
          if (result) {
            if (result.status) {
              this.status = result.status;
            }
          }
          // Handle msg error status
          else if (msg.error) {
            this.onError(msg.error);
            this.stop();
            return;
          }
          if (jsep) {
            Janus.debug("Handling SDP as Well... ", jsep);
            let stereo = jsep.sdp.indexOf("stereo=1") !== -1;
            this.plugin.createAnswer({
              jsep: jsep,
              media: {
                audioSend: false,
                videoSend: false,
                data: true,
              },
              customizeSdp: (jsep) => {
                if (stereo && jsep.sdp.indexOf("stereo=1") == -1) {
                  jsep.sdp = jsep.sdp.replace(
                    "useinbandfec=1",
                    "useinbandfec=1;stereo=1"
                  );
                }
              },
              success: (jsep) => {
                Janus.debug("Got SDP!", jsep);
                let body = { request: "start" };
                this.plugin.send({
                  message: body,
                  jsep: jsep,
                });
              },
              error: (error) => {
                this.onError("WebRTC Error: ", error);
                alert("WebRTC error... ", error);
              },
            });
          }
        },
        onremotetrack: (track, mid, on) => {
          Janus.debug(
            "Remote track (mid=" +
              mid +
              ") " +
              (on ? "added" : "removed") +
              ":",
            track
          );
          // New track was added
          if (track.kind === "video") {
            this.remoteVideos++;
            this.stream = new MediaStream();
            this.stream.addTrack(track.clone());
            this.remoteTracks.mid = this.stream;
            Janus.log("Created remote audio stream:", this.stream);
          }
        },
        oncleanup: () => {
          this.onCleanup();
        },
      });
    },
    updateStreamsList() {
      this.plugin.send({
        message: { request: "list" },
        success: (result) => {
          if (!result) {
            this.onError("Got no response to our query for available streams.");
          }
          // console.log("Updating StreamList....", result)
          this.streamList.options = result.list;
          if (result.list.length) {
            this.streamList.selected = this.streamList.options[0].id;
          }
        },
      });
    },
    start() {
      // this.plugin.send({ message: { request: "watch", id: this.streamList.selected } })
      this.plugin.send({ message: { request: "watch", id: this.idcamera } });
    },
    stop() {
      this.plugin.send({ message: { request: "stop" } });
      this.plugin.hangup();
    },
    // Reset data.params to null
    onCleanup() {
      Janus.log(" ::: Got a cleanup notification :::");
      this.stream = null;
      this.status = null;
      this.remoteTracks = {};
      this.remoteVideos = 0;
      this.error = null;
    },
    // Handle on error event occur
    onError(message, error = "") {
      Janus.error(message, error);
      this.error = message + error;
      alert(this.error, function () {
        window.location.reload();
      });
    },
    //Joy
    pressedA(e) {
      this.textA = "Click";
      console.log(`pressA`, e);
      this.dbRefJoystick.set({
        forword: 0,
        backword: 1,
        right: 0,
        left: 0,
      });
    },
    releasedA() {
      this.textA = "A";
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0,
      });
    },
    pressedX(e) {
      this.textX = "Click";
      console.log(`pressX`, e);
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 1,
      });
    },
    releasedX() {
      this.textX = "X";
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0,
      });
    },
    pressedY(e) {
      this.textY = "Click";
      console.log(`pressY`, e);
      this.dbRefJoystick.set({
        forword: 1,
        backword: 0,
        right: 0,
        left: 0,
      });
    },
    releasedY() {
      this.textY = "Y";
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0,
      });
    },
    pressedB(e) {
      this.textB = "Click";
      console.log(`pressB`, e);
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 1,
        left: 0,
      });
    },
    releasedB() {
      this.textB = "B";
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0,
      });
    },
    // pressedReset(e) {
    //   this.textLB = "Click";
    //   console.log(`pressLB`, e);
    //   this.dbRefJoystick.set({
    //     forword: 0,
    //     backword: 0,
    //     right: 0,
    //     left: 0,
    //   });
    // },
    releasedReset() {
      this.dbRefJoystick = firebaseApp
        .database()
        .ref("/" + this.namerover + "/control");
      this.textLB = "Reset";
      this.dbRefJoystick.set({
        forword: 0,
        backword: 0,
        right: 0,
        left: 0,
      });
    },
  },
  created() {
    // console.log("created()");
    // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
    this.dbRef = firebaseApp.database().ref("/");
    // this.dbStatus = firebaseApp.database().ref('/Rover1/status')
    // this.dbRef1 = firebaseApp.database().ref('Rover1/location/user')
    // window.addEventListener('beforeunload', this.logout);
    // window.addEventListener('beforeunload', this.releasedReset);
  },
  beforeDestroy() {
    // console.log("beforeDestroy()");
    // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
    this.dbRefJoystick = firebaseApp
      .database()
      .ref("/" + this.namerover + "/control");
    // window.removeEventListener('beforeunload', this.logout);
    window.removeEventListener("beforeunload", this.releasedReset);
    // window.removeEventListener('beforeunload', this.$router.push("/login"));
    // this.releasedReset
    this.dbRef.off();
    this.dbStatus.off();
    // this.dbRef1.off()
    this.logout;
  },
  detectTabClose() {
    this.$router.push("/login");
  },
};
</script>
<style>
.scrolling {
  overflow-y: auto;
  height: 220px;
}

.bgg {
  /*background-color: #133cf1;*/
  border: 0.8px solid rgba(0, 0, 0, 0.38);
  border-radius: 4px;
}

.FullPage {
  height: 70%;
  width: 70%;
}
</style>
