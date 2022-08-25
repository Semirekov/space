import argparse
from datetime import datetime
import os
import os.path

import random
import time

import telegram

from bot import upload_image
from utils_env import get_settins
from utils_file import get_file_names


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'pause', 
        type=int, 
        default=14400,
        help='pause in seconds'
    )
    
    return parser.parse_args()


def is_valid_size(file_path, valid_size=20_000_000):
    return os.path.getsize(file_path) <= valid_size


def upload_photos(parent_path, token, chat_id):
    images = get_file_names(parent_path)    
    random.shuffle(images)

    for image in images:
        if is_valid_size(image):
            upload_image(image, token, chat_id)        
            time.sleep(2)
        

        
    
if __name__ == '__main__':    
    args = get_parser_args()
    env = get_settins()

    try_connect_count = 0
    sleep_time, sleep_time_max = 30, 240       

    while True:
        try:
            upload_photos(env.dir, env.telegram_token, env.chat_id)            
            time.sleep(args.pause)
        except telegram.error.TimedOut:
            try_connect_count += 1
            now = datetime.now()            
            print(try_connect_count, 'Ошибка подключения: ', now.strftime("%d-%m-%Y %H:%M:%S"))
            
            if try_connect_count > 1:                                            
                time.sleep(sleep_time)
                if sleep_time < sleep_time_max:
                    sleep_time *= 2

            
            
