import datetime
import os
import requests
import logging
#lulw no leaks today
from config import *

# Set up logging
logging.basicConfig(filename='my_log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

day_of_notify = 0

# Define the messages to send
messages = [
    "@Nupellot короче ты знаешь что делать",
    "@Samamobaky, прошу прощенияб не могли бы вы провести мытье полов?",
    "@lazarestas тут не заигноришь уборочку",
    "@Lnkawai время мыть шконку:))))"
]

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        logging.error(f"Error sending message: {response.content}")

def count_weeks(date):
    """
    Counts the number of weeks from the beginning of 2023 to a given date.
    Assumes date is a datetime.date object.
    """
    start_date = datetime.date(2023, 1, 1)
    delta = date - start_date
    return delta.days // 7

# Get the current date and day of the week
today = datetime.datetime.today()
logging.info(today)
current_date = today.date()
logging.info(current_date)
day_of_week = today.weekday()
logging.info(day_of_week)

# Check if it's the day and if the script has not already been run on this day 
# in the current week
if day_of_week == day_of_notify and os.path.exists('tw_ran.txt') == False:
    logging.info(count_weeks(current_date))
    # Choose a random message to send
    message = messages[(count_weeks(current_date)) % len(messages)]
    logging.info(message)
    # Send the message to tg
    send_message(message)

    # Create a file to indicate that the script has been run on Tuesday this week
    with open('tw_ran.txt', 'w') as f:
        f.write(str(current_date))

elif day_of_week != day_of_notify:

    os.remove('tw_ran.txt')
    