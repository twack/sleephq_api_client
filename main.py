# File: main.py
# Description: Main entry point for the application
#
import os
import logging
import time
import inspect
from lib import logger_conf 
from lib import viatom
from lib import resmed
from lib import withings
from lib.check_credentials import has_credentials
from lib.new_file_trigger import FileTrigger

# setup and configure the logger that is defined in the lib/logger_conf.py file
logger_conf.setup_logger()
logger = logging.getLogger(__name__)

def process_device_file(file, file_type):
    if file_type == 'viatom':
        viatom.process_viatom_file(file)
    elif file_type == 'resmed':
        resmed.process_resmed_file(file)
    elif file_type == 'withings':
        withings.process_withings_file(file)    
    else:
        logger.error(f"Unknown file type: {file_type}")
        
def main():
    # set the logging level to desired level
    logging.getLogger().setLevel(logging.INFO)
    
    # check for credentials
    if not has_credentials(silent=False):
        logger.error(f"[{inspect.currentframe().f_code.co_name}] >> CLIENT_UID and CLIENT_SECRET not found in environment variables or constants.py")
        logger.error(f"[{inspect.currentframe().f_code.co_name}] >> Exiting application!!!")
        return None
    
    logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Starting App to import files to SleepHQ...") 
    base_directory = os.path.dirname(os.path.realpath(__file__))
    file_store_directory = os.path.join(base_directory, 'file_stores')  # replace with your relative directory
    
    trigger = FileTrigger(file_store_directory, callback=process_device_file)
    # Start the FileTrigger
    trigger.start()
    
    try:
        while True:
            time.sleep(1)  # Keep the main thread running, otherwise it will exit and stop the FileTrigger thread
    except KeyboardInterrupt:
        # Stop the FileChecker when Ctrl-C is pressed
        trigger.stop()
        print('')
        logger.info(f"[{inspect.currentframe().f_code.co_name}] >> Stopped FileChecker due to KeyboardInterrupt.")

if __name__ == '__main__':
    main()
    

