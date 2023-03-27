from flask import Flask, request
import redis
import requests
import json

app = Flask(__name__)

def get_redis_client():
    '''
    Returns a redis db client
    '''
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)

rd = get_redis_client()

@app.route('/data', methods = ['GET', 'POST', 'DELETE'])
def handle_data() -> list:
    '''
    Manipulates data wiht 3 different methods with GET, POST, and DELETE method

    Args: None

    Returns: String corresponding to which method was used
        "DELETE" method: deletes all data in redis db
        "POST" method: posts data into redis db
        "GET" method: returns data from redis db
    '''

    method = request.method
    global rd

    if method == 'POST':
        response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        data = response.json()

        for item in data['response']['docs']:
            rd.set(item.get('hgnc_id'), json.dumps(item))
        return f'Data Loaded there are {len(rd.keys())} keys in the db\n'
    

    elif method == 'GET':
        output_list = []
        keys = rd.keys()
        for key in keys:
            output_list.append(json.loads(rd.get(key)))
        return output_list
        

    elif method =='DELETE':
        rd.flushdb()
        return f'data deleted, there are {len(rd.keys())} keys in the db\n'


    else:
        return 'the method you tried is not supported\n'

    return f'method completed \n'


@app.route('/genes', methods = ['GET'])
def get_ids() -> list:
    '''
    Returns json-formatted list of all hgnc_ids

    Args: NONE

    Returns:
        id_list: List of all the hgnc IDs
    '''
    id_list = []

    for key in rd.keys():
        id_list.append(key)

    return(id_list)



@app.route('/genes/<hgnc_id>', methods = ['GET'])
def get_hgnc_data(hgnc_id) -> dict:
    '''
    Return all data associated with <hgnc_id>

    ROUTE: /gene/<hgnc_id>

    Args:
        hgnc_id:    The hgnc ID from the HGNC data set
    
    Returns:
        all data associated with the given hcnc ID

    '''
    if len(rd.keys()) == 0:
        return "Database is empty. Please post data. \n"

    for key in rd.keys():
        if str(key) == str(hgnc_id):
            return json.loads(rd.get(key))

    return "Given ID did not match any IDs in the Data base\n"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
