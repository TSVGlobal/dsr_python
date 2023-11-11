from waitress import serve
from app import app
import os
import sys
import logging
from  logger import log_args_and_return

#Logging Configuration
log_format = '%(asctime)s %(levelname)s %(message)s'
log_level = logging.INFO
logging.basicConfig(format=log_format, level=log_level, stream=sys.stdout)

if __name__ == "__main__":
    try:
        @log_args_and_return
        def run_app():
            host = os.environ.get('SERVER_HOST', 'localhost')
            port = int(os.environ.get('SERVER_PORT', '9099'))
            serve(app, host=host, port=port)
        run_app()
    except Exception as e:
            logging.exception("An unhandled exception occured : $s", str(e))