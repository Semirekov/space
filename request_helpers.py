from os import makedirs
from os.path import join
from urllib.parse import urlsplit

import requests


def download_file_from_url(url, filename, dirname='images'):    
    response = requests.get(url)
    response.raise_for_status()
    
    makedirs(dirname, exist_ok=True)    
    path = join(dirname, filename)

    with open(path, 'wb') as file:
        file.write(response.content)        


def get_json_from_api_request(url, params=None):    
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
