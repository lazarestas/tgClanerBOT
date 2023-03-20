import datetime
import requests
from config import *
messages = [
    "@pidor1",
    "@pidor2",
    "@pidor3",
    "@pidor4"
]


def get_week_number(date):
    return date.isocalendar()[1]

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Error sending message: {response.content}")

today = datetime.date.today()
week_number = get_week_number(today)

message_index = (week_number - 1) % len(messages)
message_to_send = messages[message_index]

send_message(message_to_send)