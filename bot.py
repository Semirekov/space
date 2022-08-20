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


async def upload_file(token, chat_id, filename):    
    bot = telegram.Bot(token)
    async with bot:        
        await bot.send_document(
            chat_id=chat_id,
            document=open(filename, 'rb')
        )        


def upload_image(filename):    
    load_dotenv()    
    asyncio.run(
        upload_file(
            os.environ['TELEGRAM_TOKEN'],
            os.environ['CHAT_ID'],
            filename
        )
    )


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    load_dotenv()    
    asyncio.run(
        upload_file(
            os.environ['TELEGRAM_TOKEN'],
            os.environ['CHAT_ID'],
            args.filename
        )
    )


