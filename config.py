import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Pusher:
    app_id: str = os.environ.get('PUSHER_APP_ID')
    key: str = os.environ.get('PUSHER_KEY')
    secret: str = os.environ.get('PUSHER_SECRET')
    cluster: str = os.environ.get('PUSHER_CLUSTER')
    ssl: bool = True
