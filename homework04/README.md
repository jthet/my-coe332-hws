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
To run the flask application:
```
$ flask --app iss_tracker --debug run 
```
This should output the following prompt:

```
$ flask --app iss_tracker --debug run 
 * Serving Flask app 'iss_tracker'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-861-049

```

#### Step 2: Use the Flask app
Each route can be accesd with the following:
```
$ curl localhost:5000/ [ROUTE]
```


All of the routes and example output are shown below.

Route: `/`
```
$ curl localhost:5000/
              .
              .
              .
 {
    "EPOCH": "2023-063T12:00:00.000Z",
    "X": {
      "#text": "2820.04422055639",
      "@units": "km"
    },
    "X_DOT": {
      "#text": "5.0375825820999403",
      "@units": "km/s"
    },
    "Y": {
      "#text": "-5957.89709645725",
      "@units": "km"
    },
    "Y_DOT": {
      "#text": "0.78494316057540003",
      "@units": "km/s"
    },
    "Z": {
      "#text": "1652.0698653803699",
      "@units": "km"
    },
    "Z_DOT": {
      "#text": "-5.7191913150960803",
      "@units": "km/s"
    }
  }
]
```


Route: `/epochs`
```
$ curl localhost:5000/epochs
              .
              .
              .
  "2023-063T11:43:00.000Z",
  "2023-063T11:47:00.000Z",
  "2023-063T11:51:00.000Z",
  "2023-063T11:55:00.000Z",
  "2023-063T11:59:00.000Z",
  "2023-063T12:00:00.000Z"
]
```

Route: `/epochs/<int:epoch>`
```
$ curl localhost:5000/epochs/1

{
  "EPOCH": "2023-048T12:04:00.000Z",
  "X": {
    "#text": "-5998.4652356788401",
    "@units": "km"
  },
  "X_DOT": {
    "#text": "-2.8799691318087701",
    "@units": "km/s"
  },
  "Y": {
    "#text": "391.26194859011099",
    "@units": "km"
  },
  "Y_DOT": {
    "#text": "-5.2020406581448801",
    "@units": "km/s"
  },
  "Z": {
    "#text": "-3164.26047476555",
    "@units": "km"
  },
  "Z_DOT": {
    "#text": "4.8323394499086101",
    "@units": "km/s"
  }
}
```


Route: `/epochs/1/position`
```
$ curl localhost:5000/epochs/1/position
{
  "X (km)": "-5998.4652356788401",
  "Y (km)": "391.26194859011099",
  "Z (km)": "-3164.26047476555"
}
```

Route: `/epochs/1/velocity`
```
$ curl localhost:5000/epochs/1/velocity
[
  "-2.8799691318087701",
  "-5.2020406581448801",
  "4.8323394499086101"
]
```


Route: `/epochs/1/speed`
```
$ curl localhost:5000/epochs/1/speed
{
  "speed (km/s)": 58.70695376830683
}
```


