<template>
  <div class="map-section">
    <!-- <v-btn @click="noom">Click</v-btn> -->
    <gmap-map :center="center" :zoom="17" style="width: 100%; height: 100%" :options="{
      zoomControl: true,
      scaleControl: true,
      mapTypeControl: true,
      // mapTypeId: 'Map',
      // mapTypeId: 'satellite',
      panControl: false,
      streetViewControl: true,
      fullscreenControl: true,
      // streetViewControl: false,
      // disableDefaultUi: false
      disableDefaultUi: true,
      overviewMapControl: true,
      scrollwheel: true,
    }">

      <!-- <gmap-marker v-for="(item, key) in coordinates" :key="key" :position="getPosition(item)" :clickable="true"
        :icon="getMarkers1(key)" @click="toggleInfo(item, key)"></gmap-marker> -->
      <gmap-marker v-for="(item, key) in coordinates" :key="key" :position="getPosition(item)" :clickable="true"
        :icon="iconCar" @click="toggleInfo(item, key)"></gmap-marker>
    </gmap-map>

  </div>
</template>

<script>
import firebaseApp from '@/plugins/firebase'
// import $ from "jquery";
let iconCar = require('../assets/img/rovertop.svg');
let mapMarkerActive = "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png";
let iconUser = "https://i.postimg.cc/bNC9tsGz/icons8-iphone-se-80.png";

export default {
  name: "MapShow",

  props: {
    LogoImg: {
      type: String,
      default: require('../assets/img/class_front.png'),
    },
    propC: {
      type: String,
      required: true
    },

  },
  data: function () {
    
    return {
      readData: null,
      // mapMarker,
      isActive: true,
      namerover: "------",
      // NameRover: localStorage.getItem("name-Rover"),
      user: {
        username: 'matt'
      },
      mapMarkerActive,
      iconCar,
      iconUser,
      latitude: 0,
      longitude: 0,
      center: {
        lat: 14.874827,
        lng: 102.01551
      },
      locations: [],
      currentLocation: null,
      selectedKey: null,
      selectedMarker: null,
      coordinates: {
        0: {
          lat: 14.874827,
          lng: 102.01551
        },
        // 0: {
        //   lat: la.toString(),
        //   lng: long.toString()
        // },
        // 1: {
        //   lat: la_User.toString(),
        //   lng: long_User.toString()
        // },
      }
    };
  },
  computed: {
    // readonly
    SetdatafromHomepage() {
      let readData = this.propC
      console.log(this.propC + "-----------" + this.propC)
      return readData
    }

  },
  mounted() {
    // let i = 0;
    // setInterval(() => {
    //   $(`img[src="${iconCar}"]`).css(
    //     '-webkit-transform', 'rotate(' + i + 'deg)',
    //     '-moz-transform', 'rotate(' + i + 'deg)',
    //     '-ms-transform', 'rotate(' + i + 'deg)',
    //     'transform', 'rotate(' + i + 'deg)');
    //     console.log(i)
    //   i += 90;
    // }, 1000);
    // this.interval = setInterval(() => this.nameRoverupdate(), 3000);
    this.dbRef.on('value', ss => {
      let i = 0
      // console.log(ss.val());
      for (const [key, value] of Object.entries(ss.val())) {
        console.log(i, key, value)
        try {
          // console.log(value.location.rover.latitude)
          // console.log(value.location.rover.longitude)
          this.coordinates[i] = {
            lat: value.location.rover.latitude.toString(),
            lng: value.location.rover.longitude.toString()
          }
          // this.coordinates[i] = value.location.rover
          // tryStatements
        } catch (exceptionVar) {
          // catchStatements
        }

        i++
      }
    }
    )

    this.setLocationLatLng();
    console.log("+++++++++++>")
    // this.SetdatafromHomepage();
    // let noom = this.SetdatafromHomepage();
    // console.log(noom)
    console.log("<+++++++++++")

    
  },
  methods: {
    // nameRoverupdate() {
    //   // Define the string
    //   var encodedStringAtoB = localStorage.getItem("name-Rover");
    //   // Decode the String
    //   var decodedStringAtoB = atob(encodedStringAtoB);
    //   this.NameRover = decodedStringAtoB
    // },
    // rotate(rotate) {
    //     $(img[src="${my_icon}"]).css(
    //         {'-webkit-transform' : 'rotate('+ rotate +'deg)',
    //    '-moz-transform' : 'rotate('+ rotate +'deg)',
    //    '-ms-transform' : 'rotate('+ rotate +'deg)',
    //    'transform' : 'rotate('+ rotate +'deg)'});
    //     },
    
    noom() {
      console.log(this.coordinates)

      // console.log(coordinates)
    },
    // updateCoordinates() {
    //       this.coordinates = {
    //           lat: la,
    //           lng: long,
    //       };
    //   },
    // getMarkers(key) {
    //   if (this.selectedKey === key) return this.mapMarkerActive;
    //   return this.mapMarker;
    // },
    getMarkers1(key) {
      console.log(key)
      // if (key == 0) {
      //   return this.iconCar;
      // }
      // if (key == 1) {
      //   return this.iconUser;
      // }
      return this.iconCar;
      // if (this.selectedKey === key) return this.mapMarker;
      // return this.mapMarkerActive;
    },
    getPosition: function (marker) {
      return {
        lat: parseFloat(marker.lat),
        lng: parseFloat(marker.lng)
      };
    },
    toggleInfo: function (marker, key) {
      console.log(marker, key)
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
      navigator.geolocation.getCurrentPosition(geolocation => {
        this.center = {
          lat: geolocation.coords.latitude,
          lng: geolocation.coords.longitude
        };
      });
      // this.locations = [
      //   {
      //       lat: la,
      //       lng: long,
      //       label: 'user location'
      //   },
      // {
      //     lat: 14.874727933912586,
      //     lng: 102.0155504911628,
      //     label: 'Car'
      // },
      // {
      //     lat: 41.3828939,
      //     lng: 2.1774322,
      //     label: 'Barcelona'
      // },
      // {
      //     lat: -10.3333333,
      //     lng: -53.2,
      //     label: 'Brazil'
      // }
      // ];
    }
  },
  created() {
    // สร้าง reference ไปยัง counter ซึ่งเป็น root node ของ reatime database
    this.dbRef = firebaseApp.database().ref('/')
    this.dbRef1 = firebaseApp.database().ref('Rover1/location/user')
  },
  beforeDestroy() {
    // ยกเลิก subsciption เมื่อ component ถูกถอดจาก dom
    this.dbRef.off()
    this.dbRef1.off()
  }
};
</script>
<style scoped>
.map-section {
  height: 100%;
  width: 100%;
}

.map-info-window {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: #fff;
  padding: 15px 20px 10px;
}

.map-info-window-slide-leave-active,
.map-info-window-slide-enter-active {
  transition: 0.5s;
}

.map-info-window-slide-enter {
  transform: translate(0, -100%);
}

.map-info-window-slide-leave-to {
  transform: translate(0, -100%);
}

.city-info>div {
  margin-bottom: 10px;
}

.map-btn-close-holder {
  margin-top: 10px;
}

nav {
  padding: 100px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>