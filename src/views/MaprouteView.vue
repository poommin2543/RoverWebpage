<!-- <template>
  <div class="map-section">
    <gmap-map
      :center="{ lat: 14.874827, lng: 102.016729 }"
      :zoom="12"
      style="width: 100%; height: 100%"
      ref="gmap"
    >
    </gmap-map>
  </div>
</template>

<script>
import { gmapApi } from "vue2-google-maps";

export default {
  data() {
    return {
      map: null,
    };
  },
  computed: {
    google: gmapApi,
  },
  mounted() {
    this.$refs.gmap.$mapPromise.then((map) => {
      this.map = map;
      this.getRoute();
    });
  },
  methods: {
    getRoute() {
      const directionsService = new this.google.maps.DirectionsService();
      const directionsRenderer = new this.google.maps.DirectionsRenderer({suppressMarkers: true});
      directionsRenderer.setMap(this.map);

      const start = { lat: 14.87328, lng: 102.017933 };
      const end = { lat: 14.874544, lng: 102.020343 };

      directionsService.route(
        {
          origin: start,
          destination: end,
          travelMode: this.google.maps.TravelMode.DRIVING,
        },
        (response, status) => {
          if (status === "OK") {
            directionsRenderer.setDirections(response);
          } else {
            console.error("Directions request failed due to " + status);
          }
        }
      );
    },
  },
};
</script>
<style scoped>
.map-section {
  height: 100%;
  width: 100%;
}
</style> -->
<template>
  <div class="map-section">
    <gmap-map
      :center="{ lat: 14.874827, lng: 102.016729 }"
      :zoom="12"
      :options="mapOptions"
      style="width: 100%; height: 100%"
      ref="gmap"
    >
    </gmap-map>
  </div>
</template>
<script>
import { gmapApi } from "vue2-google-maps";
export default {
  data() {
    return {
      map: null,
      mapOptions: {
        styles: [
          {
            stylers: [{ hue: "#e4d4bc" }, { saturation: 250 }],
          },
          {
            featureType: "road",
            elementType: "geometry",
            stylers: [ { lightness: 0 }],
          },
          {
            featureType: "road",
            elementType: "labels.text.fill",
            stylers: [
              { color: "#c4bcac" }, // Change this to your desired color
            ],
          },
        ],
      },
    };
  },
  computed: {
    google: gmapApi,
  },
  mounted() {
    this.$refs.gmap.$mapPromise.then((map) => {
      this.map = map;
      this.getRoute();
    });
  },
  methods: {
    getRoute() {
      const directionsService = new this.google.maps.DirectionsService();
      const directionsRenderer = new this.google.maps.DirectionsRenderer({
        suppressMarkers: true,
        // polylineOptions: {
        //   strokeColor: '#b0bec5'  // change this to your desired color
        // }
      });
      directionsRenderer.setMap(this.map);

      const start = { lat: 14.87328, lng: 102.017933 };
      const end = { lat: 14.874544, lng: 102.020343 };

      directionsService.route(
        {
          origin: start,
          destination: end,
          travelMode: this.google.maps.TravelMode.WALKING,
        },
        (response, status) => {
          if (status === "OK") {
            directionsRenderer.setDirections(response);
          } else {
            console.error("Directions request failed due to " + status);
          }
        }
      );
    },
  },
};
</script>
<style scoped>
.map-section {
  height: 100%;
  width: 100%;
}
</style>
