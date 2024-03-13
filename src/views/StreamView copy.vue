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
      <input id="server-input" v-model="serverURL" placeholder="Enter server URL" />
    
      <button @click.prevent="applyServerSettings">Apply</button>
    </div>
    
    <div class="select-ctn">
      <select v-model="streamList.selected" :disabled="stream">
        <option v-for="option in streamList.options" :key="option.id" :value="option.id">
          {{ option.description }}
        </option>
      </select>
      <div>{{ stream == null ? "null" : notNull }}</div>
      <button @click.prevent="start" :disabled="stream">Start</button>
      <button @click.prevent="stop" :disabled="!stream">Stop</button>
    </div>
    <h3 v-if="status == 'starting'"> Loading video stream ...  </h3>
    <div class="video-vtn">
      <video autoplay="autoplay" :srcObject.prop="stream" ref="videoStream" playsinline width="640px" height="480px"></video>
    </div>
    <div v-if="!stream">No Stream</div>
    <div>Status: {{ status ? status : "No video stream" }}</div>
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script>
import { Janus } from 'janus-gateway'

// const JANUS_URL = 'http://127.0.0.1:8088/janus'
//const JANUS_URL = 'http://34.87.84.21:8088/janus'
// let JANUS_URL = 'https://34.143.225.243:8089/janus'
// let JANUS_URL = "https://janus.roverautonomous.com/janus";
// if(window.location.protocol === 'http:'){
//   //  JANUS_URL = 'http://34.143.225.243:8088/janus'
//    JANUS_URL = "https://janus.roverautonomous.com/janus";
// }


export default {
  name: 'App',
  data(){
    return {
      janus: null,
      error: null,
      plugin: null,
      status: null,
      stream: null,
      streamList: {
        selected: null,
        options: []
      },
      remoteTracks : {},
      remoteVideos : 0,
      serverProtocol: 'https', // Default protocol
      serverURL: 'janus.roverautonomous.com/janus', // User-defined server URL
      JANUS_URL: "", // Default Janus server URL
    }
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
  methods:{
    applyServerSettings() {
      // Construct the JANUS_URL from the user input
      this.JANUS_URL = `${this.serverProtocol}://${this.serverURL}`;
      // Now you can use this.JANUS_URL in the connect method or elsewhere
      console.log("Updated JANUS_URL:", this.JANUS_URL);
      // Optionally, reconnect to the Janus server with the new URL
      Janus.init({
      debug: true,
      dependencies: Janus.useDefaultDependencies(),
      callback: ()=>{
        console.log("Connecting to Janus api with server ",this.JANUS_URL)
        this.connect(this.JANUS_URL)
      }
    })
      // this.connect(this.JANUS_URL);
    },
    connect(server){
      this.janus = new Janus({server,
        // Call success callback
        success: ()=>{
          console.log("Connected")
          this.attachPlugin()
        },
        // Call error callback 
        error: (error)=>{
          console.log("Error")
          this.onError('Failed to connect janus server',error)
        },
        // Call destroyed callback
        destroyed: ()=>{
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
          console.log("getBitrate : ",this.plugin.getBitrate())
          this.updateStreamsList()
        },
        error: (error) => {
          this.onError('Error attaching plugin... ', error)
        },
        iceState: (state) => {
          console.log("ICE state changed to ",state)
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
          if(result){
            if(result.status){
              this.status = result.status
            }
          }
          // Handle msg error status 
          else if (msg.error) {
            this.onError(msg.error)
            this.stop()
            return ;
          }
          if(jsep) {
            Janus.debug("Handling SDP as Well... ", jsep)
            let stereo = (jsep.sdp.indexOf("stereo=1") !== -1 )
            this.plugin.createAnswer({
              jsep: jsep,
              media: {
                audioSend: false,
                videoSend: false,
                data: true
              },
              customizeSdp: (jsep) => {
                if(stereo && jsep.sdp.indexOf("stereo=1") == -1 ) {
                  jsep.sdp = jsep.sdp.replace("useinbandfec=1", "useinbandfec=1;stereo=1")
                }
              },
              success: (jsep) => {
                Janus.debug("Got SDP!", jsep)
                let body = { request: "start"}
                this.plugin.send({
                  message: body,
                  jsep: jsep
                })
              },
              error: (error) => {
                this.onError("WebRTC Error: ",error)
                alert("WebRTC error... " , error)
              }
            })
          }
        },
        onremotetrack: (track , mid, on) => {
          Janus.debug("Remote track (mid=" + mid + ") " + (on ? "added" : "removed") + ":", track)
          // New track was added 
          if(track.kind === "video") {
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
      this.plugin.send ({
        message: { request: "list"},
        success: (result) => {
          if(!result) {
            this.onError("Got no response to our query for available streams.")
          }
          console.log("Updating StreamList....",result)
          this.streamList.options = result.list
          if (result.list.length) {
            this.streamList.selected = this.streamList.options[0].id
          }
        }
      })
    },
    start() {
      this.plugin.send({ message: { request: "watch", id: this.streamList.selected } })
    },
    stop() {
      this.plugin.send({ message: { request: "stop" } } )
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
    onError(message, error='') {
      Janus.error(message, error)
      this.error = message + error
      alert(this.error, function() {
        window.location.reload()
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #48627c;
  margin-top: 60px;
}
div {
  margin-bottom: 1.5rem;
}
button {
  padding: .5rem .7rem;
  margin: 0 .5rem 0 .5rem;
}
video {
  width: 50%;
}
.server-ctn {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 10px; /* Adds space between elements */
}

.server-ctn label,
.server-ctn select,
.server-ctn input,
.server-ctn button {
  padding: 10px;
  margin: 5px;
  flex: 1 1 auto; /* Allows each element to grow and shrink as needed */
}

/* Responsive design for smaller screens */
@media (max-width: 768px) {
  .server-ctn {
    flex-direction: column; /* Stack elements vertically on small screens */
  }
}
</style>