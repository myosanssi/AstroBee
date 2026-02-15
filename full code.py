#Libraries/Imports
from datetime import datetime, timedelta #Danah & Noah
from exif import Image #Noah
import os #Noah
from time import sleep #Danah
import math #Arij
from picamzero import Camera

folder = base_folder
results = []
list_speed = []

start_time = datetime.now()
now_time = datetime.now()
number = 0

while (now_time < start_time + timedelta(minutes=9.8)): #minutes != 10 b/c code could take longer
   cam = Camera()
   if number == 0:
      image_path = base_folder / f"imageA.jpg"
   elif number == 1:
      image_path = base_folder / f"imageB.jpg"
   cam.take_photo(str(image_path))

   def dms_to_decimal(dms):
      '''
      Takes degrees, minutes, and seconds and converts them to decimals
      :param dms: degrees, minutes, and seconds from the coordinates of the images
      :return: dsm in decimals
      '''
      degrees, minutes, seconds = dms
      return degrees + minutes / 60 + seconds / 3600
   
   def extract_data(image_path):
      '''
      Extracts data from images
      :param image_path: the file path to the image
      :return: latitude, longitude, and Unix time
      '''
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

   for filename in os.listdir(folder):
      if filename.endswith(".jpg") or filename.endswith(".JPG"):
         full_path = os.path.join(folder, filename)
         lat, lon, time = extract_data(full_path)
         results.append((filename, lat, lon, time))
  
   def get_time(data):
      '''
      Gives the time from a picture's data
      :param data: choosing the picture's data
      :returns: the time the picture was taken
      '''
      return data[3]
   results.sort(key=get_time)

   if len(results) == 2:
      data1 = results[0]
      lat1 = data1[1]
      long1 = data1[2]
      time1 = data1[3]
      
      data2 = results[1]
      lat2 = data2[1]
      long2 = data2[2]
      time2 = data2[3]
      
      def HaversineFormula(lat1, long1, lat2, long2):
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
         radlong1 = math.radians(long1)
         radlong2 = math.radians(long2)
            
         dlat = radlat2 - radlat1
         dlong = radlong2 - radlong1
            
         haversine = math.sin(dlat/2)**2 + math.cos(radlat1) * math.cos(radlat2) * math.sin(dlong/2)**2
         angle = 2 * math.atan2(math.sqrt(haversine),math.sqrt(1-haversine))
         distance = 6371 * angle
            
         return distance

      dis = HaversineFormula(lat1, long1, lat2, long2)
      
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

      speed = SpeedFormula(dis, time1, time2)
      
      results.pop(0)
      
      def into_the_list(speed):
         '''
         get the speeds from "SpeedFormula" and add them to the list called "list_speed"
         :param speed: the calculated speed of the ISS
         :return: the list of the speed ("list_speed")
         '''
         list_speed.append(speed)
      
      into_the_list(speed)
         
      def average_speed(list_speed):
         '''
         calculate the average speed from the list
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
