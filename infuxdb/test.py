data = {'control': {'backword': 0, 'forword': 0, 'left': 0, 'right': 0}, 'location': {'rover': {'latitude': 14.875359, 'longitude': 102.0154718, 'rotate': 336}, 'user': {'altitude': 237.30590336490422, 'latitude': 14.875733, 'longitude': 102.015569}}, 'status': {'Battery': 100, 'auto': True, 'door': False, 'idcam': 11, 'status': 0, 'velocity': 1}}


print(data)
print(data["location"]["rover"]["latitude"])
print(data["location"]["rover"]["longitude"])
print(data["location"]["rover"]["rotate"])
print(data["status"]["Battery"])
print(data["status"]["auto"])
print(data["status"]["door"])
print(data["status"]["idcam"])
print(data["status"]["velocity"])