import argparse
from datetime import datetime
import os
import os.path

import random
import time

import telegram

from bot import upload_image


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'pause',
        type=int,
        help='pause in seconds'
    )
    
    return parser


def append_images(parent_path, files):
    images = []    
    for file_name in files:
        file_path = os.path.join(parent_path, file_name)
        if os.path.getsize(file_path) <= 20_000_000:
            images.append(f'{file_path}')

    return images

                
def upload_photos(parent_path = 'images'):

    images = []    
    for parent_path, dirs, files in os.walk(parent_path):
        images += append_images(parent_path, files)
        
    random.shuffle(images)
    for image in images:
        upload_image(image)        
        time.sleep(2)

        
    
if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()
    try_connect_count = 0
    sleep_time = 30
    sleep_time_limit = 240
    
    while True:
        try:
            upload_photos()        
            time.sleep(args.pause)
        except telegram.error.TimedOut:
            try_connect_count += 1
            now = datetime.now()            
            print(try_connect_count, 'Ошибка подключения: ', now.strftime("%d-%m-%Y %H:%M:%S"))
            
            if try_connect_count == 1:                
                continue
            
            time.sleep(sleep_time)
            if sleep_time < sleep_time_limit:
                sleep_time *= 2

            
            
