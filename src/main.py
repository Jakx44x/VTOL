'''main executable for setting up Quadcopter'''
import json
from dronekit import LocationGlobalRelative
from quadcopter import setup_vehicle

def main(configs):
    '''Configure Quadcopter and ready for mission'''
    vehicle = setup_vehicle(configs)

    vehicle.takeoff()

    vehicle.set_altitude(3)

    vehicle.set_altitude(10)

    home = vehicle.location.global_relative_frame

    destination = LocationGlobalRelative(configs["dest"]["lat"],\
        configs["dest"]["long"],\
        configs["dest"]["alt"])

    vehicle.go_to(destination)
    # Pick-up function for ping pong balls

    vehicle.land()

    vehicle.takeoff()

    vehicle.go_to(home)

    vehicle.land()

if __name__ == '__main__':
    with open('configs.json', 'r') as data:
        main(json.load(data))
        