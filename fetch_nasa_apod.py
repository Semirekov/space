import os
from os.path import split
from os.path import splitext

from urllib.parse import urlsplit

from dotenv import load_dotenv

from request_helpers import download_file_from_url
from request_helpers import get_json_from_api_request


def fetch_nasa_apod(token):        
    url = f'https://api.nasa.gov/planetary/apod?api_key={token}'
    
    response_json = get_json_from_api_request(
        url,
        {'count' : 50}
    )

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
    load_dotenv()    
    fetch_nasa_apod(os.environ['NASA_TOKEN'])
