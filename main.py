#Libraries/Imports
from datetime import datetime, timedelta
from time import sleep
import math
from picamzero import Camera
from pathlib import Path
from astro_pi_orbit import ISS

base_folder = Path(__file__).parent.resolve()
folder = base_folder
list_speed = []

start_time = datetime.now()
now_time = datetime.now()
number = 0

lat1, lon1, t1 = None, None, None
lat2, lon2, t2 = None, None, None
dis = None
final_speed = "0"

cam = Camera()

iss = ISS()

def get_position():
    point = iss.coordinates()
    return (
        point.latitude.degrees,
        point.longitude.degrees,
        datetime.now().timestamp()
    )
    
def HaversineFormula(lat1, lon1, lat2, lon2):
    '''
    Calculates the shortest distance between two coordinates
    :param lat1: latitude of the first coordinate
    :param long1: longitude of the second coordinate
    :param lat2: latitude of the second coordinate
    :param long2: longitude of the second coordinate
    :return: distance
    '''
    radlat1 = math.radians(lat1)
    radlat2 = math.radians(lat2)
    radlon1 = math.radians(lon1)
    radlon2 = math.radians(lon2)

    dlat = radlat2 - radlat1
    dlon = radlon2 - radlon1

    haversine = math.sin(dlat/2)**2 + math.cos(radlat1) * math.cos(radlat2) * math.sin(dlon/2)**2
    angle = 2 * math.atan2(math.sqrt(haversine), math.sqrt(1-haversine))
    distance = 6371 * angle
    return distance
     
def SpeedFormula(distance, time1, time2):
    '''
    Calculates the speed
    :param distance: distance calculated with the previous function
    :param time1: Unix time of the first picture
    :param time2: Unix time of the second picture
    :return: speed between two coordinates
    '''
    speed = distance / (time2 - time1)
    return speed
    
def average_speed(list_speed):
    '''
    Calculate the average speed from the list
    :param list_speed: the list that contains all the speeds 
    :return: the average speed
    '''
    return sum(list_speed) / len(list_speed)

while (now_time < start_time + timedelta(minutes=9.5)): #minutes != 10 b/c code could take longer
    if number == 0:
       image_path = base_folder / f"imageA.jpg"
    elif number == 1:
        image_path = base_folder / f"imageB.jpg"
    
    cam.take_photo(str(image_path))

    lat, lon, t = get_position()

    if number == 0:
        lat1, lon1, t1 = lat, lon, t
        print(lat1, lon1, t1)
    elif number == 1:
        lat2, lon2, t2 = lat, lon, t
        print(lat2, lon2, t2)

    if lat1 is not None and lat2 is not None and lon1 is not None and lon2 is not None:
        dis = HaversineFormula(lat1, lon1, lat2, lon2)

    if dis is not None and (t2 - t1) > 4:
        speed = SpeedFormula(dis, t1, t2)

        lat1, lon1, t1 = lat2, lon2, t2
        lat2, lon2, t2 = None, None, None
        dis = None
      
        if 6.5 < speed < 8.5:
            list_speed.append(speed)
   
        if len(list_speed) >= 3:
            avg = average_speed(list_speed)
            final_speed = format(avg, ".5g")
            print(final_speed)
   
    sleep(7) #the interval from which the code gets run through
    now_time = datetime.now()

    number = 1 - number

file_path = "result.txt" 
with open(file_path, 'w') as file:
    file.write(final_speed)
