import argparse

from utils_env import get_settins
from utils_request import download_file_from_url
from utils_request import get_json_from_api_request
from utils_request import extract_file_ext


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'count',
        nargs='?',
        type=int,
        default=50,
        help='Сколько нужно скачать фото'
    )

    return parser.parse_args()


def download_image(media_url, dirname, index):
    file_ext = extract_file_ext(media_url)
            
    download_file_from_url(
        media_url,             
        dirname,   
        f'nasa_apod_{index:03}{file_ext}'
    )

def get_apod_json(token, count):
    url = f'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count' : count
    }
    
    return get_json_from_api_request(url, params)

def download_only_image(apod_json, dirname):
    for index, media in enumerate(apod_json):
        if media['media_type'] == 'image':        
            download_image(media['url'], dirname, index)      


def fetch_nasa_apod(token, dirname, count):            
    apod_json = get_apod_json(token, count)
    download_only_image(apod_json, dirname)

    

if __name__ == '__main__':    
    args = get_parser_args()    
    env = get_settins()
    fetch_nasa_apod(env.nasa_token, env.dir, args.count)
