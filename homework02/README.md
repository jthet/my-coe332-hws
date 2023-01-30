
# Homework 2: "No One JSON" 
### Scenario: You are operating a robotic vehicle on Mars and the task for today is to investigate five meteorite landing sites in Syrtis Major.
#### The objective of this homework was to familiarize us with JSON data structures and how to use them with python.

### Scripts:

`generate_sites.py`:
Creates a dictionary with one key "sites" containing a list, each element in the list being a dictionary containting information about the meteorite landing site. The script then writes out this dictionary to a JSON file. 

`calculate_trip.py`:
Reads the JSON file mentioned above and calculates the distance between each meteroite landing spot, the time it takes to travel, the time it takes to sample meteorites.


### Instructions:
Download all files in homework02 folder and proceed.

#### Step 1: Create meteorite landing data. 
Run `generate_sites.py` with the following command:
``` 
$ python3 generate_sites.py 
```
This will create a JSON file with a dictionary containing meteorite landing data, specifically the ID, latitude, longitude, composition of 5 different meteors. The created file name will be `meteorLanding_sites.json`.
  
  
 #### Step 2: Read Meteorite Data and Analyze
 Run `calculate_trip.py` with the following command:
``` 
$ python3 calculate_trip.py
```
  This will read in the JSON file from step 1, and analyze the data. The data analysis consideres a mars rover moving from a staring position at (lat, long) = (16.0 , 82.0) and moving to each meteroite landing site. This file calculates the time between each landing site or each "leg", as well as the time it takes the rover to sample the metoer. Lastly, it calculates the total number of trips it took, the total time, and the total distance traveled. 
  
This will produce an output similar to the following:
  
 ```
$ python3 calculate_trip.py 
leg = 1, time to travel = 3.58 hours, time to sample 2 hours
leg = 2, time to travel = 9.06 hours, time to sample 1 hours
leg = 3, time to travel = 4.54 hours, time to sample 1 hours
leg = 4, time to travel = 1.57 hours, time to sample 2 hours
leg = 5, time to travel = 9.05 hours, time to sample 3 hours
number of legs = 5, total time elapsed = 36.80 hours, total distance = 278.015 km
```
#### Method 2:
Run the following command to combine the previous two steps and work through testing faster:
```
$ python3 generate_sites.py && python3 calculate_trip.py 
```
