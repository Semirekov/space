import argparse

from utils_env import get_settins
from utils_request import download_file_from_url
from utils_request import get_json_from_api_request


def get_image_links(launch):
    url = f'https://api.spacexdata.com/v5/launches/{launch}'
           
    request_json = get_json_from_api_request(url)
    return request_json['links']['flickr']['original']


def download_images(image_links, dirname):
    for index, link in enumerate(image_links):    
        download_file_from_url(link, dirname,f'space_{index:03}.jpg')


def fetch_spacex_last_launch(launch, dirname):    
    image_links = get_image_links(launch)
    download_images(image_links, dirname)
    

def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'launch',
        nargs='?',
        default='latest',
        help='ID SpaceX launch'
    )

    return parser.parse_args()
    

if __name__ == '__main__':    
    args = get_parser_args()
    env = get_settins()
    fetch_spacex_last_launch(args.launch, env.dir)
