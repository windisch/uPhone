# main.py -- put your code here!

from uphone import Phone
from uphone import Config


config = Config('config.json')

phone = Phone(config)
phone.start()
