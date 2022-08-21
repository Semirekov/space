import argparse
import os
from os.path import split
from os.path import splitext

from urllib.parse import urlsplit

from dotenv import load_dotenv

from request_helpers import download_file_from_url
from request_helpers import get_json_from_api_request


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'count',
        nargs='?',
        type=int,
        default=50,
        help='Сколько нужно скачать фото'
    )

    return parser

    
def fetch_nasa_apod(token, count):        
    url = f'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count' : count
    }
    
    response_json = get_json_from_api_request(url, params)

    for index, media in enumerate(response_json):
        if media['media_type'] == 'image':            
            media_url = media['url']
            
            path_dir, file_name = split(
                urlsplit(media_url).path
            )
            file_name, file_ext = splitext(file_name)
            
            download_file_from_url(
                media_url,
                f'nasa_apod_{index:03}{file_ext}'
            )


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    
    load_dotenv()    
    fetch_nasa_apod(os.environ['NASA_TOKEN'], args.count)
