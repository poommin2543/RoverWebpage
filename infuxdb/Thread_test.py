from threading import Thread
import pyrebase

config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjE",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_start(data):
    db.child("Rover1").stream(stream_handler)

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

def thread_callback(name, end):
    for i in range(1, end + 1):
        print(name + ": " + str(i))


thr1 = Thread(target=stream_start, args=['Thread-1'])
thr2 = Thread(target=thread_callback, args=['Thread-2', 100000])

thr1.start()
thr2.start()