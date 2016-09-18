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
csvname = sys.argv[3]

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

#define function to call stop name
def stop(df,x):
    name = df[x]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
    if name <> "":
        return name
    else:
        return "N/A"

#define function to call stop status 
def status(df,x):
    stat = df[x]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    if stat <> "":
        return stat
    else:
        return "N/A"

#create lists for each column of CSV table output
latlist = []
for x in range(len(bus)):
    latlist.append(lat(bus,x))
lonlist = []
for x in range(len(bus)):
    lonlist.append(lon(bus,x))
stoplist = []
for x in range(len(bus)):
    stoplist.append(stop(bus,x))
statuslist = []
for x in range(len(bus)):
    statuslist.append(status(bus,x))

#put lists dictionary, then into data frame
result_list = pd.DataFrame({'Latitude': latlist, 'Longitude': lonlist, 'Stop Name': stoplist, 'Stop Status': statuslist})
result_list

result_list.to_csv(csvname,index = False)