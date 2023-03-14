import firebase from 'firebase/compat/app'
import 'firebase/compat/database'

// ค่า minimum configuration คือ `apiKey` และ `databaseURL`
const config = {
    apiKey: "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjE",
    authDomain: "location-a26be.firebaseapp.com",
    databaseURL: "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "location-a26be",
    storageBucket: "location-a26be.appspot.com",
    messagingSenderId: "275944322136",
    appId: "1:275944322136:web:70f14965096c7dff1e462d",
    measurementId: "G-2W7W0Z25Y4"
}

// คืนค่า firebase application ที่อาจถูก instantiate แล้วหรือ instantiate ใหม่
export default firebase.apps[0] || firebase.initializeApp(config)
