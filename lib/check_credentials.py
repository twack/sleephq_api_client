"""
* check_credentials.py

* This module contains a function to check if the SleepHQ user credentials are available.

* Functions:
* ----------
* - has_credentials(silent=None): Checks if the SleepHQ user credentials are available.
"""

import os
import inspect
import logging
import constants

logger = logging.getLogger(__name__)

def has_credentials(silent=None):
    """
    * Checks if the SleepHQ user credentials are available.

    * This function first checks if the credentials are set as environment variables. If not, it checks if they are set in the constants module.
    * If the credentials are not found in either place, it returns False. If they are found, it returns a dictionary containing the credentials.

    * Parameters:
    * -----------
    * silent : bool, optional
    *     If set to True, the function will not log any messages. Default is None, which means messages will be logged.

    * Returns:
    * --------
    * dict or bool
    *     If the credentials are found, returns a dictionary with 'client_uid' and 'client_secret' as keys. If not found, returns False.
    """
    if not silent:
        logger.warning(f"[{inspect.currentframe().f_code.co_name}] >> Checking for SleepHQ user credentials...")
        
    CLIENT_UID = os.getenv('CLIENT_UID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    if not CLIENT_UID or not CLIENT_SECRET:
        try:
            CLIENT_UID = constants.CLIENT_UID
            CLIENT_SECRET = constants.CLIENT_SECRET
        except AttributeError:
            return False

    if not CLIENT_UID or not CLIENT_SECRET:
        return False
    else:
        if not silent:
            logger.warning(f"[{inspect.currentframe().f_code.co_name}] >> SleepHQ credentials Found.")
            logger.warning(f"[{inspect.currentframe().f_code.co_name}] >> Credentials not checked for validity.")
        return {'client_uid': CLIENT_UID, 'client_secret': CLIENT_SECRET}