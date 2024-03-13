<template>
  <div id="app">
    <h1>Poommin Testing WebRTC</h1>
    <h3>Using Janus webRTC server.</h3>
    <div class="server-ctn">
      <label for="protocol-select">Protocol:</label>
      <select v-model="serverProtocol">
        <option value="http">HTTP</option>
        <option value="https">HTTPS</option>
      </select>
      <label for="server-input">Server URL:</label>
      <input
        id="server-input"
        v-model="serverURL"
        placeholder="Enter server URL"
      />
      <!-- <button @click.prevent="applyServerSettings">Apply</button> -->
      <div class="my-2">
        <v-btn
          @click.prevent="applyServerSettings"
          color="secondary"
          dark
          large
        >
          Apply
        </v-btn>
      </div>
    </div>

    <div class="select-ctn">
      <select v-model="streamList.selected" :disabled="stream">
        <option
          v-for="option in streamList.options"
          :key="option.id"
          :value="option.id"
        >
          {{ option.description }}
        </option>
      </select>
      <div>{{ stream == null ? "null" : notNull }}</div>
      <v-btn @click.prevent="start" :disabled="stream" depressed color="primary"> Start </v-btn>
      <v-btn @click.prevent="stop" :disabled="!stream" depressed color="error"> Stop </v-btn>
      <!-- <button @click.prevent="start" :disabled="stream">Start</button>
      <button @click.prevent="stop" :disabled="!stream">Stop</button> -->
    </div>
    <h3 v-if="status == 'starting'">Loading video stream ...</h3>
    <div class="video-vtn">
      <video
        autoplay="autoplay"
        :srcObject.prop="stream"
        ref="videoStream"
        playsinline
        width="640px"
        height="480px"
      ></video>
    </div>
    <div v-if="!stream">No Stream</div>
    <div>Status: {{ status ? status : "No video stream" }}</div>
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script>
import { Janus } from "janus-gateway";

// const JANUS_URL = 'http://127.0.0.1:8088/janus'
//const JANUS_URL = 'http://34.87.84.21:8088/janus'
// let JANUS_URL = 'https://34.143.225.243:8089/janus'
// let JANUS_URL = "https://janus.roverautonomous.com/janus";
// if(window.location.protocol === 'http:'){
//   //  JANUS_URL = 'http://34.143.225.243:8088/janus'
//    JANUS_URL = "https://janus.roverautonomous.com/janus";
// }

export default {
  name: "App",
  data() {
    return {
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
      serverProtocol: "https", // Default protocol
      serverURL: "janus.roverautonomous.com/janus", // User-defined server URL
      JANUS_URL: "", // Default Janus server URL
    };
  },
  mounted() {
    // Janus.init({
    //   debug: true,
    //   dependencies: Janus.useDefaultDependencies(),
    //   callback: ()=>{
    //     console.log("Connecting to Janus api with server ",JANUS_URL)
    //     this.connect(JANUS_URL)
    //   }
    // })
  },
  methods: {
    applyServerSettings() {
      // Construct the JANUS_URL from the user input
      this.JANUS_URL = `${this.serverProtocol}://${this.serverURL}`;
      // Now you can use this.JANUS_URL in the connect method or elsewhere
      console.log("Updated JANUS_URL:", this.JANUS_URL);
      // Optionally, reconnect to the Janus server with the new URL
      Janus.init({
        debug: true,
        dependencies: Janus.useDefaultDependencies(),
        callback: () => {
          console.log("Connecting to Janus api with server ", this.JANUS_URL);
          this.connect(this.JANUS_URL);
        },
      });
      // this.connect(this.JANUS_URL);
    },
    connect(server) {
      this.janus = new Janus({
        server,
        // Call success callback
        success: () => {
          console.log("Connected");
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
          this.updateStreamsList();
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
          console.log(" ::: Got a message :::", msg);
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
          console.log("Updating StreamList....", result);
          this.streamList.options = result.list;
          if (result.list.length) {
            this.streamList.selected = this.streamList.options[0].id;
          }
        },
      });
    },
    start() {
      this.plugin.send({
        message: { request: "watch", id: this.streamList.selected },
      });
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
    createParticles(event) {
      // Reference to the button, ensuring that particles are appended within the component
      console.log("Click");
      const button = event.currentTarget;
      const particlesNumber = 30;

      for (let i = 0; i < particlesNumber; i++) {
        let particle = document.createElement("span");
        particle.classList.add("particle", "scoped-particle"); // Adding a class for scoped styling

        // Position particles relative to the button
        let rect = button.getBoundingClientRect();
        let buttonX = rect.left + rect.width / 2;
        let buttonY = rect.top + rect.height / 2;

        const x = (Math.random() - 0.5) * (Math.random() * 100);
        const y = (Math.random() - 0.5) * (Math.random() * 100);
        const size = Math.random() * 10 + 5;
        const hue = Math.random() * 360;

        particle.style.left = `${buttonX}px`;
        particle.style.top = `${buttonY}px`;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.background = `hsl(${hue}, 100%, 50%)`;

        // Now append particle to the button instead of body
        button.appendChild(particle);

        // Set CSS variables for the animation
        particle.style.setProperty("--x", `${x}px`);
        particle.style.setProperty("--y", `${y}px`);

        // Clean up after animation ends
        particle.addEventListener("animationend", function () {
          particle.remove();
        });
      }
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f4f9;
  color: #333;
  line-height: 1.6;
}

#app {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 1rem;
  text-align: center;
}

/* Headings */
h1 {
  font-size: 2.5rem;
  color: #255957;
  margin-bottom: 1rem;
}

h3 {
  font-size: 1.2rem;
  color: #457b9d;
  margin-bottom: 1rem;
}

/* Server Container */
.server-ctn {
  background-color: #fff;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 2rem;
}

.server-ctn label {
  flex-basis: 100%;
  text-align: left;
  font-weight: 600;
  color: #3a506b;
}

.server-ctn select,
.server-ctn input {
  padding: 0.5rem 1rem;
  border: 2px solid #ced4da;
  border-radius: 5px;
  width: calc(50% - 20px);
  transition: border-color 0.3s ease-in-out;
}

.server-ctn select:focus,
.server-ctn input:focus {
  border-color: #495867;
  outline: none;
}

/* Buttons */
.explosion-btn .scoped-particle {
  /* styles for particle */
  position: absolute;
  border-radius: 50%;
  background-color: gold;
  opacity: 0;
  pointer-events: none;
  animation: explode 700ms cubic-bezier(0.19, 1, 0.22, 1) forwards;
}

/* Define the keyframes for the explode animation within the scoped style */
@keyframes explode {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(3) translate(var(--x), var(--y));
    opacity: 0;
  }
}

/* Stream Container */
.select-ctn {
  background-color: #fff;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

/* Video */
.video-vtn {
  background-color: #fff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.2);
  line-height: 0;
  margin-bottom: 2rem;
}

video {
  width: 100%;
  height: auto;
}

/* Status and Error Messages */
.status-message {
  background-color: #e63946;
  color: #fff;
  padding: 0.75rem;
  border-radius: 5px;
  margin-bottom: 1rem;
  display: inline-block;
}

/* Responsive Design */
@media (max-width: 768px) {
  .server-ctn,
  .select-ctn {
    flex-direction: column;
  }

  .server-ctn select,
  .server-ctn input {
    width: 100%;
  }
}
</style>
