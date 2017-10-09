import requests
from tokens import keys


def send_msg(msg):
    requests.post(keys["webhook_url"], data={"content": msg})
