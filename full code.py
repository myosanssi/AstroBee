#add you code here!
print('test')
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
