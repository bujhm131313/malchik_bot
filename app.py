import datetime
from typing import List

import telegram
import os

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = -489188532


def get_options(is_weekend: bool = False) -> List[str]:
    if is_weekend:
        return [
            'ЩАС',
            '17:30',
            '18:00',
            '18:30',
            '19:00',
            '19:30',
            '20:00',
            '20:30',
            '21:00',
            '21:30',
        ]
    else:
        return [
            'ЩАС',
            '18:00',
            '18:30',
            '19:00',
            '19:30',
            '20:00',
            '20:30',
            '21:00',
            '21:30',
        ]


def send_message():
    bot = telegram.Bot(token=TOKEN)

    weekno = datetime.datetime.today().weekday()
    is_weekend = weekno > 4

    bot.send_poll(
        CHAT_ID,
        'Когда катаем?',
        options=get_options(is_weekend),
        is_anonymous=False,
        allows_multiple_answers=True,
        explanation='Время по Киеву, щеглы'
    )
