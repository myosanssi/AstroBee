#add you code here!

'''
This is Danah's code
One is for the code to stop after 10 mins
The other is for trimming sig figs
'''
from datetime import datetime, timedelta
from time import sleep

start_time = datetime.now()
now_time = datetime.now()

while (now_time < start_time + timedelta(minutes=9)): #minutes != 10 b/c code could take longer
    print("The rest of the code comes here✨✨")
    sleep(10) #the interval from which the 'hello' gets sent
    now_time = datetime.now()


speed = 7.74686573629 #this is only an example
str_speed = str(speed)
final_speed = str_speed[0:7]
print(final_speed)

'''
this is Arij's code
I will use certain terminology that we will modify once we put everything together
'''
import math
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

def VelocityFormula(distance, time):
  velocity = distance/time
  return velocity
