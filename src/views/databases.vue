<template>
  <!-- eslint-disable -->
  <div>
    <v-btn @click="readEmployees">
      Button
    </v-btn>
    <v-btn @click="createEmployee">
      Button
    </v-btn>
  </div>
</template>

<script>
import firebase from "@/plugins/firebase";
const db = firebase.firestore();

export default {
  name: "app",
  data() {
    return {
      name: "",
      employeesData: []
    };
  },
  methods: {
    createEmployee() {
        db.collection("users")
          .add({ date: "date", name: "name" })
          .then(() => {
            console.log("Document successfully written!");
          })
          .catch((error) => {
            console.error("Error writing document: ", error);
          });
    },
    readEmployees() {
      let employeesData = [];
      db.collection("user")
        .get()
        .then((querySnapshot) => {
          querySnapshot.forEach((doc) => {
            // console.log(doc.id, " => ", doc.data());
            employeesData.push({
              id: doc.id,
              name: doc.data().name,
              date: doc.data().date
            });
            console.log(doc.id, " => ", doc.data());
            if (doc.id == "noom@noom.com") {
              console.log(doc.data().name)
              console.log(doc.data().lastname)

            }

          });
          this.employeesData = employeesData; // Update the component data property
        })
        .catch((error) => {
          console.log("Error getting documents: ", error);
        });
    }
  }
};
</script>
