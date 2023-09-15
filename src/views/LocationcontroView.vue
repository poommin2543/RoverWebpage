<template>
  <v-app>
    <!-- Use a large card-like container as the background -->
    <v-card color="#e6ccb2" class="background-card">
      <!-- Set a light gray background color -->
      <v-container class="custom-container">
        <v-card
          flat
          class="d-flex flex-column align-center justify-center bottom-space"
          color="transparent"
        >
          <img
            class="responsive-img"
            :src="require('../assets/img/Hot-Cup-Of-Coffee.svg')"
            alt="Coffee Cup"
          />
        </v-card>
        <v-card
          :class="Locations[0].color + ' status-box'"
          flat
          color="#e6ccb2"
        >
          <!-- Replace 'Status goes here' with your dynamic status data -->
          <span>{{ Statustext }}</span>
        </v-card>
        <v-row class="justify-space-around">
          <v-col
            v-for="btn in Locations"
            :key="btn.label"
            cols="12"
            sm="4"
            lg="4"
            xs="12"
          >
            <v-btn
              class="custom-btn"
              :class="btn.label === 'Home' ? 'btn-light-yellow' : 'btn-pastel'"
              block
              outlined
              @click="navigate(btn.route)"
            >
              {{ btn.label === "Home" ? "Home" : btn.label }}
              <!-- Change 'Location' to 'Location' for all Locations -->
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-app>
</template>

<script>
import mqtt from "mqtt/dist/mqtt";
import firebaseApp from "@/plugins/firebase";
export default {
  beforeCreate() {
    firebaseApp.auth().onAuthStateChanged((user) => {
      if (!user) {
        this.$router.push("/");
        // alert("You don't have a permission");
      }
    });
  },
  data() {
    return {
      Statustext: "Status  here",
      Locations: [
        { label: "Home", route: "/Home" }, // Use 'btn-yellow' class for the Home Location
        { label: "Location 1", route: "/Location1" }, // Use 'btn-pastel-pink' class for others
        { label: "Location 2", route: "/Location2" },
        { label: "Location 3", route: "/Location3" },
        { label: "Location 4", route: "/Location4" },
        { label: "Location 5", route: "/Location5" },
      ],
      //mqtt
      connection: {
        protocol: "wss",
        // protocol: "ws",
        host: "mqtt.noom.website",
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
        topic: "contro/status",
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
    };
  },
  mounted() {
    console.log("*******************************************");
    // console.log((localStorage.getItem("mail")))
    this.createConnection();
    this.doSubscribe();
  },
  methods: {
    navigate(route) {
      // console.log("Navigating to:", route);
      this.doPublish(route);
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
            console.log("Connection succeeded!");
          });
          this.client.on("reconnect", this.handleOnReConnect);
          this.client.on("error", (error) => {
            console.log("Connection failed", error);
          });
          this.client.on("message", (topic, message) => {
            this.receiveNews = this.receiveNews.concat(message);
            // console.log(`Received message ${message} from topic ${topic}`);
            this.Statustext = message;
            // console.log(message)

            // this.text = "OFF"

            // console.log()
            // for (let i = 0; i < this.countRover; i++) {
            //   // if (topic === "rover" + (i + 1) + "/status") {
            //   //   this.check[i] = this.timenow();
            //   // }
            //   console.log('rover'+ (i+1) +'/status')
            // }
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
        console.log("Subscribe to topics res", res);
      });
    },
    doPublish(text) {
      const { topic } = this.subscription;
      this.client.publish(topic, text);
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
  },
};
</script>

<style scoped>
/* Card Background Styling */
.background-card {
  border: none;
  box-shadow: none;
  padding: 0;
  margin: 0;
  width: 100vw; /* 100% of the viewport width */
  height: 100vh; /* 100% of the viewport height */
  position: absolute; /* Absolute positioning */
  top: 0; /* Start from the top edge of the screen */
  left: 0; /* Start from the left edge of the screen */
}

/* Minimalist Location Styling */
.custom-btn {
  border-radius: 5px !important;
  border: 2px solid transparent !important;
  color: #333 !important;
  transition: all 0.3s ease 0s !important;
}

.custom-btn:hover {
  background-color: #e3c567 !important; /* Light gray background color */
  border: 2px solid #333 !important;
}

/* Light Yellow Color for Home Location */
.btn-light-yellow {
  background-color: #7f5539 !important; /* Lighter shade of yellow */
  color: #fffcfc !important; /* Dark font color for better visibility */
}
.btn-pastel {
  background-color: #b08968 !important; /* Lighter shade of yellow */
  color: #ffffff !important; /* Dark font color for better visibility */
}
.responsive-img {
  max-width: 20%; /* Ensures the image doesn't stretch beyond its container */
  height: auto; /* Maintains the aspect ratio of the image */
  display: block; /* Removes any default margins or padding */
}
.bottom-space {
  margin-bottom: 20px; /* Adjust the value as needed */
}
.status-box {
  display: flex;
  align-items: center;
  justify-content: center;
  width: auto; /* Adjust width to match the Home button */
  height: auto; /* Adjust height to match the Home button */
  margin-top: 10px; /* Space between the image and the status box */
  padding: 10px 20px; /* Padding inside the status box */
  border: 2px solid transparent !important;
  transition: all 0.3s ease 0s !important;
}
/* Style for standard Locations */
</style>
