import requests
import csv

url = "https://api.spacexdata.com/v3/launches"

# This is where we extract


def getLaunchData(url):
    launch_data = requests.get(url)
    return launch_data.json()

# This is where we transform


def tranformData(launch_data):
    # print(launch_data[0]["mission_name"])
    mission_name = []
    mission_image = []
    mission_id = []

    for launch in launch_data:
        mission_name.append(launch["mission_name"])
        mission_image.append(launch["links"]["mission_patch"])
        mission_id.append(launch["flight_number"])

    """ print(len(mission_image))
    print(len(mission_name))
    print(len(mission_id)) """

    with open('rocket_data.csv', 'w', newline='') as data:
        for a, b, c in zip(mission_id, mission_name, mission_image):
            add_data = csv.writer(data)
            add_data.writerow([a, b, c])


# This where we load
result = getLaunchData(url)
tranformData(result)
