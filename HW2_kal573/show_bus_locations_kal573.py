# Set working environment
import json
import pandas as pd
import urllib2
import sys

#define url and variables
p1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
key = sys.argv[1]
p2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
busline = sys.argv[2]
url = p1 + key + p2 + busline

#call url, read json file, create data frame, open json file within data frame
response = urllib2.urlopen(url)
json = pd.read_json(response)
df = pd.DataFrame(json)
bus = df["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

#define function to call bus latitude and longitude (locations)

def lat(df,x):
    return df[x]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
def lon(df,x):
    return df[x]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]

print "Bus Line: " + busline
print "Number of Active Buses: " + str(len(bus))

#create for loop to print each bus location
for x in range(len(bus)):
    print "Bus %i is at latitude %s and longitude %s" %(x,lat(bus,x),lon(bus,x))

