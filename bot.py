import argparse
import asyncio
from os.path import join

import telegram

from utils_env import get_settins


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',        
        help='enter file name'
    )
    
    return parser

async def send_telegram(token, chat_id, file):    
    bot = telegram.Bot(token)
    async with bot:        
        await bot.send_document(
            chat_id=chat_id,
            document=file
        )        


def upload_image(filename, token, chat_id):    
    with open(filename, 'rb') as file:
        asyncio.run(
            send_telegram(token, chat_id, file)
        )


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    
    env = get_settins()
    filename = join(env.dir, args.filename)

    upload_image(
        filename, 
        env.telegram_token, 
        env.chat_id
    )

            


