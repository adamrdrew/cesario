import logging

class Log:
    def __init__(self, file_name):
        logging.basicConfig(filename=file_name, level=logging.DEBUG)

    def warning(self, message):
        logging.warning(message)
    
    def error(self, message):
        logging.error(message)
    
    def info(self, message):
        logging.info(message)