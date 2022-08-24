from datetime import datetime

from utils_env import get_settins
from utils_request import download_file_from_url
from utils_request import get_json_from_api_request


def get_epic_json(token):
    url = f'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': token
    }
    
    return get_json_from_api_request(url, params)


def get_valid_url(image):
    img_name = image['image']

    img_date = datetime.fromisoformat(image['date'])
    img_date = img_date.strftime("%Y/%m/%d")                  
    return f'https://epic.gsfc.nasa.gov/archive/natural/{img_date}/png/{img_name}.png'    


def fetch_nasa_epic(token, dirname):   
    response_json = get_epic_json(token)

    for index, image in enumerate(response_json):
        url = get_valid_url(image)                
        download_file_from_url(url, dirname, f'nasa_epic_{index:02}.png')        


if __name__ == '__main__':
    env = get_settins()
    fetch_nasa_epic(env.nasa_token, env.dir)
