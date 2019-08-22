"""
A thin logger. Will be replaced by logging module
"""

class Logger(object):

    def __init__(self, name):
        self.name = name

    def info(self, msg):
        print('I - {name} - {msg}'.format(
            name=self.name,
            msg=msg))

    def warning(self, msg):
        print('W - {name} - {msg}'.format(
            name=self.name,
            msg=msg))


def getLogger(name):
    return Logger(name)
