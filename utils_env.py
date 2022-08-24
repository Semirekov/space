import collections
import os

from dotenv import load_dotenv


Env = collections.namedtuple('Env', ['nasa_token', 'telegram_token', 'chat_id', 'dir'])
def get_settins():    
    load_dotenv()
    return Env(
        os.environ['NASA_TOKEN'],
        os.environ['TELEGRAM_TOKEN'],
        os.environ['TELEGRAM_CHAT_ID'],
        os.getenv('TARGET_DIR', 'images'),
    )