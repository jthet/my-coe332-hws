# Homework 4: "Buddy Flask" 
### Scenario: Scenario: You have found an abundance of interesting positional and velocity data for the International Space Station (ISS). It is a challenge, however, to sift through the data manually to find what you are looking for. Your objective is to build a Flask application for querying and returning interesting information from the ISS data set.

#### Objective: Gain familiarity with flask. 

### Data:
The data for this homework set is a XML file that contains information on the state Vectors of the ISS at different epochs (points in time). The data can be viewed here: [ISS Public Data](https://spotthestation.nasa.gov/trajectory_data.cfm).

The Data is read in as XML and converted to a python dictionary with the module `xmltodict`



### Scripts:

`iss_tracker.py`:
Flask application for querying the ISS position and velocity. The application should loads in the data mentioned above and provides flask routes for a user to digest the data and find specific data points and values associated with specific data points.
The routes and returns are as follows


Colons can be used to align columns.

| Route         | Return        | 
| ------------- |:-------------:| 
| `/`     | returns full data set | 
| `/epochs`       | returns all epochs in the data set      |
| `/epochs/<int:epoch>`  | returns all the data (state vectors) associated with a specific epoch      |
| `/epochs/<int:epoch>/position`  | returns the positional coordinates of a specific epoch     |
| `/epochs/<int:epoch>/velocity`  | returns the velocity of a specific epoch        |
| `/epochs/<int:epoch>/speed`  | returns the speed of a specific epoch      |



### Instructions and Instalation:
Download all files in homework04 folder and proceed.
Note: flask, requests and xmltodict need to be installed. 
To install: 
```
$ pip3 install (flask/requests/xmltodict)
```

#### Step 1: Run the Flask app 
To run the app, start the 
