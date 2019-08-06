# main.py -- put your code here!

from uphone.sender import Phone
from uphone.config import Config


config = Config('config.json')

phone = Phone(config)
phone.start()
