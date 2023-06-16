from threading import Thread
from influxdb import InfluxDBClient
import pyrebase
import time
my_Client = InfluxDBClient(
    host='172.25.3.3',
    port=8086,
    username='rover',
    password="acselab1234",
    ssl=False,
    verify_ssl=False
)
my_Client.switch_database('mydatabase')

config = {
    "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjE",
    "authDomain": "location-a26be.firebaseapp.com",
    "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "location-a26be.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
json_body = []


def stream_start_test(data):
    db.child("Rover1").stream(stream_handler)


def stream_handler(message):
    global json_body
    global latitude,longitude,rotate,Battery,mode,door,idcam,velocity  # Default value
    # latitude=longitude=rotate=Battery=mode=door=idcam=velocity = None  # Default value
    # {'control': {'backword': 0, 'forword': 0, 'left': 0, 'right': 0}, 'location': {'rover': {'latitude': 14.875359, 'longitude': 102.0154718, 'rotate': 336}, 'user': {'altitude': 237.30590336490422, 'latitude': 14.875733, 'longitude': 102.015569}}, 'status': {'Battery': 100, 'auto': True, 'door': False, 'idcam': 11, 'status': 0, 'velocity': 1}}
    if message["path"] == "/":
        # print(message["event"])  # put
        # print(message["path"])  # /-K7yGTTEp7O549EzTYtI
        # print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}
        data = message["data"]
        # print(data["location"])
        latitude = (data["location"]["rover"]["latitude"])
        # print(type(latitude))
        longitude = (data["location"]["rover"]["longitude"])
        rotate = (data["location"]["rover"]["rotate"])
        Battery = (data["status"]["Battery"])
        mode = (data["status"]["auto"])
        door = (data["status"]["door"])
        idcam = (data["status"]["idcam"])
        velocity = (data["status"]["velocity"])
        # json_body = [
        #     {
        #         "measurement": "cputest",
        #         "tags": {
        #             # "host": "server01",
        #             # "region": "us-west"
        #             "user": "rover001",
        #             "idcam": idcam,
        #             # "brushId": "6a89f539-71c6-490d-a28d-6c5d84c0ee2fw"
        #         },
        #         "fields": {
        #             "latitude": latitude,
        #             "longitude": longitude,
        #             "rotate": rotate,
        #             "Battery": Battery,
        #             "mode": mode,
        #             "door": door,
        #             "velocity": velocity,
        #         }
        #     }
        # ]

    elif message["path"] != "/":
        # print(message["event"])  # put
        # print(message["path"])  # /-K7yGTTEp7O549EzTYtI
        # print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}
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
    
    json_body = [
        {
            "measurement": "backupdata",
            "tags": {
                # "host": "server01",
                # "region": "us-west"
                "user": "rover001",
                "idcam": idcam,
                # "brushId": "6a89f539-71c6-490d-a28d-6c5d84c0ee2fw"
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
    # print(json_body)
# def thread_callback(name, end):
#     for i in range(1, end + 1):
#         print(name + ": " + str(i))


def influxdb_up(data):
    try:
        while True:  # loop indefinitely
            if json_body!=[]:
                print(my_Client.write_points(json_body))
            print(json_body)
            time.sleep(5)  # pause for 5 seconds
    except KeyboardInterrupt:  # allow the user to interrupt the program with Ctrl+C
        my_Client.close()
        print("Stopping program")
    finally:
        my_Client.close()
    # pass


thr1 = Thread(target=stream_start_test, args=['Thread-1'])
thr2 = Thread(target=influxdb_up, args=['Thread-2'])

thr1.start()
thr2.start()
