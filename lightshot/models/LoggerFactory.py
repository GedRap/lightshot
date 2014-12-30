import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
import os.path

class LoggerFactory:
    log_directory = None

    def __init__(self, log_directory = None, file_base_name = "lightshot.log"):
        self.log_directory = log_directory
        self.file_base_name = file_base_name

    # default to 1MB
    def create_rotating_file_handler(self, max_bytes = 1048576):
        self.handler = RotatingFileHandler(os.path.join(self.log_directory, self.file_base_name), maxBytes=max_bytes)

        self.handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))

        return self.handler