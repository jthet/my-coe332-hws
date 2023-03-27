# Homework 6: "Say It Ain’t Genes" 
#### Scenario:
We are going to turn our attention to a brand new dataset. The Human Genome Organization (HUGO) is a non-profit which oversees the HUGO Gene Nomenclature Committee (HGNC). The HGNC “approves a unique and meaningful name for every gene”. For this homework, we will download the complete set of HGNC data and inject it into a Redis database through a Flask interface.

#### Objective:
Combine redis and flask. 

### Data:
The data for this homework set is a JSON file that contains information on genes found in the human genome, approved by the HGNC (HUGO Genome Nomenclature Committee). The HGNC sets standards for human gene nomenclature. 

This data set holds information on all the HGNC recocgnized genes.

The data can be viewed here: [HGNC Data](https://www.genenames.org/download/archive/).



# WIP

### Scripts:

`gene_api.py`:
Flask application for querying the genome data. The application should loads in the data mentioned above and provides flask routes for a user to digest the data and find specific data points and associated values.
The routes and returns are as follows.


| Route         | Method        | Return |
| ------------- |:-------------:| ------------- |
| `/data`     | GET | Return all data in Redis database | 
| | DELETE |  Delete data in Redis | 
| | POST | Put data into Redis | 
| `/genes`    | GET |  Returns the unique hgnc_id of all the genes in the data set      |
| `/genes/<hgnc_id>`  | GET |  Return all data associated with a specific hgnc_id |



** Note: the variable `<hgnc_id>` takes the format "HGNC:1234", where 1234 is replaced with the unique ID number.



`Dockerfile`: Text document that contains the commands to assemble the `gene_api` Docker image that is used to produce the Docker container when ran. 

`docker-compose.yaml`: YAML script that orchestrates the containerization and port mapping of the flask app and redis database.

### Instructions and Installation:

#### IMPORTANT NOTE:
Before any use, it is required that an empty folder named "data" is created by the user, so that the user has writing priveleges.
This can be done with the following command:
```
$ mkdir data
```

#### Method 1: Launch the containerized app and Redis using docker-compose (strongly preffered)

Use the command 

```
$ docker-compose up
Starting homework06_redis-db_1 ... done
.
.
.
flask-app_1  |  * Debugger is active!
flask-app_1  |  * Debugger PIN: 411-831-197
```
This will create 2 containers; the flask app and the redis database/

Check these containers exist with:
```
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED              STATUS              PORTS                                       NAMES
9df1e28ee08e   jthet/gene_api:1.0   "python3 /gene_api.py"   About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   homework06_flask-app_1
d00467cc9354   redis:7              "docker-entrypoint.s…"   3 hours ago          Up About a minute   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   homework06_redis-db_1

```

You can now use the flask-redis api through curl: see the "Running the Flask App" section

To close the containers use the command:

```
$ docker-compose down
Stopping homework06_flask-app_1 ... done
Stopping homework06_redis-db_1  ... done
Removing homework06_flask-app_1 ... done
Removing homework06_redis-db_1  ... done
Removing network homework06_default
```

#### Method 2: Pull and use your existing image from Docker Hub

To use the existing Docker Image run the following commands:
```
$ docker pull jthet/gene_api:1.0
```
This will add the image to the users docker images, which can be checked with the command 
```
$ docker images
REPOSITORY            TAG       IMAGE ID       CREATED         SIZE
jthet/gene_api        1.0       c8b0a0825328   4 hours ago     899MB
```
Next, set up the redis data base with the following command:

```
$ docker run -d -p 6379:6379 -v </path/on/host>:/data redis:7 --save 1 1
```
For example:
```
$ docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw redis:7 --save 1 1
9e18a9279d4950a3f05b16 ...
```
This will create a containerized image of redis and map ports 6379 inside the container to port 6379 of the host.
This also tells redis to save every 1 second and keep only 1 backup in memory. 

Once the redis container is running, the flask app container image can be run with the command
```
$ docker run -it --rm -p 5000:5000 jthet/gene_api:1.0 
```

This will simultaneously open the flask app and redis database in a container. Skip to step 2 of method 2 below to see how to use the flask app. 



*Note this method will not work with the existing image as the host name of the flask app is set to match docker-compose's host name for redis of 'redis-db'.*

*For this reason, either the redis client host name must be changed from "host = 'redis-rd'" to "host = 0.0.0.1"*

*It is recommened to just use method 1*




#### Method 3: Build a new image from your Dockerfile
To build a new image from the existing Dockerfile, execute the following commands:
Note: Dockerfile must be in the current directory when this command is executed.
```
$ docker build -t <dockerhubusername>/<code>:<version> .
```
Example:
```
$ docker build -t jthet/gene_api:1.0 .
Sending build context to Docker daemon   7.68kB
Step 1/4 : FROM python:3.8.10
 ---> a369814a9797
Step 2/4 : RUN pip install Flask==2.2.0 redis requests
 ---> Using cache
 ---> 20dabd1acd2c
Step 3/4 : ADD ./gene_api.py /gene_api.py
 ---> 76fe0eec9b92
Step 4/4 : CMD ["python3", "/gene_api.py"]
 ---> Running in fe2c0f85b0db
Removing intermediate container fe2c0f85b0db
 ---> ba3e81e8f47f
Successfully built ba3e81e8f47f
Successfully tagged jthet/gene_api:1.0
```

Check the image was built with `$ docker images`:
```
$ docker images
REPOSITORY                 TAG        IMAGE ID       CREATED              SIZE
jthet/gene_api             1.0        2883079fad18   About a minute ago   928MB

```

Next, set up the redis data base with the following command:

```
$ docker run -d -p 6379:6379 -v </path/on/host>:/data redis:7 --save 1 1
```
For example:
```
$ docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw redis:7 --save 1 1
9e18a9279d4950a3f05b16 ...
```
This will create a containerized image of redis and map ports 6379 inside the container to port 6379 of the host.
This also tells redis to save every 1 second and keep only 1 backup in memory.

Run the image with the following:
```
$ docker run -it --rm -p 5000:5000 jthet/gene_api:1.0
```
This will open the flask app in a new container.



### Running the Flask App

#### After the container is built and the Flask app is running:
This should output the following prompt:

```
$ docker run -it --rm -p 5000:5000 jthet/iss_tracker:hw05
 * Serving Flask app 'iss_tracker'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-861-049
```

#### Using the Flask app
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

Route: `/help`
```
$ curl localhost:5000/help

HERE IS A HELP MESSAGE FOR EVERY FUNCTION/ROUTE IN "iss_tracker.py"

get_data:

    Retrieves the data from the nasa published ISS location coordinates, converts from XML to a dictionary, and returns the 
    Valuable data concering the ISS position and velocity at different times. 

    Route: None, only used to retreive data for other routes

    Args:
        None

    Returns:
        data (dict): the ISS stateVectors at different epochs
    

get_all:

    Returns all epochs for the entire data set of the ISS state vectors. Decorated with the app route "<baseURL>/"

    Route: <baseURL>/

    Args:
        None

    Returns:
        dataSet (dict): Dictionary of all epochs and corresponding state Vectors of the ISS
    
```

Route: `/delete-data` (Must use `-X DELETE` tag)
```
$ curl -X DELETE localhost:5000/delete-data
Data is deleted
```

Route: `/post-data` (Must use `-X POST` tag)
```
$ curl -X POST localhost:5000/post-data
Data is posted
```


### Query Parameters
The route `/epochs` has 2 query paramaters: "limit" and "offset" 

The offset query parameter should offset the start point by an integer. For example, `offset=0` would begin printing at the first Epoch, `offset=1` would begin printing at the second Epoch, etc. The limit query parameter controls how many results are returned. For example `limit=10` would return 10 Epochs, `limit=100` would return 100 Epochs, etc. Putting them together, the route `/epochs?limit=20&offset=50` would return Epochs 51 through 70 (20 total).

Example:
```
$ curl 'localhost:5000/epochs?limit=4&offset=20'
{
  "21": "2023-055T13:20:00.000Z",
  "22": "2023-055T13:24:00.000Z",
  "23": "2023-055T13:28:00.000Z",
  "24": "2023-055T13:32:00.000Z"
}
```
