#Libraries/Imports
from datetime import datetime, timedelta #Danah & Noah
from exif import Image #Noah
import os #Noah
from time import sleep #Danah
import math #Arij

# Noah's code!
def dms_to_decimal(dms):
    degrees, minutes, seconds = dms
    return degrees + minutes / 60 + seconds / 3600

def extract_data(image_path):
    with open(image_path, 'rb') as image_file:
        img = Image(image_file)

        latitude = dms_to_decimal(img.gps_latitude)
        longitude = dms_to_decimal(img.gps_longitude)

        dt = datetime.strptime(
            img.datetime_original,
            "%Y:%m:%d %H:%M:%S"
        )
        unix_time = dt.timestamp()

        return latitude, longitude, unix_time
    
#    lat, lon, time = extract_data("ExamplePhotos/image1.jpg")
#   print("latitude:", lat)
#   print("longitude:", lon)
#   print("time:", time)


# loop:

folder = "ExamplePhotos"
results = []

for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".JPG"):

        full_path = os.path.join(folder, filename)

        lat, lon, time = extract_data(full_path)
        results.append((filename, lat, lon, time))

# for testing:

        print(filename)
        print("Latitude:", lat)
        print("Longitude:", lon)
        print("Time:", time)
        print("------")

# for list (results):

        print(results)


'''
this is Arij's code
I will use certain terminology that we will modify once we put everything together
'''
if len(results) == 2:
    def HaversineFormula(lat1, long1, lat2, long2):
        radlat1 = math.radians(lat1)
        radlat2 = math.radians(lat2)
        radlong1 = math.radians(long1)
        radlong2 = math.radians(long2)
        
        dlat = radlat2 - radlat1
        dlong = radlong2 - radlong1
        
        haversine = math.sin(dlat/2)**2 + math.cos(radlat1) * math.cos(radlat2) * math.sin(dlong/2)**2
        angle = 2 * math.atan2(math.sqrt(haversine),math.sqrt(1-haversine))
        distance = 6371 * angle
        
        return distance
    def SpeedFormula(distance, time):
        speed = distance/time
        return speed
    
    results.pop(0)

'''
This is Yui's code
That averages velocities & appends them to a list
'''
list_speed = []
def into_the_list(speed):
    '''
    variable: the calculated speed of the ISS
    get the speed from the other function and add it one by one to the list called "list_speed"
    '''
    list_speed.append(speed)

def average_speed(list_speed):
    '''
    variable: the list that contains all the speed
    calculate the average speed from the list
    '''
    sum_speed = 0
    for num in list_speed:
        sum_speed += num
    average_speed = float(sum_speed/len(list_speed))
    return speed

 average_speed(list_speed)

'''
This is Danah's code
One is for the code to stop after 10 mins
The other is for trimming sig figs
'''
start_time = datetime.now()
now_time = datetime.now()

while (now_time < start_time + timedelta(minutes=9)): #minutes != 10 b/c code could take longer
    print("The code comes here✨✨")
    sleep(0.5) #the interval from which the code gets run through
    now_time = datetime.now()

#Danah's code
str_average_speed = str(average_speed)
final_speed = str_average_speed[0:7]
print(final_average_speed)

file_path = "result.txt" 
with open(file_path, 'w') as file:
    file.write(final_speed)

print("Data written to", file_path)
