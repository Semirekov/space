from os import makedirs
from os.path import split
from os.path import splitext
from urllib.parse import urlsplit

import requests


def download_file_from_url(url, filename):    
    response = requests.get(url)
    response.raise_for_status()

    dirname = 'images'
    makedirs(dirname, exist_ok=True)
    path = f'{dirname}/{filename}'

    with open(path, 'wb') as file:
        file.write(response.content)        


def get_json_from_api_request(url, params=None):    
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
