<template>
  <div class="map-section">
    <gmap-map
      :center="center"
      :zoom="17"
      style="width: 100%; height: 100%"
      :options="{
        ...{
          zoomControl: true,
          scaleControl: true,
          mapTypeControl: true,
          panControl: false,
          streetViewControl: true,
          fullscreenControl: true,
          disableDefaultUi: true,
          overviewMapControl: true,
          scrollwheel: true,
        },
        ...mapOptions,
      }"
      ref="gmap"
    >
      <gmap-marker
        v-for="(item, key) in coordinates"
        :key="key"
        :position="getPosition(item)"
        :clickable="true"
        :icon="getMarkers1(key)"
        @click="toggleInfo(item, key)"
      ></gmap-marker>
      <!-- <gmap-marker v-on:change="updateCoordinates()" :position="center" :draggable="true" @closeclick="updateCoordinates()"/> -->
    </gmap-map>
    <!-- <v-overlay absolute="True" :opacity="opacity">
      
      <v-btn>
        Button
      </v-btn>
    </v-overlay> -->
    <v-overlay :absolute="true" :value="true" class="overlay-position"
                opacity="0">
      <!-- Content goes here -->
      <div>
        <!-- <v-btn> Button </v-btn> -->
        <v-img :src="require('../assets/img/iconroute.png')" 
        @click="drawRouteBetweenRoverAndUser"/>
      </div>
    </v-overlay>
  </div>
</template>

<script>
import firebaseApp from "@/plugins/firebase";
import $ from "jquery";
import { gmapApi } from "vue2-google-maps";
var la = 0;
var long = 0;
var la_User = 0;
var long_User = 0;
// var la = 14.875811571268388;
// var long = 102.01502828868293;
// var la_User = 14.875811571268388;
// var long_User = 102.01502828868293;

let iconCar = require("../assets/img/Roverclass.svg");
// let iconroute = require("../assets/img/iconroute.svg");
let mapMarkerActive =
  "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png";
let iconUser = "https://i.postimg.cc/bNC9tsGz/icons8-iphone-se-80.png";
export default {
  name: "MapShow",

  props: {
    LogoImg: {
      type: String,
      default: require("../assets/img/class_front.png"),
    },
    // LogoRoute: {
    //   type: String,
    //   default: require("../assets/img/iconroute.svg"),
    // },
    propNameRover: {
      type: String,
      required: false,
    },
  },
  data: function () {
    return {
      directionsRenderer: null,
      mapOptions: {
        styles: [
          {
            stylers: [{ hue: "#FCECD9" }, { saturation: 0 }],
            // stylers: [{ hue: "#D3EAFF" }, { saturation: 0 }],
          },
          {
            featureType: "road",
            elementType: "geometry",
            stylers: [{ lightness: 0 }],
          },
          {
            featureType: "road",
            elementType: "labels.text.fill",
            stylers: [{ color: "#c4bcac" }],
          },
        ],
      },
      // mapMarker,
      isActive: true,
      namerover: null,
      // NameRover: localStorage.getItem("name-Rover"),
      rotatestatus: null,
      user: {
        username: "matt",
      },
      mapMarkerActive,
      iconCar,
      iconUser,
      latitude: 0,
      longitude: 0,
      center: {
        lat: 0,
        lng: 0,
      },
      locations: [],
      currentLocation: null,
      selectedKey: null,
      selectedMarker: null,
      coordinates: {
        0: {
          lat: la.toString(),
          lng: long.toString(),
        },
        1: {
          lat: la_User.toString(),
          lng: long_User.toString(),
        },
      },
    };
  },
  computed: {
    google: gmapApi,
  },
  watch: {
    propNameRover: function (newVal, old) {
      // watch it
      // console.log('Prop changed: ', newVal, ' | was: ')

      this.StartgetLocationRover(newVal, old);
      this.StartgetLocationUser(newVal, old);
      setTimeout(() => {
        this.drawRouteBetweenRoverAndUser();
      }, 2000);
    },
  },
  mounted() {
    // this.interval = setInterval(() => this.nameRoverupdate(), 3000);
    this.namerover = localStorage.getItem("Name-rover");

    console.log(this.namerover + "55555555");

    setTimeout(() => {
      this.StartgetLocationUser(this.namerover, this.namerover);
      this.StartgetLocationRover(this.namerover, this.namerover);
    }, 1000);
    setTimeout(() => {
      this.drawRouteBetweenRoverAndUser();
    }, 2000);
  },
  methods: {
    test(){
      console.log("555555555555555555555")
    },
    drawRouteBetweenRoverAndUser() {
      this.$refs.gmap.$mapPromise.then((map) => {
        this.map = map;
        this.getRoute({ lat: la, lng: long }, { lat: la_User, lng: long_User });
      });
    },
    deleteRoute() {
      if (this.directionsRenderer) {
        console.log("***************");
        console.log(this.directionsRenderer);
        // this.directionsRenderer.setDirections(null);
        this.directionsRenderer.setMap(null);
        console.log("***************");
      }
    },
    getRoute(start, end) {
      console.log("----------------------------");
      console.log(start, end);
      console.log("----------------------------");
      this.deleteRoute(); // Delete the old route
      const directionsService = new this.google.maps.DirectionsService();
      this.directionsRenderer = new this.google.maps.DirectionsRenderer({
        suppressMarkers: true,
      });

      this.directionsRenderer.setMap(this.map);

      directionsService.route(
        {
          origin: start,
          destination: end,
          travelMode: this.google.maps.TravelMode.WALKING,
        },
        (response, status) => {
          if (status === "OK") {
            // this.directionsRenderer.setDirections(null);
            // directionsRenderer.setDirections(null);
            // this.directionsRenderer.setDirections(null);
            this.directionsRenderer.setDirections(response);
          } else {
            console.error("Directions request failed due to " + status);
          }
        }
      );
    },
    StartgetLocationRover(rovername, old) {
      console.log(rovername, old);
      if (rovername != old) {
        // console.log(rovername,old)
        this.dbRefRover.off();
        this.rotateRover(0);
      }
      console.log(rovername + "/location/rover");
      this.dbRefRover = firebaseApp
        .database()
        .ref(rovername + "/location/rover");
      this.dbRefRover.on("value", (ss) => {
        // console.log(ss.val());
        for (const [key, value] of Object.entries(ss.val())) {
          if (key == "latitude") {
            this.latitude = value;
            console.log(`${key} Rover: ${value}`);
            la = value;
          }
          if (key == "rotate") {
            this.rotatestatus = value;
            console.log(`${key} Rover: ${value}`);
            this.rotateRover(this.rotatestatus);
          }
          if (key == "longitude") {
            this.longitude = value;
            console.log(`${key}: ${value}`);
            long = value;
          }
          // this.center = {
          //   lat: (la + la_User) / 2,
          //   lng: (long + long_User) / 2
          // }
          this.coordinates = {
            0: {
              lat: la.toString(),
              lng: long.toString(),
            },
            1: {
              lat: la_User.toString(),
              lng: long_User.toString(),
            },
          };
        }
      });
      this.center = {
        lat: 14.8721436,
        lng: 102.02077519999999,
      };
      // this.center = {
      //       lat: (la + la_User) / 2,
      //       lng: (long + long_User) / 2
      //     }
    },
    StartgetLocationUser(rovername, old) {
      console.log(rovername, old);
      if (rovername != old) {
        // console.log(rovername,old)
        this.dbRefUser.off();
        this.rotateRover(0);
      }

      this.dbRefUser = firebaseApp.database().ref(rovername + "/location/user");
      this.dbRefUser.on("value", (ss) => {
        console.log(ss.val());
        for (const [key, value] of Object.entries(ss.val())) {
          if (key == "latitude") {
            this.latitude = value;
            console.log(`${key} User: ${value}`);
            // this.latitude;
            la_User = value;
          }
          if (key == "longitude") {
            this.longitude = value;
            console.log(`${key} User: ${value}`);
            long_User = value;
          }
          this.coordinates = {
            0: {
              lat: la.toString(),
              lng: long.toString(),
            },
            1: {
              lat: la_User.toString(),
              lng: long_User.toString(),
            },
            //
          };
        }
      });
      this.center = {
        lat: 14.8721436,
        lng: 102.02077519999999,
      };
    },

    getMarkers(key) {
      if (this.selectedKey === key) return this.mapMarkerActive;
      return this.mapMarker;
    },
    getMarkers1(key) {
      // console.log(key)
      if (key == 0) {
        return this.iconCar;
      }
      if (key == 1) {
        return this.iconUser;
      }
    },
    rotateRover(rotate) {
      $(`img[src="${iconCar}"]`).css({
        "-webkit-transform": "rotate(" + rotate + "deg)",
        "-moz-transform": "rotate(" + rotate + "deg)",
        "-ms-transform": "rotate(" + rotate + "deg)",
        transform: "rotate(" + rotate + "deg)",
      });
    },
    getPosition: function (marker) {
      return {
        lat: parseFloat(marker.lat),
        lng: parseFloat(marker.lng),
      };
    },
    toggleInfo: function (marker, key) {
      this.infoPosition = this.getPosition(marker);
      this.selectedMarker = marker;
      this.selectedKey = key;
      this.infoOpened = !this.infoOpened;
    },
    closeInfoWindow: function () {
      this.infoOpened = false;
      this.markerOptions = this.mapMarker;
    },
    setPlace(loc) {
      this.currentLocation = loc;
    },
    setLocationLatLng: function () {
      navigator.geolocation.getCurrentPosition((geolocation) => {
        this.center = {
          lat: geolocation.coords.latitude,
          lng: geolocation.coords.longitude,
        };
      });
    },
  },
  created() {
    // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
    // this.dbRef = firebaseApp.database().ref('Rover1/location/rover')
    // this.dbRef1 = firebaseApp.database().ref('Rover1/location/user')
  },
  beforeDestroy() {
    // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
    // this.dbRef.off()
    // this.dbRef1.off()
  },
};
</script>
<style scoped>
.map-section {
  height: 100%;
  width: 100%;
}
.overlay-position {
  position: absolute;
  top: 12%;
  left: 5%;
  width: 50px;
  height: 50px;
  z-index: 10;
}
.content-align-right {
  text-align: right;
}
</style>
