<template>
  <v-app>
    <!-- Use a large card-like container as the background -->
    <v-card color="#e6ccb2" class="background-card">
      <!-- Set a light gray background color -->
      <v-container class="custom-container">
        <v-card flat class="d-flex flex-column align-center justify-center bottom-space" color="transparent">
          <img
              class="responsive-img"
              :src="require('../assets/img/Hot-Cup-Of-Coffee.svg')"
              alt="Coffee Cup"
          />
      </v-card>
      <v-card :class="Locations[0].color + ' status-box'" flat color="#e6ccb2">
        <!-- Replace 'Status goes here' with your dynamic status data -->
        <span>Status goes here</span>
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
export default {
  data() {
    return {
      Locations: [
        { label: "Home", route: "/", color: "btn-yellow" }, // Use 'btn-yellow' class for the Home Location
        { label: "Location 1", route: "/Location1", color: "btn-pastel-pink" }, // Use 'btn-pastel-pink' class for others
        { label: "Location 2", route: "/Location2", color: "btn-pastel-green" },
        {
          label: "Location 3",
          route: "/Location3",
          color: "btn-pastel-yellow",
        },
        {
          label: "Location 4",
          route: "/Location4",
          color: "btn-pastel-purple",
        },
        {
          label: "Location 5",
          route: "/Location5",
          color: "btn-pastel-orange",
        },
      ],
    };
  },
  methods: {
    navigate(route) {
      console.log("Navigating to:", route);
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
  width: 100vw;   /* 100% of the viewport width */
  height: 100vh;  /* 100% of the viewport height */
  position: absolute; /* Absolute positioning */
  top: 0;        /* Start from the top edge of the screen */
  left: 0;       /* Start from the left edge of the screen */
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
  max-width: 20%;  /* Ensures the image doesn't stretch beyond its container */
  height: auto;     /* Maintains the aspect ratio of the image */
  display: block;   /* Removes any default margins or padding */
}
.bottom-space {
  margin-bottom: 20px;  /* Adjust the value as needed */
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
