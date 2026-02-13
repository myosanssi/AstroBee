#add you code here!
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
    print(f'The average speed is {average_speed}')

 average_speed(list_speed)

'''
This is Danah's code
One is for the code to stop after 10 mins
The other is for trimming sig figs
'''
import datetime
from time import sleep

start_time = datetime.now()
now_time = datetime.now()

while (now_time < start_time + timedelta(minutes=9)): #minutes != 10 b/c code could take longer
    print("The rest of the code comes here✨✨")
    sleep(10) #the interval from which the 'hello' gets sent
    now_time = datetime.now()

str_average_speed = str(average_speed)
final_speed = str_average_speed[0:7]
print(final_average_speed)

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
