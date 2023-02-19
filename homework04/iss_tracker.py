from flask import Flask
import requests
import xmltodict

app = Flask(__name__)

# Gets usefull date (only data -> stateVectors)
def get_data() -> dict:
    """
    Retrieves the data from the nasa published ISS location coordinates, converts from XML to a dictionary, and returns the 
    Valuable data concering the ISS position and velocity at different times. 

    Args:
        None

    Returns:
        data (dict): the ISS stateVectors at different epochs
    """

    url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.text) # repsonse.text contains text xml Data
    return data['ndm']['oem']['body']['segment']['data']['stateVector']

# Base url, returns dict of all data
@app.route('/', methods = ['GET'])
def get_all() -> dict:
    """
    Returns all epochs for the entire data set of the ISS state vectors. Decorated with the app route "<baseURL>/"

    Args:
        None
    Returns:
        dataSet (dict): Dictionary of all epochs and corresponding state Vectors of the ISS
    """
    dataSet = get_data()
    return dataSet

@app.route('/epochs', methods = ['GET'])
def get_epochs() -> list:
    """
    Returns all the epochs in the data set, without the state Vectors. 
    Decorated with the app route "<baseURL>/epochs"
    Args:
        None
    Returns:
        epochs (list): A list of all the epochs (time stamps) in the data set. 
    """

    epochs = []
    for d in get_data():
        epochs.append(d['EPOCH'])
    return epochs

@app.route('/epochs/<int:epoch>', methods = ['GET'])
def get_entry(epoch: str) -> dict:
    """
    Given an epoch, returns the state vectors associated with that specific epoch.
    Decorated with the app route "<baseURL>/epochs/<epoch>"

    Args:
        epoch (string): returns a string representing the epoch entry index number as an int. 
            - Note: epoch is given as a string but is converted to and used as a integer to index a list. 

    Returns:
        data[int(epoch)] (dict): returns the given index "epoch" of the data list from the full data set 
    """
    # Every other function calls this function so this the only error checking we need

    try: 
        epoch = int(epoch)
    except ValueError
        return "Error: Epoch must be an integer"

    data = get_data() 
    return data[int(epoch)]

@app.route('/epochs/<int:epoch>/speed', methods = ['GET'])
def speed_calc(epoch: str) -> dict:
    """
    Given an epoch, returns the speed of the ISS at that specific epoch. 
    Speed is calculated from the X, Y, and Z velocities given in the data set. 
    
    Args:
        epoch (string): returns a string representing the epoch entry index number as an int. 
            - Note: epoch is given as a string but is converted to and used as a integer to index a list. 

    Returns:
        {"speed" : speed} (dict): returns the speed of a given index "epoch"
    """

    veloList = get_velocity(epoch)
    speed = sum([float(i)**2 for i in veloList])
    return {"speed" : speed}

@app.route('/epochs/<int:epoch>/position', methods = ['GET'])
def get_position(epoch: str) -> dict:
    """
    Given an epoch, returns the position of the ISS at that specific epoch. 
    Position is given as the the X, Y, and Z positional coordinates. 
    
    Args:
        epoch (string): returns a string representing the epoch entry index number as an int. 
            - Note: epoch is given as a string but is converted to and used as a integer to index a list. 

    Returns:
        position (dict): returns the X, Y, and Z positional coordinates of a given index "epoch"
    """


    epoch_state = get_entry(epoch)
    position = {'X': epoch_state['X']['#text'], 'Y': epoch_state['Y']['#text'], 'Z': epoch_state['Z']['#text']}
    return position

@app.route('/epochs/<int:epoch>/velocity', methods = ['GET'])
def get_velocity(epoch: str) -> list:
    """
    Given an epoch, returns the velocity of the ISS at that specific epoch. 
    Velocity is given as the X, Y, and Z velocities. 
    
    Args:
        epoch (string): returns a string representing the epoch entry index number as an int. 
            - Note: epoch is given as a string but is converted to and used as a integer to index a list. 

    Returns:
        velo (list): returns the X, Y, and Z velocity of a given index "epoch"
    """

    velo = [] # formatted as [X, Y, Z]
    epoch_state = get_entry(epoch)
    velo.append(epoch_state['X_DOT']['#text'])
    velo.append(epoch_state['Y_DOT']['#text'])
    velo.append(epoch_state['Z_DOT']['#text'])
    return velo





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')