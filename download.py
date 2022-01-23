import json
import requests


def download_camera_positions():
    with open('get_positions.rq') as f:
        query = f.read()
    params = {'query': query, 'format': 'application/sparql-results+json'}
    resp = requests.get('http://dati.camera.it/sparql', params=params)
    data = resp.json()
    with open('positions.json', 'w') as f:
        f.write(json.dumps(data['results']['bindings']))


if __name__ == '__main__':
    download_camera_positions()
