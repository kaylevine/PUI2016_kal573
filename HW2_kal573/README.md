# PUI2016 Homework 2


## Project Work Balance:

I completed this assignment working in a group with Mona (nm2773) and Claire (xh895). Mona helped explain pandas, json files, data frames, keys, coding structure and basic coding syntax to Claire and I. Her background in computer science helped me complete these three assignments by explaining which python commands to use and in what order. 

## Assignment 1:

I first wrote my code in a python notebook for testing purposes on Jupyter. Then, I copied my code to a text editor and added code for the 2 arguments. Next, I followed the instructions to test my code in Terminal, which ran successfully.

To begin this assignment, I first imported json, pandas, urllib2, and sys for future use.
I then split the url into different variables that allow a user to input their specific key and the bus line.

```
p1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
key = sys.argv[1]
p2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
busline = sys.argv[2]
url = p1 + key + p2 + busline
```


I then called the mta bus data url, and placed the json information into a data frame for handeling purposes. I also created a bus variale to store data in and use later.
```
response = urllib2.urlopen(url)
json = pd.read_json(response)
df = pd.DataFrame(json)
bus = df["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
```

Next, I defined two functions that return bus latitude and longitude from the json file.
```
def lat(df,x):
    return df[x]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
```
```
def lon(df,x):
    return df[x]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
```
Last, I created the print statements that would allow for user input (arguments) in the Terminal.
```
print "Bus Line: " + busline
print "Number of Active Buses: " + str(len(bus))

for x in range(len(bus)):
    print "Bus %i is at latitude %s and longitude %s" %(x,lat(bus,x),lon(bus,x))
```
## Assignment 2:

Again, I wrote my code in a python notebook for testing purposes on Jupyter. I copied my code to a text editor and added code for the 3 arguments. Next, I followed the instructions to test my code in Terminal, which ran successfully.

To begin assignment 2, I first imported json, pandas, urllib2, and sys for future use.
I then split the url into different variables that allow a user to input their specific key and the bus line. I also added code to allow the user to input the csv file name this code creates.
```
p1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
key = sys.argv[1]
p2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
busline = sys.argv[2]
url = p1 + key + p2 + busline
csvname = sys.argv[3]
```
Similar to assignment 1, I called the url, put the json data into a data frame, created the bus variable, and defined latitude/longitude functions.
```
p1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
key = sys.argv[1]
p2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
busline = sys.argv[2]
url = p1 + key + p2 + busline
csvname = sys.argv[3]

response = urllib2.urlopen(url)
json = pd.read_json(response)
df = pd.DataFrame(json)
bus = df["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

def lat(df,x):
    return df[x]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
def lon(df,x):
    return df[x]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    ```
I then defined two more functions to call Stop Name and Stop Status.
```
def stop(df,x):
    name = df[x]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
    if name <> "":
        return name
    else:
        return "N/A"

def status(df,x):
    stat = df[x]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    if stat <> "":
        return stat
    else:
        return "N/A"
```
In order to create a csv file, I first converted each of the four defined functions into lists using for loops. This enabled my code to collect information for each of the buses in the range.
```
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
```
Last, I created a dictionary from the lists within the data frame, and created a csv file from the results.
```
result_list = pd.DataFrame({'Latitude': latlist, 'Longitude': lonlist, 'Stop Name': stoplist, 'Stop Status': statuslist})
result_list
result_list.to_csv(csvname,index = False)
```

## Assignment 3:

For Assignment 3, I completed the entire coding process in Jupyter notebooks within the CUSP green environment.

The markdown for this assignment is located in the notebook itself.


