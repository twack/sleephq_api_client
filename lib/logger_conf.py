"""
* logger_conf.py

* This module contains a function to set up a colored logger for the application.

* Functions:
* ----------
* - setup_logger(): Sets up a colored logger.
"""

import logging
import colorlog

def setup_logger():
    """
    * Sets up a colored logger.

    * This function creates a StreamHandler with a ColoredFormatter and adds it to the root logger. The log level is set to DEBUG, which means that messages with level DEBUG and above will be logged.

    * The ColoredFormatter is configured to include the log level, message, and timestamp in each log message. Different log levels are displayed in different colors.
    """
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'white',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'magenta',
        }
    ))

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)  # Set the minimum log level to DEBUG