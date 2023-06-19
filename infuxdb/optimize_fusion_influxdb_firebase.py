from threading import Thread, Event
from influxdb import InfluxDBClient
import pyrebase
import time

namerover = "rover001"
datarover = "Rover1"

class DataProcessor:
    def __init__(self):
        self.json_body = []
        self.stop_event = Event()
        ststusconnext = False
        while ststusconnext is not True:
            self.my_Client = InfluxDBClient(
                host='172.25.3.3',
                port=8086,
                username='rover',
                password="acselab1234",
                ssl=False,
                verify_ssl=False
            )
            connext = self.my_Client.switch_database('mydatabase')
            try:
                self.my_Client.ping()
                print("Connection successful")
                ststusconnext = True
            except Exception as e:
                print(f"Failed to connect to InfluxDB: {str(e)}")
        # print(self.my_Client)

        config = {
            "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjE",
            "authDomain": "location-a26be.firebaseapp.com",
            "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
            "storageBucket": "location-a26be.appspot.com"
        }

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def construct_json_body(self, latitude, longitude, rotate, Battery, mode, door, idcam, velocity):
        return [
            {
                "measurement": "backupdata",
                "tags": {
                    "user": namerover,
                    "idcam": idcam,
                },
                "fields": {
                    "latitude": latitude,
                    "longitude": longitude,
                    "rotate": rotate,
                    "Battery": Battery,
                    "mode": mode,
                    "door": door,
                    "velocity": velocity,
                }
            }
        ]

    def stream_start_test(self):
        self.db.child(datarover).stream(self.stream_handler)

    def stream_handler(self, message):
        global latitude,longitude,rotate,Battery,mode,door,idcam,velocity  # Default value
        if message["path"] == "/":
            data = message["data"]
            latitude = (data["location"]["rover"]["latitude"])
            longitude = (data["location"]["rover"]["longitude"])
            rotate = (data["location"]["rover"]["rotate"])
            Battery = (data["status"]["Battery"])
            mode = (data["status"]["auto"])
            door = (data["status"]["door"])
            idcam = (data["status"]["idcam"])
            velocity = (data["status"]["velocity"])
        else:
            if message["path"] == "/location/rover/latitude":
                latitude = message["data"]
            if message["path"] == "/location/rover/longitude":
                longitude = message["data"]
            if message["path"] == "/location/rover/rotate":
                rotate = message["data"]
            if message["path"] == "/status/Battery":
                Battery = message["data"]
            if message["path"] == "/status/auto":
                mode = message["data"]
            if message["path"] == "/status/door":
                door = message["data"]
            if message["path"] == "/status/idcam":
                idcam = message["data"]
            if message["path"] == "/status/velocity":
                velocity = message["data"]

        self.json_body = self.construct_json_body(latitude, longitude, rotate, Battery, mode, door, idcam, velocity)

    def influxdb_up(self):
        try:
            while not self.stop_event.is_set():  # loop until stop_event is set
                if self.json_body:
                    print(self.my_Client.write_points(self.json_body))
                    print(self.json_body)
                time.sleep(5)  # pause for 5 seconds
        except Exception as e:  # allow the user to interrupt the program with Ctrl+C
            print(f"Error occurred: {e}")
        finally:
            self.my_Client.close()
            print("Stopping program")

data_processor = DataProcessor()

thr1 = Thread(target=data_processor.stream_start_test)
thr2 = Thread(target=data_processor.influxdb_up) 

thr1.start()
thr2.start()

try:
    while True:
        time.sleep(1)  # main thread is alive as long as the other threads are
except KeyboardInterrupt:
    data_processor.stop_event.set()  # stop the threads

thr1.join()
thr2.join()
