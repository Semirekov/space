import argparse
import os
import os.path

import random
import time

from bot import upload_image


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'pause',
        type=int,
        help='pause in seconds'
    )
    
    return parser


def upload_photos(parent_path = 'images'):

    images = []
    
    for parent_path, dirs, files in os.walk(parent_path):
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            if os.path.getsize(file_path) <= 20_000_000:
                images.append(f'{file_path}')
        
    random.shuffle(images)
    for image in images:
        upload_image(image)        
        time.sleep(2)

        
    
if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()
    
    while True:        
        upload_photos()        
        time.sleep(args.pause)    
