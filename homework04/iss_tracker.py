from flask import Flask
import requests
import xmltodict

app = Flask(__name__)

# To find each entry:
# data['ndm']['oem']['body']['segment']['data']['stateVector'][0]

def get_data() -> dict:
    url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.text) # repsonse.text contains text xml Data
    return data['ndm']['oem']['body']['segment']['data']['stateVector']


@app.route('/', methods = ['GET'])
def get_all() -> dict:
    dataSet = get_data()
    return dataSet

@app.route('/epochs', methods = ['GET'])
def get_epochs() -> list:
    epochs = []
    for d in get_data():
        epochs.append(d['EPOCH'])
    return epochs

@app.route('/epochs/<int:epoch>', methods = ['GET'])
def get_entry(epoch) -> dict:
    data = get_data() 
    return data[int(epoch)]

@app.route('/epochs/<int:epoch>/speed', methods = ['GET'])
def speed_calc(epoch):
    veloList = get_velocity(epoch)
    speed = sum([float(i)**2 for i in veloList])
    return {"speed" : speed}

@app.route('/epochs/<int:epoch>/position', methods = ['GET'])
def get_position(epoch) -> dict:
    epoch_state = get_entry(epoch)
    position = {'X': epoch_state['X']['#text'], 'Y': epoch_state['Y']['#text'], 'Z': epoch_state['Z']['#text']}
    return position

@app.route('/epochs/<int:epoch>/velocity', methods = ['GET'])
def get_velocity(epoch) -> list:
    position = [] # formatted as [X, Y, Z]
    epoch_state = get_entry(epoch)
    position.append(epoch_state['X_DOT']['#text'])
    position.append(epoch_state['Y_DOT']['#text'])
    position.append(epoch_state['Z_DOT']['#text'])
    return position

'''
Notes:
    Make doc strings
    use type hints

    use "try:" and expetion handling for every function 

    make get_velocity return a dict instead of a list

    add query parameters?

'''










if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')