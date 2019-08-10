import os

from dotenv import find_dotenv, load_dotenv
from telegram import Bot

load_dotenv(find_dotenv())


class TelegramBot:
    def __init__(self):
        self._token = os.environ.get('TELEGRAM_TOKEN')
        self._bot = Bot(token=self._token)

    def get_recent_messages(self, count=10):
        updates = self._bot.getUpdates()
        if updates:
            return [update.message for update in updates[-count:]]

    def send(self, message):
        self._last_message = self.get_recent_messages(count=1)
        if self._last_message:
            self._bot.sendMessage(
                chat_id=self._last_message[0].chat_id,
                text=message,
            )


if __name__ == '__main__':
    t = TelegramBot()
    print(t.get_recent_messages(3))
    t.send('hi')
