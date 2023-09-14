<!-- 
<template>
    <v-app>
      <v-container>
        <v-row class="justify-space-around">
          <v-col v-for="btn in Locations" :key="btn.label" cols="12" sm="4" lg="4" xs="12">
            <v-btn block color="primary" outlined @click="navigate(btn.route)">
                {{ btn.label }}
              </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        Locations: [
          { label: 'Home', route: '/' },
          { label: 'Location 1', route: '/Location1' },
          { label: 'Location 2', route: '/Location2' },
          { label: 'Location 3', route: '/Location3' },
          { label: 'Location 4', route: '/Location4' },
          { label: 'Location 5', route: '/Location5' },
        ],
      };
    },
    methods: {
      navigate(route) {
        // For demonstration purposes, we'll just log the route.
        // In a real application, you'd use Vue Router to navigate.
        console.log("Navigating to:", route);
      },
    },
  };
  </script>
   -->
   <template>
    <v-app>
      <!-- Use a large card-like container as the background -->
      <v-card color="#edede9" class="background-card"> <!-- Set a light gray background color -->
        <v-container class="custom-container">
          <v-row class="justify-space-around">
            <v-col v-for="btn in Locations" :key="btn.label" cols="12" sm="4" lg="4" xs="12">
              <v-btn
                class="custom-btn"
                :class="btn.label === 'Home' ? 'btn-light-yellow' : 'btn-pastel'"
                block
                outlined
                @click="navigate(btn.route)"
              >
                {{ btn.label === 'Home' ? 'Home' : btn.label }} <!-- Change 'Location' to 'Location' for all Locations -->
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
          { label: 'Home', route: '/', color: 'btn-yellow' }, // Use 'btn-yellow' class for the Home Location
          { label: 'Location 1', route: '/Location1', color: 'btn-pastel-pink' }, // Use 'btn-pastel-pink' class for others
          { label: 'Location 2', route: '/Location2', color: 'btn-pastel-green' },
          { label: 'Location 3', route: '/Location3', color: 'btn-pastel-yellow' },
          { label: 'Location 4', route: '/Location4', color: 'btn-pastel-purple' },
          { label: 'Location 5', route: '/Location5', color: 'btn-pastel-orange' },
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
  }
  
  /* Minimalist Location Styling */
  .custom-btn {
    border-radius: 5px !important;
    border: 2px solid transparent !important;
    color: #333 !important;
    transition: all 0.3s ease 0s !important;
  }
  
  .custom-btn:hover {
    background-color: #f0f0f0 !important; /* Light gray background color */
    border: 2px solid #333 !important;
  }
  
  /* Light Yellow Color for Home Location */
  .btn-light-yellow {
    background-color: #d5bdaf!important; /* Lighter shade of yellow */
    color: #333 !important; /* Dark font color for better visibility */
  }
  .btn-pastel {
    background-color: #e3d5ca !important; /* Lighter shade of yellow */
    color: #333 !important; /* Dark font color for better visibility */
  }
  
  /* Style for standard Locations */
  
  </style>
  