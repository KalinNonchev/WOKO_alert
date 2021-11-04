from urllib.request import urlopen
import ssl
import smtplib
import time
import random
from bs4 import BeautifulSoup
import yaml

with open("config.yaml", "r") as opened_file:
    config = yaml.safe_load(opened_file)


def send_message(content, receiver_email, sender_email, password):
    """
    Send email if the number of rooms on WOKO is changed
    :param content:
    :param receiver_email:
    :param sender_email:
    :param password:
    :return:
    """
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    message = f"Subject: You have a new post\n\n\n{content}.\n\n\nCheers,\nYour team"
    print(message)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print('Message send!')

def query_all_website():
    """
    Check the WOKO website for the number of available rooms
    :return: Number of rooms
    """
    url = "http://www.woko.ch/en/nachmieter-gesucht"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = [chunk for chunk in chunks if config["keyword"] in chunk]
    return text

def sleep():
    """
    Sleep time
    between 3 to 6 minutes
    :return:
    """
    timer = config["timer"] * random.choice([1, 2])
    print(f"Sleep for: {timer // 60}min.")
    time.sleep(timer)


memory_list = query_all_website()

while True:
    new_memory_list = query_all_website()

    if memory_list != new_memory_list:
        send_message(**config)
        print("Found!")
        memory_list = new_memory_list
        sleep()
    else:
        print(f"Still: {len(new_memory_list) - 3} rooms...")
        sleep()
