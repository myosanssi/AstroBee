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

cam = Camera()

iss = ISS()

def get_position():
    point = iss.coordinates()
    return (
        point.latitude.degrees,
        point.longitude.degrees,
        datetime.now().timestamp()
    )


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
        angle = 2 * math.atan2(math.sqrt(haversine),math.sqrt(1-haversine))
        distance = 6371 * angle
            
        return distance

    if lat1 is not None and lat2 is not None and lon1 is not None and lon2 is not None:
        dis = HaversineFormula(lat1, lon1, lat2, lon2)

    def SpeedFormula(distance, time1, time2):
        '''
        Calculates the speed
        :param distance: distance calculated with the previous function
        :param time1: Unix time of the first picture
        :param time2: Unix time of the second picture
        :return: speed between two coordinates
        '''
        speed = distance/(time2 - time1)
        return speed

    if dis != None:
        speed = SpeedFormula(dis, t1, t2)
      
        def into_the_list(speed):
            '''
            Get the speeds from "SpeedFormula" and add them to the list called "list_speed"
            :param speed: the calculated speed of the ISS
            :return: the list of the speed ("list_speed")
            '''
            list_speed.append(speed)
      
        into_the_list(speed)
         
        def average_speed(list_speed):
            '''
            Calculate the average speed from the list
            :param list_speed: the list that contains all the speeds 
            :return: the average speed
            '''
            sum_speed = 0
            for num in list_speed:
                sum_speed += num
                average_speed = float(sum_speed/len(list_speed))
            return average_speed
   
        final_speed = "{:.4g}".format(average_speed(list_speed))
        print(final_speed)
   
    sleep(0.5) #the interval from which the code gets run through
    now_time = datetime.now()

    number = 1 - number

file_path = "result.txt" 
with open(file_path, 'w') as file:
    file.write(final_speed)
