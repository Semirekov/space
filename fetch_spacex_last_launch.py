import argparse

from request_helpers import download_file_from_url
from request_helpers import get_json_from_api_request

def fetch_spacex_last_launch(launch='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{launch}'
           
    request_json = get_json_from_api_request(url)
    images = request_json['links']['flickr']['original']
    
    for index, image in enumerate(images):    
        download_file_from_url(
            image,
            f'space_{index:03}.jpg'
        )


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'launch',
        nargs='?',
        help='ID SpaceX launch'
    )
    
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    
    fetch_spacex_last_launch(args.launch)
