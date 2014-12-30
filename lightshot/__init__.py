from flask import Flask

from lightshot.models.LoggerFactory import LoggerFactory

app = Flask(__name__)
app.config.from_envvar('LIGHTSHOT_SETTINGS')
logger = LoggerFactory(app.config['LS_LOG_PATH'])
app.logger.addHandler(logger.create_rotating_file_handler())

import lightshot.views