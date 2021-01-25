import requests
import csv
import itertools

url = "https://api.spacexdata.com/v3/launches"

# This is where we extract


def getLaunchData(url):
    launch_data = requests.get(url)
    return launch_data.json()

# This is where we transform


def tranformData(launch_data):
    # print(launch_data[0]["mission_name"])
    mission_flight_number = []
    mission_name = []
    mission_image = []
    mission_id = []

    for launch in launch_data:
        mission_flight_number.append(launch["flight_number"])
        mission_name.append(launch["mission_name"])
        mission_image.append(launch["links"]["mission_patch"])
        mission_id.append(launch["mission_id"])

    """ print(len(mission_image))
    print(len(mission_name))
    print(len(mission_id)) """

    with open('rocket_data.csv', 'w', newline='') as data:
        for a, b, c, d in itertools.zip_longest(mission_flight_number, mission_name, mission_image, mission_id, fillvalue="empty"):
            add_data = csv.writer(data)
            add_data.writerow([a, b, c, d])


# This where we load
result = getLaunchData(url)
tranformData(result)
