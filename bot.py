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


async def upload_file(token, chat_id, file):    
    bot = telegram.Bot(token)
    async with bot:        
        await bot.send_document(
            chat_id=chat_id,
            document=file
        )        


def upload_image(filename):    
    load_dotenv()
    with open(filename, 'rb') as file:
        asyncio.run(
            upload_file(
                os.environ['TELEGRAM_TOKEN'],
                os.environ['TELEGRAM_CHAT_ID'],
                file
            )
        )


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    load_dotenv()
    with open(args.filename, 'rb') as file:
        asyncio.run(
            upload_file(
                os.environ['TELEGRAM_TOKEN'],
                os.environ['TELEGRAM_CHAT_ID'],
                file
            )
        )
            


