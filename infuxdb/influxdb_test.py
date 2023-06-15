import time
# importing the required module  
from influxdb import InfluxDBClient  
# defining the host and port  
my_Client = InfluxDBClient(  
    host = '172.25.3.3',  
    port = 8086,  
    username = 'rover',  
    password = "acselab1234",  
    ssl = False,  
    verify_ssl = False  
    ) 
my_Client.switch_database('mydatabase')
json_body = [  
    {
        "measurement": "cputest",
        "tags": {
            # "host": "server01",
            # "region": "us-west"
            "user": "rover003",
            "idcam": "11",
            # "brushId": "6a89f539-71c6-490d-a28d-6c5d84c0ee2fw"
        },
        "fields": {
            "latitude": 14.875359,
            "longitude": 102.0154718,
            "Battery": 100,
            "mode": "auto",
            "door": False,
            "velocity": 0,
        }
    }
]
# for i in range(10):
#     my_Client.write_points(json_body)

# my_Client.close()

try:
    while True:  # loop indefinitely
        print(my_Client.write_points(json_body))
        time.sleep(5)  # pause for 5 seconds
except KeyboardInterrupt:  # allow the user to interrupt the program with Ctrl+C
    my_Client.close()
    print("Stopping program")
finally:
    my_Client.close()