import os
from os.path import split
from os.path import splitext

from urllib.parse import urlsplit

from dotenv import load_dotenv

from request_helpers import download_file_from_url
from request_helpers import get_json_from_api_request

def fetch_nasa_epic(token):
    url = f'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': token
    }
    
    response_json = get_json_from_api_request(url, params)

    for index, images in enumerate(response_json):
        img_name = images['image']
        imp_day, img_time = images['date'].split()
        img_date = imp_day.replace('-', '/')
                
        img_url = f'https://epic.gsfc.nasa.gov/archive/natural/{img_date}/png/{img_name}.png'
                
        download_file_from_url(
            img_url, 
            f'nasa_epic_{index:02}.png'
        )


if __name__ == '__main__':
    load_dotenv()    
    fetch_nasa_epic(os.environ['NASA_TOKEN'])
