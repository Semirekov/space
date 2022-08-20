import argparse
import asyncio
import os

from dotenv import load_dotenv
import telegram


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',        
        help='enter file name'
    )
    
    return parser


async def upload_file(token, filename):
    
    bot = telegram.Bot(token)
    async with bot:        
        await bot.send_document(chat_id='@spacefanat', document=open(filename, 'rb'))        


def upload_image(filename):    
    load_dotenv()    
    asyncio.run(
        upload_file(os.environ['TELEGRAM_TOKEN'], filename)
    )


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    load_dotenv()    
    asyncio.run(
        upload_file(os.environ['TELEGRAM_TOKEN'], args.filename)
    )


